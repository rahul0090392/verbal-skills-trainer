import asyncio
import os

import openai


class LLMClient:
    def __init__(self):
        self.provider = os.getenv("LLM_PROVIDER", "openai")
        self.api_key = (
            os.getenv("OPENAI_API_KEY")
            if self.provider == "openai"
            else os.getenv("XAI_API_KEY")
        )
        self.model = os.getenv("LLM_MODEL", "gpt-4")

        if not self.api_key:
            raise ValueError(f"{self.provider.upper()} API key is not set")

        if self.provider == "openai":
            self.client = openai.AsyncOpenAI(api_key=self.api_key)
        elif self.provider == "xai":
            # Placeholder for xAI client setup
            self.client = None

    async def get_completion(self, prompt, system_message=None, retries=3):
        messages = (
            [{"role": "system", "content": system_message}] if system_message else []
        )
        messages.append({"role": "user", "content": prompt})

        for attempt in range(retries):
            try:
                if self.provider == "openai":
                    response = await self.client.chat.completions.create(
                        model=self.model, messages=messages, temperature=0.7
                    )
                    return response.choices[0].message.content
                elif self.provider == "xai":
                    return "xAI integration pending"  # Placeholder response
            except openai.RateLimitError:
                if attempt < retries - 1:
                    await asyncio.sleep(2**attempt)  # Exponential backoff
                else:
                    return "I'm experiencing high demand. Please try again later."
            except Exception as e:
                return f"Error: {str(e)}"
