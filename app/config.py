import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    # API Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    XAI_API_KEY = os.getenv("XAI_API_KEY")

    # LLM Configuration
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")  # or "xai"
    LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4")  # Default model

    # Database Configuration
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///verbal_trainer.db")

    # Application Configuration
    DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "t")
    PORT = int(os.getenv("PORT", "8000"))
