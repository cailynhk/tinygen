from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from api.github.github import fetch_files_in_repo
import dotenv
import os
from typing import Optional
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

dotenv.load_dotenv('.env.local')

github_token = os.getenv("GITHUB_TOKEN")

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
    return {"response": result}