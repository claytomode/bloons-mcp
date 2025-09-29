import asyncio
import re
import textwrap
from pathlib import Path

import httpx
from jinja2 import Environment, FileSystemLoader
from lxml import html


def to_snake_case(name: str) -> str:
    """Converts a string from camelCase to snake_case."""
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def to_pascal_case(name: str) -> str:
    """Converts a string like '_btd6_race' to 'Btd6Race'."""
    name = name.lstrip("_")
    name = name.replace("btd6", "Btd6").replace("battles2", "Battles2")
    return "".join(part.capitalize() for part in re.split("_|-", name))


def map_type_hint(type_str: str) -> str:
    """Maps the documentation type string to a Python type hint."""
    type_str = type_str.strip().lower()
    if not type_str:
        return "Any"

    if "," in type_str:
        literals = [f"'{val.strip()}'" for val in type_str.split(",")]
        return f"Literal[{', '.join(literals)}]"

    type_map = {
        "string": "str",
        "number": "int | float",
        "boolean": "bool",
        "array": "list",
        "string[]": "list[str]",
        "map": "dict[str, Any]",
        "nestedmap": "dict[str, Any]",
        "asseturl": "str",
        "raw": "dict[str, Any]",
    }
    return type_map.get(type_str, "Any")


def generate_pydantic_models(tree: html.HtmlElement) -> str:
    """Parses HTML and generates complete Pydantic model class strings."""
    model_definitions = []
    processed_models = set()
    model_title_elements = tree.xpath('//div[contains(text(), "Response Model:")]')

    for title_elem in model_title_elements:
        model_name_raw = title_elem.text_content().replace("Response Model:", "").strip()
        if model_name_raw in processed_models:
            continue
        processed_models.add(model_name_raw)

        class_name = to_pascal_case(model_name_raw)
        fields_data = []

        param_container = title_elem.xpath(
            './following-sibling::div[contains(@class, "container-fluid")][1]'
        )
        if not param_container:
            continue

        field_rows = param_container[0].xpath(
            './/div[@class="row nkEndpointSectionParameter"]'
        )
        for row in field_rows:
            cols = row.xpath("./div")
            if len(cols) > 2:
                raw_field_name = cols[0].text_content().strip()

                python_field_name = to_snake_case(raw_field_name.lstrip("_"))
                if raw_field_name.startswith("_"):
                    python_field_name += "_data"

                field_desc = " ".join(cols[1].text_content().strip().split())
                py_type = map_type_hint(cols[2].text_content().strip())

                fields_data.append(
                    {
                        "name": python_field_name,
                        "type_hint": py_type,
                        "alias": raw_field_name,
                        "description": field_desc or "No description available.",
                    }
                )

        field_strings = []
        for field in fields_data:
            field_def = f"{field['name']}: {field['type_hint']} | None = Field(default=None, alias='{field['alias']}')"
            docstring = f'"""{field["description"]}"""'
            field_strings.append(f"{field_def}\n    {docstring}")

        all_fields_str = "\n\n    ".join(field_strings) if field_strings else "pass"

        model_code = f"""class {class_name}(BaseModel):
    \"\"\"Pydantic model for {model_name_raw}\"\"\"
    model_config = ConfigDict(use_attribute_docstrings=True)

    {all_fields_str}
"""
        model_definitions.append(model_code)

    return "\n\n".join(model_definitions)


def parse_api_methods(tree: html.HtmlElement) -> list[dict]:
    """Parses the HTML to extract data for API client methods."""
    methods_data = []
    endpoints = tree.xpath(
        '//div[contains(@class, "nkLeftMenu")]//a[contains(@class, "nkAnchor")]'
    )

    for endpoint in endpoints:
        path = endpoint.xpath(
            './/div[contains(@class, "nkLeftMenuItemTitle")]/text()'
        )[0].strip()
        description = endpoint.xpath(
            './/div[contains(@class, "nkLeftMenuItemBody")]/text()'
        )[0].strip()

        endpoint_section = tree.xpath(f'//div[@id="{path}"]/following-sibling::div[1]')

        model_name, return_model, is_list = "Any", "Any | None", False

        if endpoint_section:
            model_title_elem = endpoint_section[0].xpath(
                './/div[contains(text(), "Response Model:")]'
            )
            if model_title_elem:
                model_name_raw = (
                    model_title_elem[0]
                    .text_content()
                    .replace("Response Model:", "")
                    .strip()
                )
                model_name = to_pascal_case(model_name_raw)

                list_triggers = ["leaderboard", "filter", "matches", "homs"]
                if (
                    (":" not in path)
                    or any(trigger in path for trigger in list_triggers)
                    or path.endswith("/maps")
                ):
                    is_list = True
                    return_model = f"list[{model_name}] | None"
                else:
                    return_model = f"{model_name} | None"

        params = [to_snake_case(p) for p in re.findall(r":(\w+)", path)]

        clean_path = path.replace("/", " ").replace(":", " by ").strip()
        clean_path = re.sub(r"\s+", "_", clean_path)
        function_name = to_snake_case(f"get_{clean_path}")

        endpoint_fstring = path.strip("/")
        for param in re.findall(r":(\w+)", path):
            endpoint_fstring = endpoint_fstring.replace(
                f":{param}", f"{{{to_snake_case(param)}}}"
            )

        methods_data.append(
            {
                "name": function_name,
                "description": description,
                "url": path,
                "params": params,
                "endpoint_fstring": endpoint_fstring,
                "return_type": return_model,
                "model_name": model_name,
                "is_list": is_list,
            }
        )
    return methods_data


async def run_generator():
    """Fetches the API docs and generates the wrapper script using templates."""
    SCRIPT_DIR = Path(__file__).parent.resolve()
    PROJECT_ROOT = SCRIPT_DIR.parent
    url = "https://data.ninjakiwi.com/"
    output_filename = PROJECT_ROOT / "fastmcp_server.py"

    print("--- FastMCP Server Generator Script ---")

    print(f"1. Fetching latest API documentation from {url}...")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            html_input = response.text
    except httpx.RequestError as e:
        print(f"\nError: Could not fetch the documentation page. Details: {e}")
        return
    except Exception as e:
        print(f"\nAn unexpected error occurred during fetch: {e}")
        return

    print("2. Parsing HTML and generating code components...")
    tree = html.fromstring(html_input)

    rendered_models = generate_pydantic_models(tree)
    methods_data = parse_api_methods(tree)

    print("3. Rendering final FastMCP server from templates...")
    template_dir = SCRIPT_DIR / "templates"
    env = Environment(
        loader=FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True
    )

    rendered_methods_list = [
        textwrap.indent(env.get_template("api_method.py.j2").render(method=m), " " * 4)
        for m in methods_data
    ]
    
    client_class_name = "NinjaKiwiAPI"
    rendered_mcp_server_block = env.get_template("mcp_server_block.py.j2").render(
        methods=methods_data,
        client_class_name=client_class_name,
        module_name=output_filename.stem
    )

    final_code = env.get_template("wrapper.py.j2").render(
        pydantic_models=rendered_models,
        api_client_class_name=client_class_name,
        methods="\n\n".join(rendered_methods_list),
        mcp_server_block=rendered_mcp_server_block,
    )

    print(f"4. Writing server to '{output_filename}'...")
    with open(output_filename, "w", encoding="utf-8") as f_out:
        f_out.write(final_code)

    print(f"\nSuccessfully generated '{output_filename}'.")
    print("You can now run your server with: uvicorn fastmcp_server:app --reload")


if __name__ == "__main__":
    asyncio.run(run_generator())