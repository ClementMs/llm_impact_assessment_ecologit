import json
import ecologits
from ecologits import EcoLogits
import os
from openai import OpenAI
from anthropic import Anthropic
#from langchain_openai.chat_models import ChatOpenAI

cwd = os.getcwd()

cred_dir = cwd + '/'
openai_access_key_dir = cred_dir + 'openai_key.txt'
f = open(openai_access_key_dir, 'r')
openai_access_key = f.read()
claude_access_key_dir = cred_dir + 'claude_key.txt'
f = open(claude_access_key_dir, 'r')
claude_access_key = f.read()


def lambda_handler(event, context):
    EcoLogits.init()


    client = Anthropic(api_key=claude_access_key)

    

    claude_response = client.messages.create(
    max_tokens=100,
    messages=[{"role": "user", "content": "Tell me a funny joke!"}],
    model="claude-3-haiku-20240307",
)

    #print(claude_access_key)

    #print(claude_response)


    # Get estimated environmental impacts of the inference
    print("Claude 3 Haiku's energy consumption: ")
    print(f"Energy consumption: {claude_response.impacts.energy.value} kWh")
    print(f"GHG emissions: {claude_response.impacts.gwp.value} kgCO2eq")



    client = OpenAI(api_key=openai_access_key)
    openai_response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Tell me a funny joke!"}
    ]
)
    print("ChatGPT's energy consumption: ")
    print(f"Energy consumption: {openai_response.impacts.energy.value} kWh")
    print(f"GHG emissions: {openai_response.impacts.gwp.value} kgCO2eq")

    
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
