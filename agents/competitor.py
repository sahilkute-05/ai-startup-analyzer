from models.competitor import CompetitorResult
from services.llm_service import LLMService


class CompetitorAgent:

    def __init__(self, llm_service: LLMService):

        self.llm_service = llm_service

        self.system_prompt = """
You are a startup competitor analysis expert.

Your job is to analyze a startup idea and identify:

1. Existing or potential competitors.
2. What those competitors offer.
3. Their strengths.
4. Their weaknesses.
5. How the proposed startup could differentiate itself.

Be realistic and avoid inventing overly specific facts.

Return the result in the requested structured format.
"""

    def run(self, task: str) -> CompetitorResult:

        return self.llm_service.generate_structured(
            system_prompt=self.system_prompt,
            user_prompt=task,
            response_model=CompetitorResult
        )

    async def run_async(self, task: str) -> CompetitorResult:

        return await self.llm_service.generate_structured_async(
            system_prompt=self.system_prompt,
            user_prompt=task,
            response_model=CompetitorResult
        )