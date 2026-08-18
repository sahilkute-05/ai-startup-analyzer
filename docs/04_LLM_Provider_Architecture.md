# LLM Provider Architecture

## Problem

Agents should not depend directly on a specific LLM provider.

If ResearchAgent directly used Gemini, switching to OpenAI or Ollama would require modifying the agent.

## Solution

Introduce an LLMProvider abstraction.

ResearchAgent
↓
LLMService
↓
LLMProvider
↓
Concrete Provider

## Current Provider

GeminiProvider

## Future Providers

- OpenAIProvider
- OllamaProvider

## Concepts Learned

- Abstraction
- Abstract Base Classes
- Interfaces
- Polymorphism
- Dependency Injection
- Separation of Concerns