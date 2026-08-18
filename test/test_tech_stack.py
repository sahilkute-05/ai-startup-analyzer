from dotenv import load_dotenv

from agents.competitor import CompetitorAgent
from agents.research import ResearchAgent
from agents.tech_stack import TechStackAgent
from providers.gemini_provider import GeminiProvider
from services.llm_service import LLMService


load_dotenv()


provider = GeminiProvider()

llm_service = LLMService(provider)


research_agent = ResearchAgent(llm_service)

competitor_agent = CompetitorAgent(llm_service)

tech_stack_agent = TechStackAgent(llm_service)


research_result = research_agent.run(
    "An AI-powered fitness application designed specifically "
    "for college students."
)


competitor_result = competitor_agent.run(
    research_result
)


tech_stack_result = tech_stack_agent.run(
    research=research_result,
    competitors=competitor_result
)


print("\n===== TECHNOLOGY STACK =====")


print("\nFrontend:")
for technology in tech_stack_result.frontend:
    print("-", technology)


print("\nBackend:")
for technology in tech_stack_result.backend:
    print("-", technology)


print("\nDatabase:")
for technology in tech_stack_result.database:
    print("-", technology)


print("\nAI/ML:")
for technology in tech_stack_result.ai_ml:
    print("-", technology)


print("\nInfrastructure:")
for technology in tech_stack_result.infrastructure:
    print("-", technology)


print("\nExternal APIs:")
for api in tech_stack_result.external_apis:
    print("-", api)


print("\nReasoning:")
print(tech_stack_result.reasoning)