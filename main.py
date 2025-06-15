# main.py
import os
from dotenv import load_dotenv
from agents import Agent, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import litellm
import rich

# Load environment variables
load_dotenv()

# Disable tracing and aiohttp transport for LiteLLM
set_tracing_disabled(disabled=True)
litellm.disable_aiohttp_transport = True

# Fetch Gemini API key from environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Create agent with LiteLLM + Gemini model
agent = Agent(
    name="my agent",
    instructions="you are a helpful assistant",
    model=LitellmModel(
        model="gemini/gemini-2.0-flash",
        api_key=GEMINI_API_KEY
    )
)

# Run agent synchronously with input
result = Runner.run_sync(agent, "hi")

# Display the final output using rich
rich.print(result.final_output)
