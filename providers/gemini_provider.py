import asyncio
import os
from typing import Type, TypeVar

from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel

from providers.llm_provider import LLMProvider


load_dotenv()


T = TypeVar("T", bound=BaseModel)


class GeminiProvider(LLMProvider):

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is not set in the environment."
            )

        self.client = genai.Client(
            api_key=api_key
        )

        # ----------------------------------------------------
        # MODEL CONFIGURATION
        # ----------------------------------------------------

        self.model = os.getenv(
            "GEMINI_MODEL",
            "gemini-2.5-flash"
        )

        self.timeout = int(
            os.getenv(
                "GEMINI_TIMEOUT",
                "60"
            )
        )

        # ----------------------------------------------------
        # RETRY CONFIGURATION
        # ----------------------------------------------------

        # We deliberately keep retries low.
        #
        # IMPORTANT:
        # 429 quota errors should NOT be retried repeatedly.
        # They indicate that the API quota/rate limit has been
        # reached and retrying immediately only wastes time.
        self.max_retries = 1

        self.base_delay = 2

    # ========================================================
    # ERROR CLASSIFICATION
    # ========================================================

    def _is_quota_error(
        self,
        error: Exception
    ) -> bool:

        error_message = str(error).lower()

        quota_terms = [
            "429",
            "resource_exhausted",
            "quota exceeded",
            "generate_content_free_tier_requests",
            "rate limit"
        ]

        return any(
            term in error_message
            for term in quota_terms
        )

    def _is_retryable_error(
        self,
        error: Exception
    ) -> bool:

        error_message = str(error).lower()

        retryable_terms = [
            "500",
            "502",
            "503",
            "504",
            "temporarily unavailable",
            "internal error",
            "server error",
            "deadline exceeded",
            "connection reset",
            "connection error"
        ]

        return any(
            term in error_message
            for term in retryable_terms
        )

    # ========================================================
    # RETRY WAIT
    # ========================================================

    async def _wait_before_retry(
        self,
        attempt: int
    ):

        delay = self.base_delay * (
            2 ** attempt
        )

        print(
            f"Gemini request failed temporarily. "
            f"Retrying in {delay} second(s)..."
        )

        await asyncio.sleep(delay)

    # ========================================================
    # ASYNC STRUCTURED REQUEST
    # ========================================================

    async def _generate_structured_request(
        self,
        system_prompt: str,
        user_prompt: str,
        response_model: Type[T]
    ) -> T:

        response = await asyncio.wait_for(
            self.client.aio.models.generate_content(
                model=self.model,
                contents=user_prompt,
                config={
                    "system_instruction": system_prompt,
                    "response_mime_type": "application/json",
                    "response_schema": response_model
                }
            ),
            timeout=self.timeout
        )

        if not response.text:
            raise ValueError(
                "Gemini returned an empty response."
            )

        return response_model.model_validate_json(
            response.text
        )

    # ========================================================
    # SYNCHRONOUS GENERATION
    # ========================================================

    def generate(
        self,
        system_prompt: str,
        user_prompt: str
    ) -> str:

        response = self.client.models.generate_content(
            model=self.model,
            contents=user_prompt,
            config={
                "system_instruction": system_prompt
            }
        )

        if not response.text:
            raise ValueError(
                "Gemini returned an empty response."
            )

        return response.text

    # ========================================================
    # SYNCHRONOUS STRUCTURED GENERATION
    # ========================================================

    def generate_structured(
        self,
        system_prompt: str,
        user_prompt: str,
        response_model: Type[T]
    ) -> T:

        response = self.client.models.generate_content(
            model=self.model,
            contents=user_prompt,
            config={
                "system_instruction": system_prompt,
                "response_mime_type": "application/json",
                "response_schema": response_model
            }
        )

        if not response.text:
            raise ValueError(
                "Gemini returned an empty response."
            )

        return response_model.model_validate_json(
            response.text
        )

    # ========================================================
    # ASYNC STRUCTURED GENERATION
    # ========================================================

    async def generate_structured_async(
        self,
        system_prompt: str,
        user_prompt: str,
        response_model: Type[T]
    ) -> T:

        for attempt in range(
            self.max_retries + 1
        ):

            try:

                print(
                    f"Calling Gemini "
                    f"({self.model}) "
                    f"attempt {attempt + 1}/"
                    f"{self.max_retries + 1}..."
                )

                return await self._generate_structured_request(
                    system_prompt=system_prompt,
                    user_prompt=user_prompt,
                    response_model=response_model
                )

            # ------------------------------------------------
            # TIMEOUT
            # ------------------------------------------------

            except asyncio.TimeoutError:

                print(
                    f"Gemini request timed out "
                    f"after {self.timeout} seconds."
                )

                if attempt >= self.max_retries:
                    raise

                await self._wait_before_retry(
                    attempt
                )

            # ------------------------------------------------
            # OTHER ERRORS
            # ------------------------------------------------

            except Exception as error:

                print(
                    f"Gemini request failed: "
                    f"{type(error).__name__}: {error}"
                )

                # --------------------------------------------
                # DO NOT RETRY QUOTA ERRORS
                # --------------------------------------------

                if self._is_quota_error(error):

                    print(
                        "\nGemini API quota/rate limit reached."
                    )

                    print(
                        "The request will not be retried."
                    )

                    raise

                # --------------------------------------------
                # RETRY TEMPORARY SERVER ERRORS
                # --------------------------------------------

                if (
                    self._is_retryable_error(error)
                    and attempt < self.max_retries
                ):

                    await self._wait_before_retry(
                        attempt
                    )

                    continue

                # --------------------------------------------
                # NON-RETRYABLE ERROR
                # --------------------------------------------

                raise

        raise RuntimeError(
            "Gemini request failed after all retry attempts."
        )