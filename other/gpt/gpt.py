import openai
from langchain.memory import ConversationBufferMemory
from langsmith.wrappers import wrap_openai
from langsmith import traceable

shared_memory = ConversationBufferMemory()

def gpt4_edit_repo(prompt, selected_files, api_key, project_id): 
    # Second step: editing specific files only (using smaller batches if needed)
    shared_memory.clear()
    openai.api_key = api_key
    openai.project_id = project_id
    client = wrap_openai(openai.Client())
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": f"You are an expert code assistant. Given these files: {selected_files}, edit them and OUTPUT A DIFF/PATCH string about your edits."},
            {"role": "user", "content": f"{prompt}"},
            {"role": "system", "content": "Reflect on your edits and return only the DIFF/PATCH string, including the patch header. So the beginning should always be diff --git a/path/to/file b/path/to/file\n index <sha...sha> <mode>\n <bla bla bla>"},
        ]
    )
    patch_str = response.choices[0].message.content
    result = patch_str.split("diff\n", 1)[1] # Remove the first diff header
    return result