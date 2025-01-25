import json
from ecologits import EcoLogits
from huggingface_hub import InferenceClient
import os
import regex
#import google.generativeai as genai
cwd = os.getcwd()

cred_dir = cwd + '/'
gemini_access_key_dir = cred_dir + 'gemini_key.txt'
f = open(gemini_access_key_dir, 'r')
gemini_access_key = f.read()

# Initialize EcoLogits

def lambda_handler(event, context):
    EcoLogits.init()
    # Ask something to Google Gemini
    #genai.configure(api_key=gemini_access_key)
    #model = genai.GenerativeModel("gemini-1.5-flash")
    #response = model.generate_content("Write a story about a magic backpack.")

    client = InferenceClient(model="HuggingFaceH4/zephyr-7b-beta")
    response = client.chat_completion(
    messages=[{"role": "user", "content": "Tell me a funny joke!"}],
    max_tokens=15
)

# Get estimated environmental impacts of the inference
    print(response.impacts)

