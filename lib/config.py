import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv(".env"))

class Config:
    openAiApiKey = os.environ["OPENAI_API_KEY"]