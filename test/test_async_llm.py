import asyncio

from dotenv import load_dotenv

from providers.gemini_provider import GeminiProvider
from models.research import ResearchResult


load_dotenv()


async def main():

    provider = GeminiProvider()

    print("Sending asynchronous request to Gemini...")

    result = await provider.generate_structured_async(
        system_prompt=(
            "You are a startup research analyst. "
            "Return structured information about the startup idea."
        ),
        user_prompt=(
            "Analyze an AI-powered fitness application "
            "for college students."
        ),
        response_model=ResearchResult
    )

    print("\n===== ASYNC RESULT =====")

    print("\nStartup Idea:")
    print(result.startup_idea)

    print("\nTarget Customers:")
    for customer in result.target_customers:
        print("-", customer)

    print("\nProblems:")
    for problem in result.problems:
        print("-", problem)


asyncio.run(main())