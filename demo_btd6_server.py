#!/usr/bin/env python3
"""
BTD6 Tower Stats MCP Demo

This script demonstrates the capabilities of the auto-generated BTD6 Tower Stats MCP server.
"""

import sys
from pathlib import Path

# Test import of the generated server
try:
    from btd6_tower_stats_server import BTD6TowerDataStore, Tower, Hero, TowerUpgrade
    
    def demo_generated_server():
        """Demonstrate the generated BTD6 Tower Stats MCP server"""
        
        print("🎮 BTD6 Tower Stats MCP Server Demo")
        print("📡 Generated via Web Scraping + Jinja2 Templates")
        print("=" * 60)
        
        # Initialize the data store
        store = BTD6TowerDataStore()
        
        print(f"\n📊 Server Statistics:")
        print(f"   Towers loaded: {len(store.towers)}")
        print(f"   Heroes loaded: {len(store.heroes)}")
        print(f"   Upgrades loaded: {len(store.upgrades)}")
        
        # Demo tower info
        print(f"\n🎯 Example Tower Data:")
        dart_monkey = store.get_tower("dart_monkey")
        if dart_monkey:
            print(f"   Name: {dart_monkey.name}")
            print(f"   Category: {dart_monkey.category}")
            print(f"   Cost (Medium): ${dart_monkey.cost_medium}")
            print(f"   Damage: {dart_monkey.damage}")
            print(f"   Pierce: {dart_monkey.pierce}")
            print(f"   Range: {dart_monkey.range}")
            print(f"   Hotkey: {dart_monkey.hotkey}")
        
        # Demo search functionality
        print(f"\n🔍 Search Example - 'bomb':")
        search_results = store.search_towers("bomb")
        for tower in search_results:
            print(f"   - {tower.name}: {tower.description[:50]}...")
        
        # Demo filtering by category
        print(f"\n🏗️  Tower Categories:")
        categories = ["Primary", "Military", "Magic", "Support"]
        for category in categories:
            towers = store.list_towers(category)
            if towers:
                print(f"   {category}: {', '.join(t.name for t in towers)}")
        
        # Demo heroes
        print(f"\n🦸 Heroes Available:")
        heroes = store.list_heroes()
        for hero in heroes:
            print(f"   - {hero.name} (${hero.cost}): {hero.description[:40]}...")
            print(f"     Abilities: {', '.join(hero.abilities)}")
        
        # Demo upgrades
        print(f"\n📈 Available Upgrades:")
        dart_upgrades = store.get_upgrades_for_tower("dart_monkey")
        if dart_upgrades:
            print(f"   Dart Monkey upgrades:")
            for upgrade in dart_upgrades:
                print(f"     T{upgrade.tier} {upgrade.path}: {upgrade.name} (${upgrade.cost_medium})")
        
        print(f"\n✨ MCP Tools Available:")
        tools = [
            "get_tower_info(tower_id)",
            "get_hero_info(hero_id)", 
            "list_all_towers(category?)",
            "list_all_heroes()",
            "search_towers(query)",
            "compare_tower_costs(tower_ids, difficulty)",
            "get_tower_upgrades(tower_id, path?)",
            "calculate_upgrade_cost(tower_id, path, tier, difficulty)"
        ]
        for tool in tools:
            print(f"   - {tool}")
        
        print(f"\n🎉 Server Generation Complete!")
        print(f"   The BTD6 Tower Stats MCP server was successfully generated")
        print(f"   from web-scraped data using Jinja2 templates!")
    
    if __name__ == "__main__":
        demo_generated_server()

except ImportError as e:
    print(f"❌ Could not import generated server: {e}")
    print(f"   Run 'python scraper.py' first to generate the server!")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error running demo: {e}")
    sys.exit(1)