#!/usr/bin/env python3
"""
BTD6 Tower Stats MCP Server

This server provides comprehensive information about Bloons Tower Defense 6 towers,
including stats, descriptions, upgrade paths, and detailed ability information.
"""

import asyncio
import json
from typing import Any, Literal, Optional
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field
from fastmcp import FastMCP


# --- Tower Data Models ---

class TowerUpgrade(BaseModel):
    """Represents a single tower upgrade"""
    model_config = ConfigDict(use_attribute_docstrings=True)
    
    name: str = Field(..., description="Name of the upgrade")
    path: Literal["top", "middle", "bottom"] = Field(..., description="Upgrade path (top/middle/bottom)")
    tier: int = Field(..., ge=1, le=5, description="Upgrade tier (1-5)")
    cost_easy: int = Field(..., description="Cost on Easy difficulty")
    cost_medium: int = Field(..., description="Cost on Medium difficulty")
    cost_hard: int = Field(..., description="Cost on Hard difficulty")
    cost_impoppable: int = Field(..., description="Cost on Impoppable difficulty")
    description: str = Field(..., description="Upgrade description")
    ability_description: Optional[str] = Field(default=None, description="Special ability description if applicable")


class TowerStats(BaseModel):
    """Represents base tower statistics"""
    model_config = ConfigDict(use_attribute_docstrings=True)
    
    damage: int = Field(..., description="Base damage per projectile")
    pierce: int = Field(..., description="Number of bloons each projectile can hit")
    attack_speed: float = Field(..., description="Attacks per second")
    range: int = Field(..., description="Attack range")
    projectile_speed: Optional[int] = Field(default=None, description="Speed of projectiles")
    camo_detection: bool = Field(default=False, description="Can detect camo bloons")
    lead_popping: bool = Field(default=False, description="Can pop lead bloons")
    frozen_popping: bool = Field(default=False, description="Can pop frozen bloons")


class Tower(BaseModel):
    """Represents a complete BTD6 tower"""
    model_config = ConfigDict(use_attribute_docstrings=True)
    
    id: str = Field(..., description="Unique tower identifier")
    name: str = Field(..., description="Tower display name")
    category: Literal["Primary", "Military", "Magic", "Support"] = Field(..., description="Tower category")
    cost_easy: int = Field(..., description="Base cost on Easy difficulty")
    cost_medium: int = Field(..., description="Base cost on Medium difficulty") 
    cost_hard: int = Field(..., description="Base cost on Hard difficulty")
    cost_impoppable: int = Field(..., description="Base cost on Impoppable difficulty")
    description: str = Field(..., description="Tower description")
    base_stats: TowerStats = Field(..., description="Base tower statistics")
    upgrades: list[TowerUpgrade] = Field(default_factory=list, description="All available upgrades")
    hotkey: Optional[str] = Field(default=None, description="Keyboard shortcut for placing tower")


class Hero(BaseModel):
    """Represents a BTD6 hero"""
    model_config = ConfigDict(use_attribute_docstrings=True)
    
    id: str = Field(..., description="Unique hero identifier")
    name: str = Field(..., description="Hero display name")
    description: str = Field(..., description="Hero description")
    cost: int = Field(..., description="Cost to place hero")
    abilities: list[str] = Field(default_factory=list, description="List of hero abilities by level")
    level_requirements: list[int] = Field(default_factory=list, description="XP required for each level")


# --- In-Memory Data Store ---
class TowerDataStore:
    """Manages tower and hero data"""
    
    def __init__(self, data_file: Optional[str] = None):
        self.towers: dict[str, Tower] = {}
        self.heroes: dict[str, Hero] = {}
        
        if data_file and Path(data_file).exists():
            self._load_from_file(data_file)
        else:
            self._load_sample_data()
    
    def _load_from_file(self, data_file: str):
        """Load tower and hero data from a JSON file"""
        try:
            with open(data_file, 'r') as f:
                data = json.load(f)
            
            # Load towers
            for tower_data in data.get("towers", []):
                tower_id = tower_data["name"].lower().replace(" ", "_").replace("-", "_")
                
                # Convert upgrades
                upgrades = []
                for upgrade_data in tower_data.get("upgrades", []):
                    upgrade = TowerUpgrade(
                        name=upgrade_data["name"],
                        path=upgrade_data["path"],
                        tier=upgrade_data["tier"],
                        cost_easy=upgrade_data["cost"]["easy"],
                        cost_medium=upgrade_data["cost"]["medium"],
                        cost_hard=upgrade_data["cost"]["hard"],
                        cost_impoppable=upgrade_data["cost"]["impoppable"],
                        description=upgrade_data["description"],
                        ability_description=upgrade_data.get("ability_description")
                    )
                    upgrades.append(upgrade)
                
                # Convert base stats
                stats_data = tower_data["base_stats"]
                base_stats = TowerStats(
                    damage=stats_data.get("damage", 0),
                    pierce=stats_data.get("pierce", 1),
                    attack_speed=stats_data.get("attack_speed", 1.0),
                    range=stats_data.get("range", 30),
                    projectile_speed=stats_data.get("projectile_speed"),
                    camo_detection=stats_data.get("camo_detection", False),
                    lead_popping=stats_data.get("lead_popping", False),
                    frozen_popping=stats_data.get("frozen_popping", True)
                )
                
                # Create tower
                tower = Tower(
                    id=tower_id,
                    name=tower_data["name"],
                    category=tower_data["category"],
                    cost_easy=tower_data["base_cost"]["easy"],
                    cost_medium=tower_data["base_cost"]["medium"],
                    cost_hard=tower_data["base_cost"]["hard"],
                    cost_impoppable=tower_data["base_cost"]["impoppable"],
                    description=tower_data["description"],
                    base_stats=base_stats,
                    upgrades=upgrades,
                    hotkey=tower_data.get("hotkey")
                )
                
                self.towers[tower_id] = tower
            
            # Load heroes
            for hero_data in data.get("heroes", []):
                hero_id = hero_data["name"].lower().replace(" ", "_")
                
                hero = Hero(
                    id=hero_id,
                    name=hero_data["name"],
                    description=hero_data["description"],
                    cost=hero_data["cost"],
                    abilities=hero_data["abilities"],
                    level_requirements=hero_data["level_requirements"]
                )
                
                self.heroes[hero_id] = hero
                
            print(f"Loaded {len(self.towers)} towers and {len(self.heroes)} heroes from {data_file}")
            
        except Exception as e:
            print(f"Error loading data from {data_file}: {e}")
            print("Falling back to sample data")
            self._load_sample_data()
    
    def _load_sample_data(self):
        """Load sample tower data - in a real implementation this would load from scraped data"""
        
        # Sample Primary towers
        dart_monkey = Tower(
            id="dart_monkey",
            name="Dart Monkey",
            category="Primary",
            cost_easy=170,
            cost_medium=200,
            cost_hard=215,
            cost_impoppable=240,
            description="Hurls sharp darts that can pop one bloon each.",
            hotkey="Q",
            base_stats=TowerStats(
                damage=1,
                pierce=1,
                attack_speed=1.0,
                range=32,
                projectile_speed=100
            ),
            upgrades=[
                TowerUpgrade(
                    name="Sharp Shots",
                    path="top",
                    tier=1,
                    cost_easy=120,
                    cost_medium=140,
                    cost_hard=150,
                    cost_impoppable=170,
                    description="+1 pierce. Darts can pop one extra bloon."
                ),
                TowerUpgrade(
                    name="Razor Sharp Shots", 
                    path="top",
                    tier=2,
                    cost_easy=170,
                    cost_medium=200,
                    cost_hard=215,
                    cost_impoppable=240,
                    description="+2 pierce. Darts can now pop 2 extra bloons for a total of 4."
                ),
                # Add more upgrades...
            ]
        )
        
        boomerang_monkey = Tower(
            id="boomerang_monkey",
            name="Boomerang Monkey",
            category="Primary", 
            cost_easy=270,
            cost_medium=325,
            cost_hard=350,
            cost_impoppable=390,
            description="Throws boomerangs that travel in a wide arc, popping bloons along the way.",
            hotkey="W",
            base_stats=TowerStats(
                damage=1,
                pierce=3,
                attack_speed=0.6,
                range=43,
                projectile_speed=80
            ),
            upgrades=[]  # Would be populated with real data
        )
        
        # Sample Military tower
        sniper_monkey = Tower(
            id="sniper_monkey",
            name="Sniper Monkey",
            category="Military",
            cost_easy=300,
            cost_medium=350,
            cost_hard=380,
            cost_impoppable=420,
            description="Long range sniper that can target any bloon on screen.",
            hotkey="Z",
            base_stats=TowerStats(
                damage=2,
                pierce=1,
                attack_speed=1.5,
                range=999,  # Infinite range
                projectile_speed=999,
                camo_detection=True
            ),
            upgrades=[]
        )
        
        # Sample Hero
        quincy = Hero(
            id="quincy",
            name="Quincy",
            description="Quincy is a reliable archer hero who starts with a bow and gets various upgrades.",
            cost=470,
            abilities=[
                "Rapid Shot - Quincy shoots really fast for a short time",
                "Storm of Arrows - Quincy shoots a devastating barrage of arrows"
            ],
            level_requirements=[0, 180, 460, 1000, 1860, 3280, 5180, 8320, 9380, 13620, 16380, 14400, 16650, 14940, 16380, 17820, 19260, 20700, 16200, 17820]
        )
        
        # Store the data
        self.towers[dart_monkey.id] = dart_monkey
        self.towers[boomerang_monkey.id] = boomerang_monkey  
        self.towers[sniper_monkey.id] = sniper_monkey
        self.heroes[quincy.id] = quincy
    
    def get_tower(self, tower_id: str) -> Optional[Tower]:
        """Get a tower by ID"""
        return self.towers.get(tower_id)
    
    def get_hero(self, hero_id: str) -> Optional[Hero]:
        """Get a hero by ID"""
        return self.heroes.get(hero_id)
    
    def list_towers(self, category: Optional[str] = None) -> list[Tower]:
        """List all towers, optionally filtered by category"""
        towers = list(self.towers.values())
        if category:
            towers = [t for t in towers if t.category.lower() == category.lower()]
        return towers
    
    def list_heroes(self) -> list[Hero]:
        """List all heroes"""
        return list(self.heroes.values())
    
    def search_towers(self, query: str) -> list[Tower]:
        """Search towers by name or description"""
        query = query.lower()
        results = []
        for tower in self.towers.values():
            if (query in tower.name.lower() or 
                query in tower.description.lower() or
                any(query in upgrade.name.lower() for upgrade in tower.upgrades)):
                results.append(tower)
        return results


# --- FastMCP Server Setup ---
data_file = Path(__file__).parent / "btd6_data.json"
tower_data = TowerDataStore(str(data_file))

mcp = FastMCP(
    name="btd6-tower-stats",
    instructions="An MCP server providing comprehensive BTD6 tower statistics, upgrade paths, and detailed information.",
)


# --- Tool Registration ---

@mcp.tool
async def get_tower_info(tower_id: str) -> Tower | None:
    """
    Get detailed information about a specific tower including stats and upgrades.
    
    Args:
        tower_id: The unique identifier for the tower (e.g., 'dart_monkey', 'sniper_monkey')
    
    Returns:
        Complete tower information including base stats and all upgrades, or None if not found
    """
    return tower_data.get_tower(tower_id)


@mcp.tool  
async def get_hero_info(hero_id: str) -> Hero | None:
    """
    Get detailed information about a specific hero.
    
    Args:
        hero_id: The unique identifier for the hero (e.g., 'quincy', 'gwendolin')
    
    Returns:
        Complete hero information including abilities and level requirements, or None if not found
    """
    return tower_data.get_hero(hero_id)


@mcp.tool
async def list_all_towers(category: Optional[str] = None) -> list[Tower]:
    """
    List all available towers, optionally filtered by category.
    
    Args:
        category: Optional filter by tower category ('Primary', 'Military', 'Magic', 'Support')
    
    Returns:
        List of towers matching the criteria
    """
    return tower_data.list_towers(category)


@mcp.tool
async def list_all_heroes() -> list[Hero]:
    """
    List all available heroes.
    
    Returns:
        List of all heroes with their basic information
    """
    return tower_data.list_heroes()


@mcp.tool
async def search_towers(query: str) -> list[Tower]:
    """
    Search for towers by name, description, or upgrade names.
    
    Args:
        query: Search term to match against tower information
        
    Returns:
        List of towers that match the search criteria
    """
    return tower_data.search_towers(query)


@mcp.tool
async def compare_tower_costs(tower_ids: list[str], difficulty: Literal["easy", "medium", "hard", "impoppable"] = "medium") -> dict[str, int]:
    """
    Compare the base costs of multiple towers on a specific difficulty.
    
    Args:
        tower_ids: List of tower IDs to compare
        difficulty: Game difficulty level for cost comparison
        
    Returns:
        Dictionary mapping tower IDs to their costs on the specified difficulty
    """
    costs = {}
    for tower_id in tower_ids:
        tower = tower_data.get_tower(tower_id)
        if tower:
            if difficulty == "easy":
                costs[tower_id] = tower.cost_easy
            elif difficulty == "medium":
                costs[tower_id] = tower.cost_medium
            elif difficulty == "hard":
                costs[tower_id] = tower.cost_hard
            elif difficulty == "impoppable":
                costs[tower_id] = tower.cost_impoppable
    return costs


@mcp.tool
async def get_upgrade_path(tower_id: str, path: Literal["top", "middle", "bottom"]) -> list[TowerUpgrade]:
    """
    Get all upgrades for a specific tower path.
    
    Args:
        tower_id: The unique identifier for the tower
        path: The upgrade path ('top', 'middle', or 'bottom')
        
    Returns:
        List of upgrades for the specified path, ordered by tier
    """
    tower = tower_data.get_tower(tower_id)
    if not tower:
        return []
    
    path_upgrades = [upgrade for upgrade in tower.upgrades if upgrade.path == path]
    return sorted(path_upgrades, key=lambda x: x.tier)


@mcp.tool
async def calculate_total_upgrade_cost(tower_id: str, path: Literal["top", "middle", "bottom"], 
                                     tier: int, difficulty: Literal["easy", "medium", "hard", "impoppable"] = "medium") -> dict[str, Any]:
    """
    Calculate the total cost to upgrade a tower to a specific tier on a specific path.
    
    Args:
        tower_id: The unique identifier for the tower
        path: The upgrade path ('top', 'middle', or 'bottom')
        tier: Target tier (1-5)
        difficulty: Game difficulty level for cost calculation
        
    Returns:
        Dictionary with base cost, upgrade costs, and total cost
    """
    tower = tower_data.get_tower(tower_id)
    if not tower:
        return {"error": "Tower not found"}
    
    # Get base cost
    if difficulty == "easy":
        base_cost = tower.cost_easy
    elif difficulty == "medium":
        base_cost = tower.cost_medium
    elif difficulty == "hard":
        base_cost = tower.cost_hard
    elif difficulty == "impoppable":
        base_cost = tower.cost_impoppable
    
    # Get upgrade costs for the path up to the specified tier
    path_upgrades = [upgrade for upgrade in tower.upgrades 
                    if upgrade.path == path and upgrade.tier <= tier]
    path_upgrades.sort(key=lambda x: x.tier)
    
    upgrade_costs = []
    total_upgrade_cost = 0
    
    for upgrade in path_upgrades:
        if difficulty == "easy":
            cost = upgrade.cost_easy
        elif difficulty == "medium":
            cost = upgrade.cost_medium
        elif difficulty == "hard":
            cost = upgrade.cost_hard
        elif difficulty == "impoppable":
            cost = upgrade.cost_impoppable
            
        upgrade_costs.append({"name": upgrade.name, "tier": upgrade.tier, "cost": cost})
        total_upgrade_cost += cost
    
    return {
        "tower_id": tower_id,
        "path": path,
        "target_tier": tier,
        "difficulty": difficulty,
        "base_cost": base_cost,
        "upgrades": upgrade_costs,
        "total_upgrade_cost": total_upgrade_cost,
        "total_cost": base_cost + total_upgrade_cost
    }


if __name__ == "__main__":
    print("Starting BTD6 Tower Stats MCP Server...")
    mcp.run()