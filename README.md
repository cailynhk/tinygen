# How to Get TinyGen Running!
Via POST request, TinyGen takes in:
- A public Github repo
- A code “prompt,” e.g. “convert it to Typescript”

And returns the diff that accomplishes this task.

## Hitting the public URL: 
1. Using Postman, request TinyGen using the following link: https://tinygen-theta.vercel.app/fetch-repo/
2. Place the repo URL and the prompt in the body of the request. Here's a sample of the request body:
```
{
    "repoUrl": "https://github.com/jayhack/llm.sh",
    "prompt": " The program doesn't output anything in windows 10 (base) C:\\Users\\off99\\Documents\\Code\\>llm list files in current dir; windows / Querying GPT-3200 ───────┬──────────────────────────────────────────────────────────────────────────────────────────────────────────────── File: temp.sh ───────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────  1   │   2   │ dir   3   │ ───────┴────────────────────────────────────────────────────────────────────────────────────────────────────────────────>> Do you want to run this program? [Y/n] yRunning...(base) C:\\Users\\off99\\Documents\\Code\\>Notice that there is no output. Is this supposed to work on Windows also?Also it might be great if the script detects which OS or shell I'm using and try to use the appropriate command e.g. dir instead of ls because I don't want to be adding windows after every prompt."
}
```

## TinyGen's Tech Stack 
- OpenAI's GPT-4o as LLM
- Github API to access public repos
- Langchain as a RAG to store information across all responses and prompts
- Used uvicorn to run the app
- Deployed on Vercel, increased maximum duration of loading to up to 30 seconds
 
## Running TinyGen locally: 
1. Please install all requirements listed in `requirements.txt`

2. Setup environment variables in a `.env` file, or request me for environment variables :)

3. Running server

   Please make sure your current directory is tinygen\api, otherwise:
   
   `cd api`
   
   in the terminal.

   After, run the following in the terminal: 
   `python main.py`

5. Using Postman, request TinyGen using the following link:
   http://localhost:8000/fetch-repo/

   Place the repo URL and the prompt in the body of the request. 
