"""
Reusable MCP Client for AI Startup Analyzer.

This module:
1. Starts the MCP server.
2. Establishes a STDIO connection.
3. Initializes the MCP session.
4. Discovers available MCP tools.
5. Calls MCP tools.
6. Converts MCP results into normal Python data.
"""

import asyncio
import json
import sys
from pathlib import Path
from typing import Any, Dict, Optional

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


# ============================================================
# PATH CONFIGURATION
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

PYTHON_EXECUTABLE = sys.executable

SERVER_FILE = (
    PROJECT_ROOT
    / "mcp_integration"
    / "server.py"
)


# ============================================================
# MCP CLIENT
# ============================================================

class MCPClient:

    def __init__(self):

        self.session: Optional[ClientSession] = None

        self._stdio_context = None
        self._session_context = None

        self.tools = []


    # ========================================================
    # CONNECT
    # ========================================================

    async def connect(self):

        server_params = StdioServerParameters(
            command=PYTHON_EXECUTABLE,
            args=[str(SERVER_FILE)],
            env=None
        )

        self._stdio_context = stdio_client(
            server_params
        )

        read_stream, write_stream = (
            await self._stdio_context.__aenter__()
        )

        self._session_context = ClientSession(
            read_stream,
            write_stream
        )

        self.session = (
            await self._session_context.__aenter__()
        )

        await self.session.initialize()

        tools_result = (
            await self.session.list_tools()
        )

        self.tools = tools_result.tools

        return self.tools


    # ========================================================
    # GET TOOL NAMES
    # ========================================================

    def get_tool_names(self):

        return [
            tool.name
            for tool in self.tools
        ]


    # ========================================================
    # CALL TOOL
    # ========================================================

    async def call_tool(
        self,
        tool_name: str,
        arguments: Dict[str, Any]
    ) -> Any:

        if self.session is None:

            raise RuntimeError(
                "MCP client is not connected. "
                "Call connect() first."
            )

        available_tools = (
            self.get_tool_names()
        )

        if tool_name not in available_tools:

            raise ValueError(
                f"Unknown MCP tool: {tool_name}. "
                f"Available tools: {available_tools}"
            )

        result = await self.session.call_tool(
            tool_name,
            arguments
        )

        return self._parse_result(result)


    # ========================================================
    # RESULT PARSER
    # ========================================================

    @staticmethod
    def _parse_result(result):

        structured_content = getattr(
            result,
            "structuredContent",
            None
        )

        if structured_content is not None:
            return structured_content

        structured_content = getattr(
            result,
            "structured_content",
            None
        )

        if structured_content is not None:
            return structured_content

        content = getattr(
            result,
            "content",
            None
        )

        if not content:
            return None

        parsed_results = []

        for item in content:

            text = getattr(
                item,
                "text",
                None
            )

            if text is None:

                parsed_results.append(item)

                continue

            try:

                parsed_results.append(
                    json.loads(text)
                )

            except (
                json.JSONDecodeError,
                TypeError
            ):

                parsed_results.append(text)

        if len(parsed_results) == 1:

            return parsed_results[0]

        return parsed_results


    # ========================================================
    # DISCONNECT
    # ========================================================

    async def disconnect(self):

        if self._session_context is not None:

            try:

                await self._session_context.__aexit__(
                    None,
                    None,
                    None
                )

            except Exception:
                pass

            self._session_context = None
            self.session = None

        if self._stdio_context is not None:

            try:

                await self._stdio_context.__aexit__(
                    None,
                    None,
                    None
                )

            except Exception:
                pass

            self._stdio_context = None


# ============================================================
# STANDALONE TEST
# ============================================================

async def main():

    print("Starting MCP client...")
    print()

    client = MCPClient()

    try:

        tools = await client.connect()

        print("Connected to MCP server.")
        print("MCP session initialized.")
        print()

        print("Available MCP tools:")

        for tool in tools:

            print(f"- {tool.name}")

            if tool.description:

                print(
                    f"  {tool.description}"
                )

        print()

        print(
            "Calling calculate_market_score..."
        )

        result = await client.call_tool(
            "calculate_market_score",
            {
                "market_size": 80,
                "demand": 90,
                "competition": 40
            }
        )

        print()
        print("Tool result:")

        print(
            json.dumps(
                result,
                indent=2,
                default=str
            )
        )

    finally:

        await client.disconnect()

        print()
        print(
            "MCP client disconnected."
        )


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":

    asyncio.run(main())