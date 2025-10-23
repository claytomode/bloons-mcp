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
A comprehensive server providing detailed BTD6 tower statistics, upgrade paths, and game mechanics data.

**Features:**
- Complete tower database with stats, costs, descriptions
- Detailed upgrade path analysis with costs for all difficulties
- Hero information with abilities and level requirements
- Advanced search and filtering capabilities
- Cost comparison and upgrade calculators

**Files:** 
- `tower_stats_server.py` - Main MCP server
- `scraper.py` - Data generator  
- `btd6_data.json` - Generated tower/hero database
- `README_TOWER_STATS.md` - Detailed documentation

## Code Generation System

The core of the Ninja Kiwi API server is a code generation script that scrapes the official [Ninja Kiwi API documentation](https://data.ninjakiwi.com/) to automatically create:

* A fully typed asynchronous Python client for the API
* Pydantic models for all API response objects
* `FastMCP` tool wrappers for every API endpoint

This ensures the server stays up-to-date with any changes in the official API with minimal manual effort.

## Quick Start

### Ninja Kiwi API Server
```bash
python fastmcp_server.py
```

### BTD6 Tower Stats Server
```bash
# Generate tower data
python scraper.py

# Run the server  
python tower_stats_server.py
```

### Demo the Tower Stats
```bash
python demo_tower_stats.py
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

- **Official Ninja Kiwi API**: Real-time player and event data
- **Tower Stats Database**: Comprehensive game mechanics data derived from community sources and game analysis

Together, these servers provide both official player data and detailed game mechanics information for comprehensive BTD6 analysis and research.
