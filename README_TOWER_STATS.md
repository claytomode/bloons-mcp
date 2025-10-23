# BTD6 Tower Stats MCP Server

This directory contains a comprehensive MCP (Model Context Protocol) server for Bloons Tower Defense 6 (BTD6) tower statistics, upgrade paths, and detailed information.

## Features

- **Complete Tower Database**: Stats, costs, descriptions for all BTD6 towers
- **Upgrade Path Analysis**: Detailed upgrade information with costs for all difficulties  
- **Hero Information**: Complete hero data with abilities and level requirements
- **Advanced Search**: Search towers by name, description, or upgrade information
- **Cost Comparison**: Compare tower costs across different game difficulties
- **Upgrade Cost Calculator**: Calculate total costs for specific upgrade paths

## Files

- `tower_stats_server.py` - Main MCP server with all tower stats functionality
- `scraper.py` - Data generator for creating comprehensive tower database
- `btd6_data.json` - Generated tower and hero data in JSON format
- `test_tower_server.py` - Test suite for validating server functionality

## Installation

1. Ensure you have Python 3.12+ installed
2. Install required dependencies:
   ```bash
   pip install pydantic fastmcp httpx lxml
   ```

3. Generate the tower data:
   ```bash
   python scraper.py
   ```

4. Run the server:
   ```bash
   python tower_stats_server.py
   ```

## Usage

The server provides the following MCP tools:

### Tower Information
- `get_tower_info(tower_id)` - Get detailed info about a specific tower
- `list_all_towers(category?)` - List all towers, optionally by category
- `search_towers(query)` - Search for towers by name/description

### Hero Information  
- `get_hero_info(hero_id)` - Get detailed info about a specific hero
- `list_all_heroes()` - List all available heroes

### Analysis Tools
- `compare_tower_costs(tower_ids, difficulty)` - Compare costs across towers
- `get_upgrade_path(tower_id, path)` - Get upgrades for specific path
- `calculate_total_upgrade_cost(tower_id, path, tier, difficulty)` - Calculate total upgrade costs

### Example Tower IDs
- `dart_monkey` - Dart Monkey
- `boomerang_monkey` - Boomerang Monkey  
- `sniper_monkey` - Sniper Monkey
- `wizard_monkey` - Wizard Monkey
- `super_monkey` - Super Monkey
- `banana_farm` - Banana Farm

### Example Hero IDs
- `quincy` - Quincy
- `gwendolin` - Gwendolin
- `striker_jones` - Striker Jones

## Data Structure

The server uses comprehensive Pydantic models for type safety:

- **Tower**: Complete tower info with stats, costs, upgrades
- **TowerStats**: Base statistics (damage, pierce, range, etc.)
- **TowerUpgrade**: Individual upgrade with costs and descriptions
- **Hero**: Hero info with abilities and level requirements

## Extending the Data

To add more towers or update existing data:

1. Modify the data generation in `scraper.py`
2. Regenerate data: `python scraper.py`
3. Restart the server

The scraper is designed to be extensible - you can add real web scraping functionality to pull data from BTD6 wikis or community sites.

## Integration

This MCP server complements the existing Ninja Kiwi API MCP by providing detailed game mechanics data not available through the official API. Together they provide:

- **Official API**: Player stats, race data, boss events
- **Tower Stats MCP**: Game mechanics, tower stats, upgrade paths

## Development

The codebase is structured for easy extension:

- Modular data loading system
- Comprehensive Pydantic models
- Extensible search functionality  
- Clean separation between data and API layers

## Note on Data Sources

The current implementation includes comprehensive sample data based on BTD6 game mechanics. In a production environment, you could extend the scraper to pull real-time data from:

- BTD6 Central (https://btd6central.com)
- Bloons Wiki (https://bloons.fandom.com)
- Community APIs and databases

This ensures the MCP server provides accurate, up-to-date information for BTD6 analysis and gameplay optimization.