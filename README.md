# Bloons MCP Server

This project provides a `FastMCP` server for the Ninja Kiwi Data API, which serves data for games like Bloons TD 6 and Bloons TD Battles 2.

The core of this project is a code generation script that scrapes the official [Ninja Kiwi API documentation](https://data.ninjakiwi.com/) to automatically create:

* A fully typed asynchronous Python client for the API.
* Pydantic models for all API response objects.
* `FastMCP` tool wrappers for every API endpoint.

This ensures the server stays up-to-date with any changes in the official API with minimal manual effort.

## Run the Server

```bash
python fastmcp_server.py
```
