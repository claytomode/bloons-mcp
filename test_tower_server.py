#!/usr/bin/env python3
"""
Test script for the BTD6 Tower Stats MCP Server
"""

import sys
import json
from pathlib import Path

# Add the current directory to Python path to import our server
sys.path.insert(0, "/home/runner/work/bloons-mcp/bloons-mcp")

try:
    from tower_stats_server import TowerDataStore, Tower, Hero
    
    def test_tower_data_store():
        """Test the TowerDataStore functionality"""
        print("Testing TowerDataStore...")
        
        # Initialize with data file
        data_file = "/home/runner/work/bloons-mcp/bloons-mcp/btd6_data.json"
        store = TowerDataStore(data_file)
        
        print(f"Loaded {len(store.towers)} towers and {len(store.heroes)} heroes")
        
        # Test getting a specific tower
        dart_monkey = store.get_tower("dart_monkey")
        if dart_monkey:
            print(f"Found Dart Monkey: {dart_monkey.name}")
            print(f"  Category: {dart_monkey.category}")
            print(f"  Base cost (medium): ${dart_monkey.cost_medium}")
            print(f"  Base damage: {dart_monkey.base_stats.damage}")
            print(f"  Base pierce: {dart_monkey.base_stats.pierce}")
            print(f"  Number of upgrades: {len(dart_monkey.upgrades)}")
        
        # Test listing towers by category
        primary_towers = store.list_towers("Primary")
        print(f"\nPrimary towers: {len(primary_towers)}")
        for tower in primary_towers:
            print(f"  - {tower.name}")
        
        # Test searching towers
        search_results = store.search_towers("sharp")
        print(f"\nTowers matching 'sharp': {len(search_results)}")
        for tower in search_results:
            print(f"  - {tower.name}")
        
        # Test heroes
        quincy = store.get_hero("quincy")
        if quincy:
            print(f"\nFound hero: {quincy.name}")
            print(f"  Cost: ${quincy.cost}")
            print(f"  Abilities: {len(quincy.abilities)}")
        
        print("\nTowerDataStore tests completed successfully!")
        return True
    
    def test_tower_models():
        """Test the Pydantic models"""
        print("\nTesting Pydantic models...")
        
        # Test that we can create models from the data
        with open("/home/runner/work/bloons-mcp/bloons-mcp/btd6_data.json", 'r') as f:
            data = json.load(f)
        
        tower_data = data["towers"][0]  # Get first tower
        print(f"Testing with tower: {tower_data['name']}")
        
        # This should work if our models are correct
        try:
            from tower_stats_server import TowerStats, TowerUpgrade, Tower
            
            # Create base stats
            stats = TowerStats(
                damage=tower_data["base_stats"]["damage"],
                pierce=tower_data["base_stats"]["pierce"],
                attack_speed=tower_data["base_stats"]["attack_speed"],
                range=tower_data["base_stats"]["range"],
                projectile_speed=tower_data["base_stats"].get("projectile_speed"),
                camo_detection=tower_data["base_stats"]["camo_detection"],
                lead_popping=tower_data["base_stats"]["lead_popping"],
                frozen_popping=tower_data["base_stats"]["frozen_popping"]
            )
            
            print("✓ TowerStats model works")
            
            # Create upgrades
            upgrades = []
            for upgrade_data in tower_data["upgrades"]:
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
            
            print("✓ TowerUpgrade model works")
            
            # Create tower
            tower = Tower(
                id="test_tower",
                name=tower_data["name"],
                category=tower_data["category"],
                cost_easy=tower_data["base_cost"]["easy"],
                cost_medium=tower_data["base_cost"]["medium"],
                cost_hard=tower_data["base_cost"]["hard"],
                cost_impoppable=tower_data["base_cost"]["impoppable"],
                description=tower_data["description"],
                base_stats=stats,
                upgrades=upgrades,
                hotkey=tower_data.get("hotkey")
            )
            
            print("✓ Tower model works")
            print("✓ All Pydantic models are working correctly!")
            
        except Exception as e:
            print(f"✗ Model validation failed: {e}")
            return False
        
        return True
    
    if __name__ == "__main__":
        print("Running BTD6 Tower Stats MCP Server Tests\n")
        
        success = True
        
        # Run tests
        success &= test_tower_data_store()
        success &= test_tower_models()
        
        if success:
            print("\n🎉 All tests passed!")
        else:
            print("\n❌ Some tests failed!")
            sys.exit(1)

except ImportError as e:
    print(f"Import error: {e}")
    print("Make sure all dependencies are available")
    sys.exit(1)