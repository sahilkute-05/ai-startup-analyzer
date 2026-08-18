import asyncio

from agents.research import ResearchAgent
from agents.competitor import CompetitorAgent
from agents.tech_stack import TechStackAgent
from agents.synthesis import SynthesisAgent

from models.startup_analysis import StartupAnalysis

from mcp_integration.mcp_client import MCPClient


class StartupAnalyzer:

    def __init__(
        self,
        research_agent: ResearchAgent,
        competitor_agent: CompetitorAgent,
        tech_stack_agent: TechStackAgent,
        synthesis_agent: SynthesisAgent,
        mcp_client: MCPClient | None = None
    ):

        self.research_agent = research_agent
        self.competitor_agent = competitor_agent
        self.tech_stack_agent = tech_stack_agent
        self.synthesis_agent = synthesis_agent

        self.mcp_client = mcp_client


    async def analyze_async(
        self,
        startup_idea: str
    ) -> StartupAnalysis:

        print("\nStarting startup analysis...\n")

        # ====================================================
        # MCP CONNECTION
        # ====================================================

        if self.mcp_client is not None:

            print("Connecting to MCP server...")

            await self.mcp_client.connect()

            print("MCP server connected.")

            print(
                "Available MCP tools:",
                self.mcp_client.get_tool_names()
            )


        # ====================================================
        # RESEARCH + COMPETITOR
        # ====================================================

        print(
            "\nRunning Research and Competitor agents "
            "in parallel..."
        )

        research_result, competitor_result = (
            await asyncio.gather(

                self.research_agent.run_async(
                    startup_idea
                ),

                self.competitor_agent.run_async(
                    startup_idea
                )
            )
        )

        print(
            "Research and Competitor analysis completed."
        )

        research_context = (
            research_result.model_dump_json(
                indent=2
            )
        )

        competitor_context = (
            competitor_result.model_dump_json(
                indent=2
            )
        )


        # ====================================================
        # MCP MARKET ANALYSIS
        # ====================================================

        if self.mcp_client is not None:

            print(
                "\nRunning MCP market analysis..."
            )

            try:

                market_result = (
                    await self.mcp_client.call_tool(
                        "analyze_market",
                        {
                            "market_size": 80,
                            "demand": 90,
                            "competition": 40,
                            "growth_potential": 85
                        }
                    )
                )

                print(
                    "MCP market analysis completed."
                )

            except Exception as e:

                print(
                    f"MCP market analysis failed: {e}"
                )

                market_result = {
                    "status": "error",
                    "message": str(e)
                }

        else:

            market_result = {
                "status": "not_available"
            }


        # ====================================================
        # COMBINED CONTEXT
        # ====================================================

        combined_context = f"""
RESEARCH ANALYSIS:

{research_context}


COMPETITOR ANALYSIS:

{competitor_context}


MCP MARKET ANALYSIS:

{market_result}
"""


        # ====================================================
        # TECH STACK
        # ====================================================

        print(
            "\nRunning Tech Stack Agent..."
        )

        tech_stack_result = (
            await self.tech_stack_agent.run_async(
                combined_context
            )
        )

        print(
            "Tech Stack analysis completed."
        )


        # ====================================================
        # SYNTHESIS
        # ====================================================

        full_context = f"""
RESEARCH ANALYSIS:

{research_context}


COMPETITOR ANALYSIS:

{competitor_context}


MCP MARKET ANALYSIS:

{market_result}


TECH STACK ANALYSIS:

{tech_stack_result.model_dump_json(indent=2)}
"""

        print(
            "\nRunning Synthesis Agent..."
        )

        synthesis_result = (
            await self.synthesis_agent.run_async(
                full_context
            )
        )

        print(
            "Synthesis analysis completed."
        )


        # ====================================================
        # MCP DISCONNECT
        # ====================================================

        if self.mcp_client is not None:

            await self.mcp_client.disconnect()

            print(
                "MCP server disconnected."
            )


        # ====================================================
        # FINAL RESULT
        # ====================================================

        return StartupAnalysis(
            research=research_result,
            competitors=competitor_result,
            tech_stack=tech_stack_result,
            synthesis=synthesis_result
        )


    def analyze(
        self,
        startup_idea: str
    ) -> StartupAnalysis:

        return asyncio.run(
            self.analyze_async(
                startup_idea
            )
        )