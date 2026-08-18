import asyncio

from services.llm_service import LLMService

from providers.gemini_provider import GeminiProvider

from agents.research import ResearchAgent
from agents.competitor import CompetitorAgent
from agents.tech_stack import TechStackAgent
from agents.synthesis import SynthesisAgent

from orchestrator.startup_analyzer import StartupAnalyzer


async def main():

    print("Starting asynchronous startup analysis...\n")

    # ---------------------------------------------------------
    # 1. Create the Gemini provider
    # ---------------------------------------------------------

    provider = GeminiProvider()

    # ---------------------------------------------------------
    # 2. Create the LLM service
    # ---------------------------------------------------------

    llm_service = LLMService(
        provider=provider
    )

    # ---------------------------------------------------------
    # 3. Create all agents
    # ---------------------------------------------------------

    research_agent = ResearchAgent(
        llm_service=llm_service
    )

    competitor_agent = CompetitorAgent(
        llm_service=llm_service
    )

    tech_stack_agent = TechStackAgent(
        llm_service=llm_service
    )

    synthesis_agent = SynthesisAgent(
        llm_service=llm_service
    )

    # ---------------------------------------------------------
    # 4. Create the Startup Analyzer
    # ---------------------------------------------------------

    analyzer = StartupAnalyzer(
        research_agent=research_agent,
        competitor_agent=competitor_agent,
        tech_stack_agent=tech_stack_agent,
        synthesis_agent=synthesis_agent
    )

    # ---------------------------------------------------------
    # 5. Startup idea to analyze
    # ---------------------------------------------------------

    startup_idea = (
        "An AI-powered fitness application designed "
        "specifically for college students."
    )

    # ---------------------------------------------------------
    # 6. Run the complete analysis
    # ---------------------------------------------------------

    result = await analyzer.analyze_async(
        startup_idea
    )

    # ---------------------------------------------------------
    # 7. Display results
    # ---------------------------------------------------------

    print("\n")
    print("=" * 30)
    print("FINAL STARTUP ANALYSIS")
    print("=" * 30)

    print("\n--- RESEARCH ---")
    print(result.research)

    print("\n--- COMPETITORS ---")
    print(result.competitors)

    print("\n--- TECH STACK ---")
    print(result.tech_stack)

    print("\n--- SYNTHESIS ---")
    print(result.synthesis)

    print("\n")
    print("=" * 30)
    print("ANALYSIS COMPLETE")
    print("=" * 30)


if __name__ == "__main__":

    asyncio.run(main())