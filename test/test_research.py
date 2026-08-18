import os

from dotenv import load_dotenv

from agents.research import ResearchAgent
from providers.gemini_provider import GeminiProvider
from services.llm_service import LLMService


load_dotenv()

provider = GeminiProvider()

llm_service = LLMService(provider)

research_agent = ResearchAgent(llm_service)

result = research_agent.run(
    "Analyze an AI-powered fitness application for college students."
)

print("\nStartup Idea:")
print(result.startup_idea)

print("\nTarget Customers:")
for customer in result.target_customers:
    print("-", customer)

print("\nProblems:")
for problem in result.problems:
    print("-", problem)

print("\nOpportunities:")
for opportunity in result.opportunities:
    print("-", opportunity)

print("\nRisks:")
for risk in result.risks:
    print("-", risk)