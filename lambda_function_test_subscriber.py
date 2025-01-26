import json

import pymongo
from pymongo import MongoClient
import os

from urllib import parse as urlparse
import base64
import time
#import datetime
#from datetime import datetime

mongodb_connexion_str = os.getenv('mongodb_connexion_string')



def lambda_handler(event, context):

    mongo_client = MongoClient(mongodb_connexion_str, server_api=pymongo.server_api.ServerApi(
    version="1", strict=True, deprecation_errors=True))

    database = mongo_client["llm_energy_impact"]

    collection = database["response"]


    document_list = [{'test': str(event) ,'datetime': str(time.time())}]

    result = collection.insert_many(document_list)

    mongo_client.close()

    #print(str(event['body']))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

