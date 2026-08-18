from dotenv import load_dotenv

from agents.competitor import CompetitorAgent
from agents.research import ResearchAgent
from providers.gemini_provider import GeminiProvider
from services.llm_service import LLMService


load_dotenv()

provider = GeminiProvider()

llm_service = LLMService(provider)

research_agent = ResearchAgent(llm_service)

competitor_agent = CompetitorAgent(llm_service)


research_result = research_agent.run(
    "Analyze an AI-powered fitness application designed specifically "
    "for college students."
)


competitor_result = competitor_agent.run(
    research_result
)


print("\n===== RESEARCH RESULT =====")

print("\nStartup Idea:")
print(research_result.startup_idea)

print("\nTarget Customers:")
for customer in research_result.target_customers:
    print("-", customer)


print("\n===== COMPETITOR ANALYSIS =====")

print("\nCompetitors:")

for competitor in competitor_result.competitors:

    print(f"\nName: {competitor.name}")

    print(f"Description: {competitor.description}")

    print("Strengths:")
    for strength in competitor.strengths:
        print("-", strength)

    print("Weaknesses:")
    for weakness in competitor.weaknesses:
        print("-", weakness)


print("\nCompetitive Advantages:")

for advantage in competitor_result.competitive_advantages:
    print("-", advantage)


print("\nMarket Gaps:")

for gap in competitor_result.market_gaps:
    print("-", gap)