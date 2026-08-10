from agents.research import ResearchAgent
from services.llm_service import LLMService


llm_service = LLMService()

research_agent = ResearchAgent(llm_service)

result = research_agent.run(
    "Analyze an AI-powered fitness application for college students."
)

print(result)