import os
from dotenv import load_dotenv
from agent_framework import Agent
from agent_framework.azure import AzureOpenAIChatClient
from tools.search_jobs import search_jobs

load_dotenv()

client = AzureOpenAIChatClient(
    endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
)

INSTRUCTIONS = """
Você é o JobAgent oficial.

REGRAS:
- Sempre use a função search_jobs
- Nunca invente vagas

IMPORTANTE:
- Converta termos específicos em genéricos:
  "Python Developer" → "software engineer"
  "Dev Backend" → "backend developer"

- Para remoto:
  use location = "" ou "remote"

- Se não encontrar vagas:
  tente automaticamente termos mais genéricos

Seja direto e útil.
""".strip()

job_agent = Agent(
    client=client,
    name="JobAgent",
    instructions=INSTRUCTIONS,
    tools=[search_jobs],
)