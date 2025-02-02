import json

import os
import ast
from urllib import parse as urlparse
import base64
import time
import awswrangler as wr
import pandas as pd


def lambda_handler(event, context):

    conn = wr.postgresql.connect("postgres_jdbc_connexion")
    
    dictionary = ast.literal_eval(event)

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

    
    
    wr.postgresql.to_sql(data, conn, schema = 'llm', table="environmental_impact", mode="append")



    conn.close()

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
       # 'body': json.dumps(text)
    }

