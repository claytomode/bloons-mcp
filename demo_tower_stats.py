#!/usr/bin/env python3
"""
BTD6 Tower Stats Demo

This script demonstrates the capabilities of the BTD6 Tower Stats MCP server
by showing the data structure and available information.
"""

import json
from pathlib import Path

def demo_tower_data():
    """Demonstrate the comprehensive tower data available"""
    
    print("🎮 BTD6 Tower Stats MCP Server Demo\n")
    
    # Load the generated data
    data_file = "/home/runner/work/bloons-mcp/bloons-mcp/btd6_data.json"
    
    if not Path(data_file).exists():
        print("❌ Data file not found. Run 'python scraper.py' first!")
        return
    
    with open(data_file, 'r') as f:
        data = json.load(f)
    
    towers = data["towers"]
    heroes = data["heroes"]
    
    print(f"📊 Database contains {len(towers)} towers and {len(heroes)} heroes\n")
    
    # Demo 1: Show tower categories
    categories = {}
    for tower in towers:
        category = tower["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append(tower["name"])
    
    print("🏗️  Tower Categories:")
    for category, tower_names in categories.items():
        print(f"   {category}: {len(tower_names)} towers")
        for name in tower_names[:3]:  # Show first 3
            print(f"     - {name}")
        if len(tower_names) > 3:
            print(f"     ... and {len(tower_names) - 3} more")
        print()
    
    # Demo 2: Detailed tower example
    dart_monkey = next(t for t in towers if t["name"] == "Dart Monkey")
    print("🎯 Example Tower: Dart Monkey")
    print(f"   Description: {dart_monkey['description']}")
    print(f"   Category: {dart_monkey['category']}")
    print(f"   Hotkey: {dart_monkey.get('hotkey', 'N/A')}")
    print(f"   Base Cost (Medium): ${dart_monkey['base_cost']['medium']}")
    
    stats = dart_monkey["base_stats"]
    print("   Base Stats:")
    print(f"     - Damage: {stats['damage']}")
    print(f"     - Pierce: {stats['pierce']}")
    print(f"     - Attack Speed: {stats['attack_speed']}/sec")
    print(f"     - Range: {stats['range']}")
    print(f"     - Can detect camo: {stats['camo_detection']}")
    print(f"     - Can pop lead: {stats['lead_popping']}")
    
    print(f"   Upgrades: {len(dart_monkey['upgrades'])} available")
    for upgrade in dart_monkey["upgrades"][:3]:  # Show first 3
        print(f"     - {upgrade['name']} (Tier {upgrade['tier']}, {upgrade['path']} path)")
        print(f"       Cost: ${upgrade['cost']['medium']} | {upgrade['description']}")
    print()
    
    # Demo 3: Cost comparison
    print("💰 Cost Comparison (Medium Difficulty):")
    tower_costs = [(t["name"], t["base_cost"]["medium"]) for t in towers]
    tower_costs.sort(key=lambda x: x[1])
    
    print("   Cheapest towers:")
    for name, cost in tower_costs[:5]:
        print(f"     ${cost:4d} - {name}")
    
    print("   Most expensive towers:")
    for name, cost in tower_costs[-3:]:
        print(f"     ${cost:4d} - {name}")
    print()
    
    # Demo 4: Hero information
    print("🦸 Heroes Available:")
    for hero in heroes:
        print(f"   {hero['name']} (${hero['cost']})")
        print(f"     {hero['description']}")
        print(f"     Abilities: {len(hero['abilities'])}")
        for ability in hero["abilities"][:2]:  # Show first 2 abilities
            print(f"       - {ability}")
        print()
    
    # Demo 5: Search capabilities
    print("🔍 Search Example: Towers with 'sharp' in name or upgrades:")
    for tower in towers:
        matches = []
        if "sharp" in tower["name"].lower():
            matches.append("name")
        for upgrade in tower["upgrades"]:
            if "sharp" in upgrade["name"].lower():
                matches.append(f"upgrade: {upgrade['name']}")
        
        if matches:
            print(f"   {tower['name']} - matches in: {', '.join(matches)}")
    print()
    
    # Demo 6: Upgrade path analysis
    print("📈 Upgrade Path Example: Dart Monkey Top Path")
    top_path_upgrades = [u for u in dart_monkey["upgrades"] if u["path"] == "top"]
    top_path_upgrades.sort(key=lambda x: x["tier"])
    
    total_cost = dart_monkey["base_cost"]["medium"]
    print(f"   Base Tower: ${total_cost}")
    
    for upgrade in top_path_upgrades:
        upgrade_cost = upgrade["cost"]["medium"]
        total_cost += upgrade_cost
        print(f"   Tier {upgrade['tier']}: {upgrade['name']} (+${upgrade_cost}) = ${total_cost}")
    
    print(f"   Total cost for 5-0-0 Dart Monkey: ${total_cost}")
    print()
    
    # Demo 7: Available MCP tools
    print("🔧 Available MCP Tools:")
    tools = [
        "get_tower_info(tower_id) - Get detailed tower information",
        "list_all_towers(category?) - List towers by category",
        "search_towers(query) - Search towers by text",
        "get_hero_info(hero_id) - Get hero information", 
        "list_all_heroes() - List all heroes",
        "compare_tower_costs(tower_ids, difficulty) - Compare costs",
        "get_upgrade_path(tower_id, path) - Get specific upgrade path",
        "calculate_total_upgrade_cost(tower_id, path, tier, difficulty) - Calculate upgrade costs"
    ]
    
    for tool in tools:
        print(f"   - {tool}")
    
    print(f"\n✨ The BTD6 Tower Stats MCP server provides comprehensive")
    print(f"   tower and hero data for analysis, strategy planning,")
    print(f"   and gameplay optimization!")

if __name__ == "__main__":
    demo_tower_data()