import pandas as pd
import pymongo
from pymongo import MongoClient

mongodb_url = 'mongodb+srv://clementmsika:u6nDXiUZzzovT2Jp@serverlessinstance0.zhyp2im.mongodb.net/?retryWrites=true&w=majority&appName=ServerlessInstance0'

mongo_client = MongoClient(mongodb_url, server_api=pymongo.server_api.ServerApi(
    version="1", strict=True, deprecation_errors=True))
database = mongo_client["llm_energy_impact"]
db = mongo_client["llm_energy_impact"]
collection = db["response"]
response = collection.find_one(sort= [('datetime', -1)])

import ast

# Stringified dictionary
#stringified_dict = '{"key1": "value1", "key2": 2}'

# Convert to dictionary
dictionary = ast.literal_eval(response['test'])

#print(dictionary)

claude_response = dictionary['claude']['answer']

claude_min_ghg = dictionary['claude']['ghg_emissions'].split(' ')[0].split('=')[1]

claude_max_ghg = dictionary['claude']['ghg_emissions'].split(' ')[1].split('=')[1]

claude_min_energy = dictionary['claude']['energy_consumption'].split(' ')[0].split('=')[1]

claude_max_energy = dictionary['claude']['energy_consumption'].split(' ')[1].split('=')[1]

openai_response = dictionary['open_ai']['answer']

openai_min_ghg = dictionary['open_ai']['ghg_emissions'].split(' ')[0].split('=')[1]

openai_max_ghg = dictionary['open_ai']['ghg_emissions'].split(' ')[1].split('=')[1]

openai_min_energy = dictionary['open_ai']['energy_consumption'].split(' ')[0].split('=')[1]

openai_max_energy = dictionary['open_ai']['energy_consumption'].split(' ')[1].split('=')[1]


data = pd.DataFrame.from_dict([{'min_ghg_openai': openai_min_ghg, 'max_ghg_openai': openai_max_ghg,
                        'min_ghg_claude': claude_min_ghg, 'max_ghg_claude': claude_max_ghg,
                         'min_energy_openai': openai_min_energy, 'max_energy_openai': openai_max_energy,
                        'min_energy_claude': claude_min_energy, 'max_energy_claude': claude_max_energy,
                         'claude_response': claude_response,'openai_response': openai_response
                        }])

data = pd.DataFrame.from_dict([{'min_ghg_openai': openai_min_ghg, 'max_ghg_openai': openai_max_ghg,
                        'min_ghg_claude': claude_min_ghg, 'max_ghg_claude': claude_max_ghg,
                         'min_energy_openai': openai_min_energy, 'max_energy_openai': openai_max_energy,
                        'min_energy_claude': claude_min_energy, 'max_energy_claude': claude_max_energy,
                         'claude_response': claude_response,'openai_response': openai_response
                        }])


client.insert('llm_responses_ecologits_methodology', data, column_names=['min_ghg_openai', 'max_ghg_openai', 'min_ghg_claude',
                                              'max_ghg_claude', 'min_energy_openai', 'max_energy_openai',
                                              'min_energy_claude', 'max_energy_claude', 'claude_response',
                                              'openai_response'])


