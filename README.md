# Bloons MCP Servers

This project provides multiple MCP (Model Context Protocol) servers for Bloons Tower Defense games, offering comprehensive data access and analysis capabilities.

## Servers Included

### 1. Ninja Kiwi API MCP Server
The original server that provides a `FastMCP` interface for the official Ninja Kiwi Data API, serving data for games like Bloons TD 6 and Bloons TD Battles 2.

**Features:**
- Fully typed asynchronous Python client for the API
- Pydantic models for all API response objects  
- `FastMCP` tool wrappers for every API endpoint
- Player statistics, race data, boss events

**File:** `fastmcp_server.py`

### 2. BTD6 Tower Stats MCP Server
A comprehensive server providing detailed BTD6 tower statistics, upgrade paths, and game mechanics data scraped from community sources.

**Features:**
- Web scraping from BTD6 Wiki and community sources
- Jinja2 template-based code generation (following same pattern as main server)
- Complete tower database with stats, costs, descriptions
- Hero information with abilities and progression data
- Advanced search and filtering capabilities
- Cost comparison and upgrade calculators

**Files:** 
- `scraper.py` - Web scraper and template-based generator
- `btd6_codegen/templates/btd6_server.py.j2` - Jinja2 template for server generation
- `btd6_tower_stats_server.py` - Generated MCP server (auto-generated, do not edit)

## Code Generation System

Both servers use code generation with web scraping and Jinja2 templates:

### Ninja Kiwi API Server
Scrapes the official [Ninja Kiwi API documentation](https://data.ninjakiwi.com/) to automatically generate:
* A fully typed asynchronous Python client for the API
* Pydantic models for all API response objects
* `FastMCP` tool wrappers for every API endpoint

### BTD6 Tower Stats Server  
Scrapes community sources (BTD6 Wiki, etc.) to automatically generate:
* Comprehensive tower and hero data models
* Complete BTD6 tower stats MCP server
* Type-safe Pydantic models for all game data
* Advanced search and analysis tools

This ensures both servers stay up-to-date with changes in their respective data sources with minimal manual effort.

## Quick Start

### Ninja Kiwi API Server
```bash
python fastmcp_server.py
```

### BTD6 Tower Stats Server
```bash
# Generate the server from web-scraped data
python scraper.py

# Run the generated server  
python btd6_tower_stats_server.py
```

## Installation

1. Ensure you have Python 3.12+ installed
2. Install dependencies:
   ```bash
   pip install pydantic fastmcp httpx lxml jinja2
   ```

## Use Cases

**Ninja Kiwi API Server:**
- Player profile analysis
- Race leaderboard tracking  
- Boss event monitoring
- Game statistics research

**BTD6 Tower Stats Server:**
- Strategy planning and optimization
- Tower cost analysis across difficulties
- Upgrade path comparison
- Game mechanics research

## Data Sources

- **Official Ninja Kiwi API**: Real-time player and event data via web scraping + generation
- **BTD6 Community Sources**: Tower stats from BTD6 Wiki and community databases via web scraping + generation

Together, these servers provide both official player data and detailed game mechanics information for comprehensive BTD6 analysis and research.

## Development

Both servers follow the same pattern:
1. **Web Scraping**: Automated data collection from external sources
2. **Jinja2 Templates**: Type-safe code generation using templates
3. **Generated Servers**: Complete MCP servers with all tools and models
4. **Automatic Updates**: Re-run generators to update with latest data

This architecture ensures maintainability and keeps data current with external sources.
