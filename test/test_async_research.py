import asyncio

from dotenv import load_dotenv

from agents.research import ResearchAgent
from providers.gemini_provider import GeminiProvider
from services.llm_service import LLMService


load_dotenv()


async def main():

    provider = GeminiProvider()

    llm_service = LLMService(
        provider=provider
    )

    research_agent = ResearchAgent(
        llm_service=llm_service
    )

    print("Running ResearchAgent asynchronously...")

    result = await research_agent.run_async(
        "Analyze an AI-powered fitness application "
        "designed specifically for college students."
    )

    print("\n===== RESEARCH RESULT =====")

    print("\nStartup Idea:")
    print(result.startup_idea)

    print("\nTarget Customers:")
    for customer in result.target_customers:
        print("-", customer)

    print("\nProblems:")
    for problem in result.problems:
        print("-", problem)


asyncio.run(main())