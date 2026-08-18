from models.research import ResearchResult
from services.llm_service import LLMService


class ResearchAgent:

    def __init__(self, llm_service: LLMService):

        self.llm_service = llm_service

        self.system_prompt = """
You are a startup research analyst.

Your job is to analyze a startup idea and identify:

1. What the startup idea is.
2. Who the target customers are.
3. What problems the startup is solving.
4. What opportunities exist in the market.
5. What risks or challenges the startup may face.

Be practical and realistic.

Return the result in the requested structured format.
"""

    def run(self, task: str) -> ResearchResult:

        return self.llm_service.generate_structured(
            system_prompt=self.system_prompt,
            user_prompt=task,
            response_model=ResearchResult
        )

    async def run_async(self, task: str) -> ResearchResult:

        return await self.llm_service.generate_structured_async(
            system_prompt=self.system_prompt,
            user_prompt=task,
            response_model=ResearchResult
        )