import asyncio
import re
import textwrap

import httpx
from lxml import html


def to_snake_case(name: str) -> str:
    """Converts a string from camelCase to snake_case."""
    s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def to_pascal_case(name: str) -> str:
    """Converts a string like '_btd6_race' to 'Btd6Race'."""
    name = name.lstrip('_')
    name = name.replace('btd6', 'Btd6').replace('battles2', 'Battles2')
    return "".join(part.capitalize() for part in re.split('_|-', name))


def map_type_hint(type_str: str) -> str:
    """Maps the documentation type string to a Python type hint."""
    type_str = type_str.strip().lower()
    if not type_str:
        return "Any"

    if ',' in type_str:
        literals = [f"'{val.strip()}'" for val in type_str.split(',')]
        return f"Literal[{', '.join(literals)}]"

    type_map = {
        "string": "str", "number": "int | float", "boolean": "bool",
        "array": "list", "string[]": "list[str]", "map": "dict[str, Any]",
        "nestedmap": "dict[str, Any]", "asseturl": "str", "raw": "dict[str, Any]",
    }
    return type_map.get(type_str, "Any")


def generate_api_wrapper(html_content: str) -> str:
    """
    Parses Ninja Kiwi API docs to generate a Pydantic-powered Python API wrapper.
    """
    tree = html.fromstring(html_content)
    
    model_definitions = ""
    processed_models = set()
    model_title_elements = tree.xpath('//div[contains(text(), "Response Model:")]')

    for title_elem in model_title_elements:
        model_name_raw = title_elem.text_content().replace("Response Model:", "").strip()
        if model_name_raw in processed_models:
            continue
        processed_models.add(model_name_raw)
        
        class_name = to_pascal_case(model_name_raw)
        field_lines = []
        
        param_container = title_elem.xpath('./following-sibling::div[contains(@class, "container-fluid")][1]')
        if not param_container:
            continue

        field_rows = param_container[0].xpath('.//div[@class="row nkEndpointSectionParameter"]')
        for row in field_rows:
            cols = row.xpath('./div')
            if len(cols) > 2:
                raw_field_name = cols[0].text_content().strip()
                
                if raw_field_name.startswith('_'):
                    python_field_name = to_snake_case(raw_field_name.lstrip('_')) + '_data'
                else:
                    python_field_name = to_snake_case(raw_field_name)

                field_desc = " ".join(cols[1].text_content().strip().split())
                field_type_str = cols[2].text_content().strip()
                py_type = map_type_hint(field_type_str)
                
                field_lines.append(f"{python_field_name}: {py_type} | None = Field(default=None, alias='{raw_field_name}')")
                field_lines.append(f'"""{field_desc}"""')

        all_fields_str = "\n".join(field_lines) if field_lines else "pass"
        indented_fields = textwrap.indent(all_fields_str, ' ' * 4)
            
        model_code = f"class {class_name}(BaseModel):\n"
        model_code += f'    """Pydantic model for {model_name_raw}"""\n'
        model_code += "    model_config = ConfigDict(use_attribute_docstrings=True)\n\n"
        model_code += f"{indented_fields}\n\n\n"
        model_definitions += model_code

    method_blocks = [
        textwrap.dedent("""
        def __init__(self, base_url="https://data.ninjakiwi.com"):
            self.client = httpx.AsyncClient(base_url=base_url, follow_redirects=True)

        async def _get_request(self, endpoint: str) -> Any | None:
            \"\"\"Internal method to handle GET requests.\"\"\"
            try:
                response = await self.client.get(endpoint)
                response.raise_for_status()
                data = response.json()
                if data and data.get('error'):
                    print(f"API Error for {endpoint}: {data['error']}")
                    return None
                return data.get('body')
            except httpx.HTTPStatusError as e:
                print(f"HTTP Error for endpoint '{endpoint}': {e}")
                return None
            except (httpx.RequestError, json.JSONDecodeError) as e:
                print(f"An error occurred with endpoint '{endpoint}': {e}")
                return None

        async def close(self):
            \"\"\"Closes the httpx client.\"\"\"
            await self.client.aclose()
    """)]
    
    menu = tree.xpath('//div[contains(@class, "nkLeftMenu")]')[0]
    endpoints = menu.xpath('.//a[contains(@class, "nkAnchor")]')

    for endpoint in endpoints:
        path = endpoint.xpath('.//div[contains(@class, "nkLeftMenuItemTitle")]/text()')[0].strip()
        description = endpoint.xpath('.//div[contains(@class, "nkLeftMenuItemBody")]/text()')[0].strip()
        
        endpoint_section = tree.xpath(f'//div[@id="{path}"]/following-sibling::div[1]')
        
        model_name, return_model, is_list = "Any", "Any | None", False
        
        if endpoint_section:
            model_title_elem = endpoint_section[0].xpath('.//div[contains(text(), "Response Model:")]')
            if model_title_elem:
                model_name_raw = model_title_elem[0].text_content().replace("Response Model:", "").strip()
                model_name = to_pascal_case(model_name_raw)
                
                if (":" not in path) or "leaderboard" in path or "filter" in path or "/maps" == path or "matches" in path or "homs" in path:
                    is_list = True
                    return_model = f"list[{model_name}] | None"
                else:
                    return_model = f"{model_name} | None"

        params = [to_snake_case(p) for p in re.findall(r':(\w+)', path)]

        clean_path = path.replace("/", " ").replace(":", " by ")
        clean_path = re.sub(r'\s+', '_', clean_path).strip('_')
        function_name = to_snake_case("get_" + clean_path)
        
        endpoint_fstring = path.strip('/')
        for param in re.findall(r':(\w+)', path):
                endpoint_fstring = endpoint_fstring.replace(f":{param}", f"{{{to_snake_case(param)}}}")

        params_with_types = ", ".join([f"{p}: str" for p in params])
        func_params_str = f", {params_with_types}" if params_with_types else ""
        
        parsing_logic = ""
        if model_name == "Any":
            parsing_logic = "return body"
        elif is_list:
            parsing_logic = textwrap.dedent(f"""
                if not body or not isinstance(body, list):
                    return None
                try:
                    return [{model_name}.model_validate(item) for item in body]
                except ValidationError as e:
                    print(f"Pydantic validation error for endpoint '{{endpoint}}': {{e}}")
                    return None
            """)
        else:
            parsing_logic = textwrap.dedent(f"""
                if not body or not isinstance(body, dict):
                    return None
                try:
                    return {model_name}.model_validate(body)
                except ValidationError as e:
                    print(f"Pydantic validation error for endpoint '{{endpoint}}': {{e}}")
                    return None
            """)
        
        method_lines = [
            f"async def {function_name}(self{func_params_str}) -> {return_model}:",
            f'    """',
            f'    {description}',
            f'    URL: https://data.ninjakiwi.com{path}',
            f'    """',
            f'    endpoint = f"{endpoint_fstring}"',
            f'    body = await self._get_request(endpoint)',
            textwrap.indent(parsing_logic, '    ')
        ]
        
        method_blocks.append("\n".join(method_lines))

    imports_and_header = textwrap.dedent("""
    import httpx
    import json
    import asyncio
    from typing import Literal, Any, Optional
    from pydantic import BaseModel, ConfigDict, Field, ValidationError

    """)
    
    all_methods_code = "\n\n".join(method_blocks)
    indented_methods = textwrap.indent(all_methods_code, ' ' * 4)
    
    api_class_code = f"""class NinjaKiwiAPI:
    \"\"\"
    An asynchronous Python wrapper for the Bloons TD 6 and Battles 2 Data API.
    \"\"\"
{indented_methods}
"""

    main_block = textwrap.dedent("""

    async def main():
        \"\"\"Example usage of the auto-generated NinjaKiwiAPI wrapper.\"\"\"
        api = NinjaKiwiAPI()
        print("Welcome to the BTD6 API Wrapper Example!")
        print("-" * 40)

        try:
            print("\\nFetching BTD6 races...")
            races = await api.get_btd6_races()
            
            if races and len(races) > 0:
                latest_race = races[0]
                print(f"Successfully fetched {len(races)} races. Latest race: '{latest_race.name}' (ID: {latest_race.id})")

                if latest_race.id:
                    print(f"\\nFetching leaderboard for race: {latest_race.name}...")
                    leaderboard = await api.get_btd6_races_by_race_id_leaderboard(race_id=latest_race.id)
                    if leaderboard and len(leaderboard) > 0:
                        top_player = leaderboard[0]
                        print(f"Top player: {top_player.display_name} with score {top_player.score}")
                    else:
                        print("Could not retrieve leaderboard or it is empty.")
            else:
                print("Failed to fetch BTD6 races or no races are available.")

        finally:
            print("\\nClosing API client.")
            await api.close()


    if __name__ == "__main__":
        asyncio.run(main())
    """)
    
    return f"{imports_and_header}# --- Pydantic Response Models ---\n{model_definitions.strip()}\n\n# --- API Client Class ---\n{api_class_code}\n{main_block}"


async def run_generator():
    """Fetches the API docs and generates the wrapper script."""
    url = "https://data.ninjakiwi.com/"
    output_filename = 'btd6_api_wrapper.py'
    
    print("--- API Wrapper Generator Script ---")
    print(f"Fetching latest API documentation from {url}...")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            html_input = response.text
        
        print("Documentation fetched successfully. Generating Pydantic API wrapper...")
        generated_code = generate_api_wrapper(html_input)
        
        with open(output_filename, 'w', encoding='utf-8') as f_out:
            f_out.write(generated_code)
        
        print(f"\\nSuccessfully generated '{output_filename}'.")

    except httpx.RequestError as e:
        print(f"\\nError: Could not fetch the documentation page. Details: {e}")
    except Exception as e:
        print(f"\\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(run_generator())