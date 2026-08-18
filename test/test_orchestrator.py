from dotenv import load_dotenv

from agents.competitor import CompetitorAgent
from agents.research import ResearchAgent
from agents.tech_stack import TechStackAgent
from orchestrator.startup_analyzer import StartupAnalyzer
from providers.gemini_provider import GeminiProvider
from services.llm_service import LLMService


load_dotenv()


# --------------------------------------------------
# 1. Create the LLM provider
# --------------------------------------------------

provider = GeminiProvider()


# --------------------------------------------------
# 2. Create the LLM service
# --------------------------------------------------

llm_service = LLMService(provider)


# --------------------------------------------------
# 3. Create the agents
# --------------------------------------------------

research_agent = ResearchAgent(llm_service)

competitor_agent = CompetitorAgent(llm_service)

tech_stack_agent = TechStackAgent(llm_service)


# --------------------------------------------------
# 4. Inject agents into the orchestrator
# --------------------------------------------------

analyzer = StartupAnalyzer(
    research_agent=research_agent,
    competitor_agent=competitor_agent,
    tech_stack_agent=tech_stack_agent,
)


# --------------------------------------------------
# 5. Run the complete workflow
# --------------------------------------------------

result = analyzer.analyze(
    "An AI-powered fitness application designed "
    "specifically for college students."
)


# --------------------------------------------------
# 6. Display the result
# --------------------------------------------------

print("\n========================================")
print("STARTUP ANALYSIS")
print("========================================")


print("\n\n===== RESEARCH =====")

print("\nStartup Idea:")
print(result.research.startup_idea)

print("\nTarget Customers:")
for customer in result.research.target_customers:
    print("-", customer)

print("\nProblems:")
for problem in result.research.problems:
    print("-", problem)

print("\nOpportunities:")
for opportunity in result.research.opportunities:
    print("-", opportunity)

print("\nRisks:")
for risk in result.research.risks:
    print("-", risk)


print("\n\n===== COMPETITOR ANALYSIS =====")

print("\nCompetitors:")

for competitor in result.competitors.competitors:

    print(f"\n{competitor.name}")

    print("Description:")
    print(competitor.description)

    print("Strengths:")
    for strength in competitor.strengths:
        print("-", strength)

    print("Weaknesses:")
    for weakness in competitor.weaknesses:
        print("-", weakness)


print("\nCompetitive Advantages:")

for advantage in result.competitors.competitive_advantages:
    print("-", advantage)


print("\nMarket Gaps:")

for gap in result.competitors.market_gaps:
    print("-", gap)


print("\n\n===== TECHNOLOGY STACK =====")

print("\nFrontend:")
for technology in result.tech_stack.frontend:
    print("-", technology)

print("\nBackend:")
for technology in result.tech_stack.backend:
    print("-", technology)

print("\nDatabase:")
for technology in result.tech_stack.database:
    print("-", technology)

print("\nAI/ML:")
for technology in result.tech_stack.ai_ml:
    print("-", technology)

print("\nInfrastructure:")
for technology in result.tech_stack.infrastructure:
    print("-", technology)

print("\nExternal APIs:")
for api in result.tech_stack.external_apis:
    print("-", api)

print("\nReasoning:")
print(result.tech_stack.reasoning)