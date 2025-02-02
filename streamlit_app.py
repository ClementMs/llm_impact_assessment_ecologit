import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

from dotenv import load_dotenv
import os
import requests
import time
import pymongo
from pymongo import MongoClient
import psycopg2

# Load the .env file
load_dotenv()

# Access the environmental variables
openai_api_key = os.getenv('openai_api_key')
claude_api_key = os.getenv('claude_api_key')
mangodb_url = os.getenv('mangodb_url')
postgres_pwd = os.getenv('postgres_pwd')

st.title("🦜🔗 Quickstart App")

#openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def generate_response(input_text):
    #model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
    st.info("Bonjour, nous avons reçue votre demande, soyez patient pendant que nous la traitons pour évaluer son impact environnemental. Merci encore d'utiliser notre app d'IA générative :)")
    
    url = 'https://xi1om2c6db.execute-api.us-east-1.amazonaws.com/default/lambda_function_test'
    headers = {"Content-Type": "application/json"}
    payload = {"key": input_text}

    response = requests.post(url, json=payload, headers=headers)
    print("Réponse API Gateway :", response.json())
    #if response['ResponseMetadata']['HTTPStatusCode'] == 202:
    #    st.info('Votre demande a été traitée')
    if True: 
        st.info('votre demande a été traitée')    

def pull_answer():
    time.sleep(15)
    #mongo_client = MongoClient(mangodb_url, server_api=pymongo.server_api.ServerApi(
    #version="1", strict=True, deprecation_errors=True))
    conn = psycopg2.connect(dbname = 'ecologits', host ='database-1.c9ycos4qoa1l.us-east-1.rds.amazonaws.com', port = '5432', user= 'postgres', password = postgres_pwd)
    cur = conn.cursor()
    conn.autocommit = True
    data = pd.read_sql('SELECT * FROM llm.environmental_impact', conn)
    #database = mongo_client["llm_energy_impact"]
    #db = mongo_client["llm_energy_impact"]
    #collection = db["response"]
    #response = collection.find_one(sort= [('datetime', -1)])
    st.dataframe(data)
    conn.close()

with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)
        pull_answer()

    #if not openai_api_key.startswith("sk-"):
    #    st.warning("Please enter your OpenAI API key!", icon="⚠")
    #if submitted and openai_api_key.startswith("sk-"):
    #    generate_response(text.content)
