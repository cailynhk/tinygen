# How to Get TinyGen Running!

Tinygen takes in two inputs via POST request:
- A public Github repo
- A code “prompt,” e.g. “convert it to Typescript”

And returns the diff that accomplishes this task.

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
   http://localhost:800/fetch-repo/

   Place the repo URL and the prompt in the body of the request. 

## Hitting the public URL: 
1. Using Postman, request TingyGen using the following link: https://tinygen-theta.vercel.app/fetch-repo/
2. Place the repo URL and the prompt in the body of the request. 
