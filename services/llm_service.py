from typing import Type, TypeVar

from pydantic import BaseModel

from providers.llm_provider import LLMProvider


T = TypeVar("T", bound=BaseModel)


class LLMService:

    def __init__(self, provider: LLMProvider):
        self.provider = provider

    def generate(
        self,
        system_prompt: str,
        user_prompt: str
    ) -> str:

        return self.provider.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt
        )

    def generate_structured(
        self,
        system_prompt: str,
        user_prompt: str,
        response_model: Type[T]
    ) -> T:

        return self.provider.generate_structured(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            response_model=response_model
        )

    async def generate_structured_async(
        self,
        system_prompt: str,
        user_prompt: str,
        response_model: Type[T]
    ) -> T:

        return await self.provider.generate_structured_async(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            response_model=response_model
        )