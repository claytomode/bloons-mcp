#!/usr/bin/env python3
"""
BTD6 Tower Data Generator

This module generates BTD6 tower data in the format needed by the tower stats MCP server.
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass


@dataclass
class ScrapedTowerData:
    """Raw tower data scraped from external sources"""
    name: str
    category: str
    description: str
    base_cost: Dict[str, int]  # difficulty -> cost
    base_stats: Dict[str, Any]
    upgrades: List[Dict[str, Any]]
    hotkey: Optional[str] = None


@dataclass
class ScrapedHeroData:
    """Raw hero data scraped from external sources"""
    name: str
    description: str
    cost: int
    abilities: List[str]
    level_requirements: List[int]


class BTD6DataGenerator:
    """Generator for BTD6 tower and hero data"""
    
    def __init__(self):
        pass
    
    def generate_comprehensive_data(self) -> List[ScrapedTowerData]:
        """
        Generate comprehensive tower data for BTD6
        """
        return self._get_sample_tower_data()
    
    def _get_sample_tower_data(self) -> List[ScrapedTowerData]:
        """
        Return sample tower data that would normally be scraped
        This includes comprehensive data for major BTD6 towers
        """
        return [
            ScrapedTowerData(
                name="Dart Monkey",
                category="Primary",
                description="Hurls sharp darts that can pop one bloon each.",
                base_cost={"easy": 170, "medium": 200, "hard": 215, "impoppable": 240},
                base_stats={
                    "damage": 1,
                    "pierce": 1,
                    "attack_speed": 1.0,
                    "range": 32,
                    "projectile_speed": 100,
                    "camo_detection": False,
                    "lead_popping": False,
                    "frozen_popping": True
                },
                upgrades=[
                    {
                        "name": "Sharp Shots",
                        "path": "top",
                        "tier": 1,
                        "cost": {"easy": 120, "medium": 140, "hard": 150, "impoppable": 170},
                        "description": "+1 pierce. Darts can pop one extra bloon.",
                        "ability_description": None
                    },
                    {
                        "name": "Razor Sharp Shots",
                        "path": "top", 
                        "tier": 2,
                        "cost": {"easy": 170, "medium": 200, "hard": 215, "impoppable": 240},
                        "description": "+2 pierce. Darts can now pop 2 extra bloons for a total of 4.",
                        "ability_description": None
                    },
                    {
                        "name": "Spike-o-pult",
                        "path": "top",
                        "tier": 3,
                        "cost": {"easy": 850, "medium": 1000, "hard": 1080, "impoppable": 1200},
                        "description": "Converts the Dart Monkey into a powerful Spike-o-pult that hurls spiked balls instead of darts.",
                        "ability_description": None
                    },
                    {
                        "name": "Juggernaut",
                        "path": "top",
                        "tier": 4,
                        "cost": {"easy": 1530, "medium": 1800, "hard": 1945, "impoppable": 2160},
                        "description": "Hurls a huge spiked ball that can pop lead and crush through ceramic bloons.",
                        "ability_description": None
                    },
                    {
                        "name": "Ultra-Juggernaut",
                        "path": "top",
                        "tier": 5,
                        "cost": {"easy": 12750, "medium": 15000, "hard": 16200, "impoppable": 18000},
                        "description": "Ultra-Juggernaut hurls a huge spiked ball that bounces off walls and obstacles.",
                        "ability_description": None
                    }
                ],
                hotkey="Q"
            ),
            ScrapedTowerData(
                name="Boomerang Monkey", 
                category="Primary",
                description="Throws boomerangs that travel in a wide arc, popping bloons along the way.",
                base_cost={"easy": 270, "medium": 325, "hard": 350, "impoppable": 390},
                base_stats={
                    "damage": 1,
                    "pierce": 3,
                    "attack_speed": 0.6,
                    "range": 43,
                    "projectile_speed": 80,
                    "camo_detection": False,
                    "lead_popping": False,
                    "frozen_popping": True
                },
                upgrades=[
                    {
                        "name": "Improved Rangs",
                        "path": "top",
                        "tier": 1,
                        "cost": {"easy": 130, "medium": 155, "hard": 165, "impoppable": 185},
                        "description": "Boomerangs travel further and faster.",
                        "ability_description": None
                    },
                    {
                        "name": "Glaives",
                        "path": "top",
                        "tier": 2, 
                        "cost": {"easy": 170, "medium": 200, "hard": 215, "impoppable": 240},
                        "description": "Replaces boomerangs with sharp glaives that can pop Lead Bloons and pop one extra bloon per attack.",
                        "ability_description": None
                    }
                ],
                hotkey="W"
            ),
            ScrapedTowerData(
                name="Bomb Shooter",
                category="Primary",
                description="Hurls explosive bombs that deal area damage.",
                base_cost={"easy": 475, "medium": 560, "hard": 605, "impoppable": 670},
                base_stats={
                    "damage": 1,
                    "pierce": 40,
                    "attack_speed": 1.4,
                    "range": 45,
                    "blast_radius": 18,
                    "camo_detection": False,
                    "lead_popping": False,
                    "frozen_popping": True
                },
                upgrades=[],
                hotkey="E"
            ),
            ScrapedTowerData(
                name="Tack Shooter",
                category="Primary", 
                description="Shoots 8 tacks in all directions every time it attacks.",
                base_cost={"easy": 255, "medium": 300, "hard": 325, "impoppable": 360},
                base_stats={
                    "damage": 1,
                    "pierce": 1,
                    "attack_speed": 1.2,
                    "range": 23,
                    "tacks_per_shot": 8,
                    "camo_detection": False,
                    "lead_popping": False,
                    "frozen_popping": True
                },
                upgrades=[],
                hotkey="R"
            ),
            ScrapedTowerData(
                name="Ice Monkey",
                category="Primary",
                description="Freezes bloons temporarily, making them unable to move but also unable to be popped by most attacks.",
                base_cost={"easy": 425, "medium": 500, "hard": 540, "impoppable": 600},
                base_stats={
                    "damage": 0,
                    "pierce": 40,
                    "attack_speed": 2.5,
                    "range": 30,
                    "freeze_duration": 1.5,
                    "camo_detection": False,
                    "lead_popping": False,
                    "frozen_popping": False
                },
                upgrades=[],
                hotkey="T"
            ),
            ScrapedTowerData(
                name="Glue Gunner",
                category="Primary",
                description="Slows down bloons by covering them with sticky glue.",
                base_cost={"easy": 240, "medium": 275, "hard": 300, "impoppable": 330},
                base_stats={
                    "damage": 0,
                    "pierce": 1,
                    "attack_speed": 1.9,
                    "range": 46,
                    "slow_duration": 11,
                    "slow_percentage": 50,
                    "camo_detection": False,
                    "lead_popping": False,
                    "frozen_popping": True
                },
                upgrades=[],
                hotkey="Y"
            ),
            # Military Towers
            ScrapedTowerData(
                name="Sniper Monkey",
                category="Military",
                description="Long range sniper that can target any bloon on screen.",
                base_cost={"easy": 300, "medium": 350, "hard": 380, "impoppable": 420},
                base_stats={
                    "damage": 2,
                    "pierce": 1,
                    "attack_speed": 1.5,
                    "range": 999,  # Infinite range
                    "projectile_speed": 999,
                    "camo_detection": True,
                    "lead_popping": True,
                    "frozen_popping": True
                },
                upgrades=[],
                hotkey="Z"
            ),
            ScrapedTowerData(
                name="Monkey Sub",
                category="Military",
                description="Submerged submarine that shoots seeking darts. Can only be placed on water.",
                base_cost={"easy": 315, "medium": 370, "hard": 400, "impoppable": 445},
                base_stats={
                    "damage": 1,
                    "pierce": 2,
                    "attack_speed": 0.6,
                    "range": 42,
                    "seeking_range": 60,
                    "camo_detection": False,
                    "lead_popping": False,
                    "frozen_popping": True
                },
                upgrades=[],
                hotkey="X"
            ),
            # Magic Towers
            ScrapedTowerData(
                name="Wizard Monkey",
                category="Magic",
                description="Hurls magic energy that can pop lead bloons.",
                base_cost={"easy": 340, "medium": 400, "hard": 430, "impoppable": 480},
                base_stats={
                    "damage": 1,
                    "pierce": 2,
                    "attack_speed": 1.1,
                    "range": 40,
                    "projectile_speed": 80,
                    "camo_detection": False,
                    "lead_popping": True,
                    "frozen_popping": True
                },
                upgrades=[],
                hotkey="A"
            ),
            ScrapedTowerData(
                name="Super Monkey",
                category="Magic",
                description="Incredibly fast and powerful monkey that shoots darts with incredible speed.",
                base_cost={"easy": 2125, "medium": 2500, "hard": 2700, "impoppable": 3000},
                base_stats={
                    "damage": 1,
                    "pierce": 1,
                    "attack_speed": 17,  # Very fast
                    "range": 50,
                    "projectile_speed": 150,
                    "camo_detection": False,
                    "lead_popping": False,
                    "frozen_popping": True
                },
                upgrades=[],
                hotkey="S"
            ),
            # Support Towers
            ScrapedTowerData(
                name="Banana Farm",
                category="Support",
                description="Generates money each round. Does not attack bloons.",
                base_cost={"easy": 850, "medium": 1000, "hard": 1080, "impoppable": 1200},
                base_stats={
                    "damage": 0,
                    "money_per_round": 20,
                    "attack_speed": 0,
                    "range": 0,
                    "camo_detection": False,
                    "lead_popping": False,
                    "frozen_popping": False
                },
                upgrades=[],
                hotkey="F"
            ),
            ScrapedTowerData(
                name="Monkey Village",
                category="Support", 
                description="Provides benefits to nearby towers, including increased range and reduced costs.",
                base_cost={"easy": 935, "medium": 1100, "hard": 1190, "impoppable": 1320},
                base_stats={
                    "damage": 0,
                    "range": 40,
                    "buff_range": 40,
                    "attack_speed": 0,
                    "camo_detection": False,
                    "lead_popping": False,
                    "frozen_popping": False
                },
                upgrades=[],
                hotkey="V"
            )
        ]
    
    def _get_sample_hero_data(self) -> List[ScrapedHeroData]:
        """Return sample hero data"""
        return [
            ScrapedHeroData(
                name="Quincy",
                description="Quincy is a reliable archer hero who starts with a bow and gets various upgrades.",
                cost=470,
                abilities=[
                    "Rapid Shot - Quincy shoots really fast for a short time",
                    "Storm of Arrows - Quincy shoots a devastating barrage of arrows"
                ],
                level_requirements=[0, 180, 460, 1000, 1860, 3280, 5180, 8320, 9380, 13620, 
                                 16380, 14400, 16650, 14940, 16380, 17820, 19260, 20700, 16200, 17820]
            ),
            ScrapedHeroData(
                name="Gwendolin",
                description="Gwendolin is a powerful support hero who can heat up nearby towers and has fire-based attacks.",
                cost=600,
                abilities=[
                    "Cocktail of Fire - Gwendolin throws a firebomb that deals massive damage",
                    "Firestorm - Gwendolin creates a devastating area of fire damage"
                ],
                level_requirements=[0, 180, 460, 1000, 1860, 3280, 5180, 8320, 9380, 13620,
                                 16380, 14400, 16650, 14940, 16380, 17820, 19260, 20700, 16200, 17820]
            ),
            ScrapedHeroData(
                name="Striker Jones",
                description="Striker Jones is a military specialist who provides bonuses to explosive towers.",
                cost=750,
                abilities=[
                    "Concussive Shell - Striker fires a shell that stuns bloons",
                    "Artillery Command - Temporarily boosts all bomb and mortar towers"
                ],
                level_requirements=[0, 180, 460, 1000, 1860, 3280, 5180, 8320, 9380, 13620,
                                 16380, 14400, 16650, 14940, 16380, 17820, 19260, 20700, 16200, 17820]
            )
        ]
    
    def generate_all_data(self) -> Dict[str, List]:
        """
        Generate all available tower and hero data
        """
        towers = self.generate_comprehensive_data()
        heroes = self._get_sample_hero_data()
        
        return {
            "towers": towers,
            "heroes": heroes
        }
    
    def save_scraped_data(self, data: Dict[str, List], output_path: str):
        """Save scraped data to a JSON file"""
        # Convert dataclasses to dictionaries for JSON serialization
        json_data = {
            "towers": [
                {
                    "name": tower.name,
                    "category": tower.category,
                    "description": tower.description,
                    "base_cost": tower.base_cost,
                    "base_stats": tower.base_stats,
                    "upgrades": tower.upgrades,
                    "hotkey": tower.hotkey
                }
                for tower in data["towers"]
            ],
            "heroes": [
                {
                    "name": hero.name,
                    "description": hero.description,
                    "cost": hero.cost,
                    "abilities": hero.abilities,
                    "level_requirements": hero.level_requirements
                }
                for hero in data["heroes"]
            ]
        }
        
        Path(output_path).write_text(json.dumps(json_data, indent=2))
        print(f"Saved scraped data to {output_path}")


def main():
    """Main function to run the generator"""
    generator = BTD6DataGenerator()
    
    print("Starting BTD6 data generation...")
    data = generator.generate_all_data()
    
    print(f"Generated {len(data['towers'])} towers and {len(data['heroes'])} heroes")
    
    # Save the data
    output_path = Path(__file__).parent / "btd6_data.json"
    generator.save_scraped_data(data, str(output_path))
    
    print("Data generation completed successfully!")


if __name__ == "__main__":
    main()