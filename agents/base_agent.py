class BaseAgent:
    """
    Base class for all AI Agents.
    Every future agent will inherit from this class.
    """

    def __init__(self, name: str, role: str, system_prompt: str):
        self.name = name
        self.role = role
        self.system_prompt = system_prompt

    def run(self, task: str):
        raise NotImplementedError(
            "Each agent must implement its own run() method."
        )