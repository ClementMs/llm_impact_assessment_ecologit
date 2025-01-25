import json
import ecologits
from ecologits import EcoLogits
import os
from openai import OpenAI
from anthropic import Anthropic
import boto3
boto_client = boto3.client('lambda')
#import pymongo
#from pymongo import MongoClient
#from huggingface_hub import InferenceClient
#from langchain_openai.chat_models import ChatOpenAI

cwd = os.getcwd()

cred_dir = cwd + '/'
openai_access_key_dir = cred_dir + 'openai_key.txt'
f = open(openai_access_key_dir, 'r')
openai_access_key = f.read()
claude_access_key_dir = cred_dir + 'claude_key.txt'
f = open(claude_access_key_dir, 'r')
claude_access_key = f.read()

mongodb_connexion_str = os.getenv('mongodb_connexion_string')


def lambda_handler(event, context):
    EcoLogits.init()


    client = Anthropic(api_key=claude_access_key)

    #mongo_client = MongoClient(mongodb_connexion_str, server_api=pymongo.server_api.ServerApi(
 #version="1", strict=True, deprecation_errors=True))

    #database = client["llm_energy_impact"]

    #collection = database["response"]

    #client.close()

    response_dictionary = {}

    claude_response = client.messages.create(
    max_tokens=100,
    messages=[{"role": "user", "content": "Tell me a funny joke!"}],
    model="claude-3-haiku-20240307",
)

    response_dictionary['claude'] = { 'ghg_emissions': str(claude_response.impacts.gwp.value),'energy_consumption': str(claude_response.impacts.energy.value)}


    #print(claude_response)




    # Get estimated environmental impacts of the inference
    #print("Claude 3 Haiku's energy consumption: ")
    #print(f"Energy consumption: {claude_response.impacts.energy.value} kWh")
    #print(f"GHG emissions: {claude_response.impacts.gwp.value} kgCO2eq")

    

    client = OpenAI(api_key=openai_access_key)
    openai_response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Tell me a funny joke!"}
    ]
)
    #print("ChatGPT's energy consumption: ")
    #print(f"Energy consumption: {openai_response.impacts.energy.value} kWh")
    #print(f"GHG emissions: {openai_response.impacts.gwp.value} kgCO2eq")

    #client = InferenceClient(model="HuggingFaceH4/zephyr-7b-beta")
    #response = client.chat_completion(
    #messages=[{"role": "user", "content": "Tell me a funny joke!"}],
    #max_tokens=15
#)

    #print(response)

    response_dictionary['open_ai'] = {'ghg_emissions': str(openai_response.impacts.gwp.value),'energy_consumption': str(openai_response.impacts.energy.value)}

    #resp = boto_client.invoke(
    #    FunctionName='arn:aws:lambda:us-east-1:406942271653:function:second_lambda_function_test_subscriber', #Arn of our second or asynchronous lambda
    #    InvocationType='Event',
    #    Payload=json.dumps('ok')
    #    )

    #print(resp)

    resp = boto_client.invoke(
        FunctionName='arn:aws:lambda:us-east-1:406942271653:function:second_lambda_function_test_subscriber', #Arn of our second or asynchronous lambda
        InvocationType='Event',
        Payload=json.dumps(str(response_dictionary))
        )
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(str(resp))
    }

