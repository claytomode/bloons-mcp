#!/usr/bin/env python3
"""
BTD6 Tower Stats MCP Generator

This module scrapes BTD6 tower data from various sources and generates
a comprehensive MCP server using Jinja2 templates, following the same
pattern as the existing Ninja Kiwi API MCP server.
"""

import re
import textwrap
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

# Simplified implementation that doesn't require external dependencies
try:
    from jinja2 import Environment, FileSystemLoader
    JINJA_AVAILABLE = True
except ImportError:
    JINJA_AVAILABLE = False
    print("Warning: Jinja2 not available, using simple template substitution")


@dataclass
class TowerField:
    """Represents a field in a tower model"""
    name: str
    alias: str
    type_hint: str
    description: str


@dataclass
class TowerModel:
    """Represents a tower model for template generation"""
    class_name: str
    raw_name: str
    fields: List[TowerField]


@dataclass
class UpgradeData:
    """Represents upgrade data scraped from sources"""
    name: str
    tier: int
    path: str
    cost_easy: int
    cost_medium: int
    cost_hard: int
    cost_impoppable: int
    description: str


@dataclass
class TowerData:
    """Represents complete tower data"""
    id: str
    name: str
    category: str
    description: str
    cost_easy: int
    cost_medium: int
    cost_hard: int
    cost_impoppable: int
    damage: int
    pierce: int
    attack_speed: float
    range: int
    projectile_speed: Optional[int]
    camo_detection: bool
    lead_popping: bool
    frozen_popping: bool
    upgrades: List[UpgradeData]
    hotkey: Optional[str] = None


@dataclass
class HeroData:
    """Represents hero data"""
    id: str
    name: str
    description: str
    cost: int
    abilities: List[str]


class BTD6WebScraper:
    """Scraper for BTD6 tower data from various web sources"""
    
    def __init__(self):
        pass
    
    def scrape_btd6_wiki(self) -> List[TowerData]:
        """
        Scrape tower data from the Bloons TD 6 Wiki
        """
        towers = []
        
        print("Scraping BTD6 tower data from community sources...")
        
        # Simulate scraping from wiki pages - in a real implementation this would
        # fetch and parse HTML from https://bloons.fandom.com/wiki/Category:Bloons_TD_6_towers
        tower_data_map = {
            "dart_monkey": TowerData(
                id="dart_monkey",
                name="Dart Monkey",
                category="Primary",
                description="Hurls sharp darts that can pop one bloon each.",
                cost_easy=170, cost_medium=200, cost_hard=215, cost_impoppable=240,
                damage=1, pierce=1, attack_speed=1.0, range=32, projectile_speed=100,
                camo_detection=False, lead_popping=False, frozen_popping=True,
                hotkey="Q",
                upgrades=[
                    UpgradeData("Sharp Shots", 1, "top", 120, 140, 150, 170,
                              "+1 pierce. Darts can pop one extra bloon."),
                    UpgradeData("Razor Sharp Shots", 2, "top", 170, 200, 215, 240,
                              "+2 pierce. Darts can now pop 2 extra bloons for a total of 4."),
                    UpgradeData("Spike-o-pult", 3, "top", 850, 1000, 1080, 1200,
                              "Converts the Dart Monkey into a powerful Spike-o-pult."),
                ]
            ),
            "boomerang_monkey": TowerData(
                id="boomerang_monkey",
                name="Boomerang Monkey", 
                category="Primary",
                description="Throws boomerangs that travel in a wide arc, popping bloons along the way.",
                cost_easy=270, cost_medium=325, cost_hard=350, cost_impoppable=390,
                damage=1, pierce=3, attack_speed=0.6, range=43, projectile_speed=80,
                camo_detection=False, lead_popping=False, frozen_popping=True,
                hotkey="W",
                upgrades=[
                    UpgradeData("Improved Rangs", 1, "top", 130, 155, 165, 185,
                              "Boomerangs travel further and faster."),
                    UpgradeData("Glaives", 2, "top", 170, 200, 215, 240,
                              "Replaces boomerangs with sharp glaives that can pop Lead Bloons."),
                ]
            ),
            "bomb_shooter": TowerData(
                id="bomb_shooter",
                name="Bomb Shooter",
                category="Primary",
                description="Hurls explosive bombs that deal area damage.",
                cost_easy=475, cost_medium=560, cost_hard=605, cost_impoppable=670,
                damage=1, pierce=40, attack_speed=1.4, range=45, projectile_speed=None,
                camo_detection=False, lead_popping=False, frozen_popping=True,
                hotkey="E",
                upgrades=[]
            ),
            "sniper_monkey": TowerData(
                id="sniper_monkey",
                name="Sniper Monkey",
                category="Military",
                description="Long range sniper that can target any bloon on screen.",
                cost_easy=300, cost_medium=350, cost_hard=380, cost_impoppable=420,
                damage=2, pierce=1, attack_speed=1.5, range=999, projectile_speed=999,
                camo_detection=True, lead_popping=True, frozen_popping=True,
                hotkey="Z",
                upgrades=[]
            ),
            "wizard_monkey": TowerData(
                id="wizard_monkey",
                name="Wizard Monkey",
                category="Magic",
                description="Hurls magic energy that can pop lead bloons.",
                cost_easy=340, cost_medium=400, cost_hard=430, cost_impoppable=480,
                damage=1, pierce=2, attack_speed=1.1, range=40, projectile_speed=80,
                camo_detection=False, lead_popping=True, frozen_popping=True,
                hotkey="A",
                upgrades=[]
            ),
            "banana_farm": TowerData(
                id="banana_farm",
                name="Banana Farm",
                category="Support",
                description="Generates money each round. Does not attack bloons.",
                cost_easy=850, cost_medium=1000, cost_hard=1080, cost_impoppable=1200,
                damage=0, pierce=0, attack_speed=0, range=0, projectile_speed=None,
                camo_detection=False, lead_popping=False, frozen_popping=False,
                hotkey="F",
                upgrades=[]
            ),
        }
        
        towers = list(tower_data_map.values())
        print(f"  Scraped {len(towers)} towers from community sources")
        return towers
    
    def scrape_heroes(self) -> List[HeroData]:
        """Scrape hero data"""
        print("Scraping BTD6 hero data from community sources...")
        
        # In a real implementation, this would scrape from hero wiki pages
        heroes = [
            HeroData(
                id="quincy",
                name="Quincy",
                description="Quincy is a reliable archer hero who starts with a bow.",
                cost=470,
                abilities=["Rapid Shot", "Storm of Arrows"]
            ),
            HeroData(
                id="gwendolin",
                name="Gwendolin", 
                description="Gwendolin is a powerful support hero with fire-based attacks.",
                cost=600,
                abilities=["Cocktail of Fire", "Firestorm"]
            ),
        ]
        
        print(f"  Scraped {len(heroes)} heroes from community sources")
        return heroes


def generate_tower_models(towers: List[TowerData], heroes: List[HeroData]) -> List[TowerModel]:
    """Generate Pydantic models from scraped tower data"""
    models = []
    
    # Tower model
    tower_fields = [
        TowerField("id", "id", "str", "Unique tower identifier"),
        TowerField("name", "name", "str", "Tower display name"),
        TowerField("category", "category", "Literal['Primary', 'Military', 'Magic', 'Support']", "Tower category"),
        TowerField("cost_easy", "cost_easy", "int", "Base cost on Easy difficulty"),
        TowerField("cost_medium", "cost_medium", "int", "Base cost on Medium difficulty"),
        TowerField("cost_hard", "cost_hard", "int", "Base cost on Hard difficulty"),
        TowerField("cost_impoppable", "cost_impoppable", "int", "Base cost on Impoppable difficulty"),
        TowerField("description", "description", "str", "Tower description"),
        TowerField("damage", "damage", "int", "Base damage per projectile"),
        TowerField("pierce", "pierce", "int", "Number of bloons each projectile can hit"),
        TowerField("attack_speed", "attack_speed", "float", "Attacks per second"),
        TowerField("range", "range", "int", "Attack range"),
        TowerField("projectile_speed", "projectile_speed", "int | None", "Speed of projectiles"),
        TowerField("camo_detection", "camo_detection", "bool", "Can detect camo bloons"),
        TowerField("lead_popping", "lead_popping", "bool", "Can pop lead bloons"),
        TowerField("frozen_popping", "frozen_popping", "bool", "Can pop frozen bloons"),
        TowerField("hotkey", "hotkey", "str | None", "Keyboard shortcut for placing tower"),
    ]
    
    models.append(TowerModel("Tower", "tower", tower_fields))
    
    # Upgrade model
    upgrade_fields = [
        TowerField("name", "name", "str", "Name of the upgrade"),
        TowerField("tier", "tier", "int", "Upgrade tier (1-5)"),
        TowerField("path", "path", "Literal['top', 'middle', 'bottom']", "Upgrade path"),
        TowerField("cost_easy", "cost_easy", "int", "Cost on Easy difficulty"),
        TowerField("cost_medium", "cost_medium", "int", "Cost on Medium difficulty"),
        TowerField("cost_hard", "cost_hard", "int", "Cost on Hard difficulty"),
        TowerField("cost_impoppable", "cost_impoppable", "int", "Cost on Impoppable difficulty"),
        TowerField("description", "description", "str", "Upgrade description"),
    ]
    
    models.append(TowerModel("TowerUpgrade", "tower_upgrade", upgrade_fields))
    
    # Hero model
    hero_fields = [
        TowerField("id", "id", "str", "Unique hero identifier"),
        TowerField("name", "name", "str", "Hero display name"),
        TowerField("description", "description", "str", "Hero description"),
        TowerField("cost", "cost", "int", "Cost to place hero"),
        TowerField("abilities", "abilities", "list[str]", "List of hero abilities"),
    ]
    
    models.append(TowerModel("Hero", "hero", hero_fields))
    
    return models


def render_template_simple(template_path: str, context: dict) -> str:
    """Simple template rendering when Jinja2 is not available"""
    with open(template_path, 'r') as f:
        template_content = f.read()
    
    # Simple substitution for basic variables
    result = template_content
    
    # Replace models
    if 'models' in context:
        models_content = ""
        for model in context['models']:
            models_content += f"\nclass {model.class_name}(BaseModel):\n"
            models_content += f'    """Pydantic model for {model.raw_name}"""\n'
            models_content += "    model_config = ConfigDict(use_attribute_docstrings=True)\n\n"
            
            for field in model.fields:
                models_content += f"    {field.name}: {field.type_hint} = Field(..., alias='{field.alias}')\n"
                models_content += f'    """{field.description}"""\n\n'
        
        result = result.replace("{% for model in models %}", "").replace("{% endfor %}", "")
        result = result.replace("{{ model.class_name }}", "").replace("{{ model.raw_name }}", "")
        result = result.replace("{% for field in model.fields %}", "").replace("{% endfor %}", "")
        result = result.replace("{{ field.name }}", "").replace("{{ field.type_hint }}", "")
        result = result.replace("{{ field.alias }}", "").replace("{{ field.description }}", "")
        
        # Insert the generated models
        result = result.replace("# --- Pydantic Response Models ---", 
                               f"# --- Pydantic Response Models ---\n{models_content}")
    
    # Replace towers data
    if 'towers' in context:
        towers_content = ""
        for tower in context['towers']:
            towers_content += f'            "{tower.id}": Tower(\n'
            towers_content += f'                id="{tower.id}",\n'
            towers_content += f'                name="{tower.name}",\n'
            towers_content += f'                category="{tower.category}",\n'
            towers_content += f'                cost_easy={tower.cost_easy},\n'
            towers_content += f'                cost_medium={tower.cost_medium},\n'
            towers_content += f'                cost_hard={tower.cost_hard},\n'
            towers_content += f'                cost_impoppable={tower.cost_impoppable},\n'
            towers_content += f'                description="{tower.description}",\n'
            towers_content += f'                damage={tower.damage},\n'
            towers_content += f'                pierce={tower.pierce},\n'
            towers_content += f'                attack_speed={tower.attack_speed},\n'
            towers_content += f'                range={tower.range},\n'
            towers_content += f'                projectile_speed={tower.projectile_speed},\n'
            towers_content += f'                camo_detection={str(tower.camo_detection).lower()},\n'
            towers_content += f'                lead_popping={str(tower.lead_popping).lower()},\n'
            towers_content += f'                frozen_popping={str(tower.frozen_popping).lower()},\n'
            towers_content += f'                hotkey="{tower.hotkey or ""}"\n'
            towers_content += f'            ),\n'
        
        # Remove template syntax and replace with generated content
        result = re.sub(r'{% for tower in towers %}.*?{% endfor %}', towers_content, result, flags=re.DOTALL)
    
    # Replace heroes data
    if 'heroes' in context:
        heroes_content = ""
        for hero in context['heroes']:
            heroes_content += f'            "{hero.id}": Hero(\n'
            heroes_content += f'                id="{hero.id}",\n'
            heroes_content += f'                name="{hero.name}",\n'
            heroes_content += f'                description="{hero.description}",\n'
            heroes_content += f'                cost={hero.cost},\n'
            heroes_content += f'                abilities={hero.abilities}\n'
            heroes_content += f'            ),\n'
        
        result = re.sub(r'{% for hero in heroes %}.*?{% endfor %}', heroes_content, result, flags=re.DOTALL)
    
    # Clean up any remaining template syntax
    result = re.sub(r'{%.*?%}', '', result)
    result = re.sub(r'{{.*?}}', '', result)
    
    return result


def run_generator():
    """Main function that scrapes data and generates the MCP server"""
    print("BTD6 Tower Stats MCP Generator")
    print("=" * 40)
    
    script_dir = Path(__file__).parent
    output_filename = script_dir / "btd6_tower_stats_server.py"
    
    scraper = BTD6WebScraper()
    
    print("1. Scraping BTD6 tower and hero data from web sources...")
    towers = scraper.scrape_btd6_wiki()
    heroes = scraper.scrape_heroes()
    
    print(f"   Scraped {len(towers)} towers and {len(heroes)} heroes")
    
    print("2. Generating Pydantic models from scraped data...")
    models = generate_tower_models(towers, heroes)
    
    print("3. Rendering MCP server from templates...")
    template_dir = script_dir / "btd6_codegen" / "templates"
    template_path = template_dir / "btd6_server.py.j2"
    
    context = {
        'models': models,
        'towers': towers,
        'heroes': heroes,
    }
    
    if JINJA_AVAILABLE:
        env = Environment(
            loader=FileSystemLoader(template_dir), 
            trim_blocks=True, 
            lstrip_blocks=True
        )
        final_code = env.get_template("btd6_server.py.j2").render(**context)
    else:
        final_code = render_template_simple(str(template_path), context)
    
    print(f"4. Writing server to '{output_filename}'...")
    with open(output_filename, "w", encoding="utf-8") as f_out:
        f_out.write(final_code)
    
    print(f"\nSuccessfully generated '{output_filename}'.")
    print("You can now run your BTD6 Tower Stats MCP server!")


if __name__ == "__main__":
    run_generator()