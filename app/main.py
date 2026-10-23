"""A minimal LLM gateway: one OpenAI-compatible endpoint routed through LiteLLM."""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI gateway (TrueSource Viewer demo)")


class Prompt(BaseModel):
    model: str = "gpt-4o-mini"
    message: str


@app.post("/v1/complete")
def complete(prompt: Prompt) -> dict:
    # imported here so that the demo can be read without LiteLLM installed
    from litellm import completion

    response = completion(model=prompt.model, messages=[{"role": "user", "content": prompt.message}])
    return {"text": response.choices[0].message.content}
