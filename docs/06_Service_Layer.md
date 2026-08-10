# Service Layer

## What is a Service?

A service contains reusable functionality that can be shared across multiple parts of the application.

## Why do we need it?

To avoid duplicating code.

To keep agents focused on business logic.

To make changing external providers easier.

## Example

Research Agent
      ↓
LLM Service
      ↓
OpenAI

## Benefits

- Reusable
- Maintainable
- Easy to test
- Easy to replace