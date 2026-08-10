class LLMService:
    """
    Handles communication with the LLM.

    For now, this is a mock implementation.
    """

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        return f"""
        MOCK RESPONSE

        System Prompt:
        {system_prompt}

        User Prompt:
        {user_prompt}
        """