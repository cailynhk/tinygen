from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from api.github.github import fetch_files_in_repo
from api.gpt.gpt import gpt4_edit_repo
import dotenv
import os
from typing import Optional
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

dotenv.load_dotenv('.env.local')

api_key = os.getenv("OPENAI_API_KEY")
project_id = os.getenv("OPENAI_PROJECT_ID")
github_token = os.getenv("GITHUB_TOKEN")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Target(BaseModel):
    repoUrl: Optional[str] = ""
    prompt: Optional[str] = ""

# give information to github
@app.post("/fetch-repo")
async def fetch_repo(request: Target):
    file_content = fetch_files_in_repo(request.repoUrl, github_token)
    result = gpt4_edit_repo(request.prompt, file_content, os.getenv("OPENAI_API_KEY"), os.getenv("OPENAI_PROJECT_ID"))
    return {"response": result}