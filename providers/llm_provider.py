from abc import ABC, abstractmethod
from typing import Type, TypeVar

from pydantic import BaseModel


T = TypeVar("T", bound=BaseModel)


class LLMProvider(ABC):

    @abstractmethod
    def generate(
        self,
        system_prompt: str,
        user_prompt: str
    ) -> str:
        pass

    @abstractmethod
    def generate_structured(
        self,
        system_prompt: str,
        user_prompt: str,
        response_model: Type[T]
    ) -> T:
        pass

    @abstractmethod
    async def generate_structured_async(
        self,
        system_prompt: str,
        user_prompt: str,
        response_model: Type[T]
    ) -> T:
        pass