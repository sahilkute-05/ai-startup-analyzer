from models.tech_stack import TechStackResult
from services.llm_service import LLMService


class TechStackAgent:

    def __init__(self, llm_service: LLMService):

        self.llm_service = llm_service

        self.system_prompt = """
You are a senior software architect.

Your job is to recommend an appropriate technology stack
for a startup idea.

Analyze:

1. Frontend technologies.
2. Backend technologies.
3. Database.
4. AI/ML technologies when required.
5. APIs and integrations.
6. Infrastructure and deployment.
7. Important technical considerations.

Recommendations should be practical for an early-stage startup.

Return the result in the requested structured format.
"""

    def run(self, task: str) -> TechStackResult:

        return self.llm_service.generate_structured(
            system_prompt=self.system_prompt,
            user_prompt=task,
            response_model=TechStackResult
        )

    async def run_async(self, task: str) -> TechStackResult:

        return await self.llm_service.generate_structured_async(
            system_prompt=self.system_prompt,
            user_prompt=task,
            response_model=TechStackResult
        )