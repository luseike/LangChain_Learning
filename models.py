import os
from pathlib import Path

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI

PROJECT_ROOT = Path(__file__).resolve().parent
load_dotenv(PROJECT_ROOT / ".env")
load_dotenv(PROJECT_ROOT / ".env.local", override=True)

openai_model = ChatOpenAI(
    model=os.getenv("LLM_MODEL"),
    api_key=os.getenv("GITHUB_TOKEN", "").strip(),
    base_url=os.getenv("DEFAULT_GITHUB_MODELS_BASE_URL"),
)

qwen = ChatOpenAI(
    model=os.getenv("QWEN_MODEL"),
    api_key=os.getenv("QWEN_API_KEY"),
    base_url=os.getenv("QWEN_API_URL"),
)

ds = ChatOpenAI(
    model=os.getenv("DEEPSEEKER_MODEL"),
    api_key=os.getenv("DEEPSEEKER_API_KEY"),
    base_url=os.getenv("DEEPSEEKER_API_URL"),
)
