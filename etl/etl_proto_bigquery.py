

from google.oauth2 import service_account
import pandas_gbq

sql = 'SELECT * FROM gen_ai_consumption.ecologits_another_test'

credentials = service_account.Credentials.from_service_account_file(
    'bigquery_key.json',
)

project_id = 'gen-lang-client-0626658913'



df = pandas_gbq.read_gbq(sql, project_id=project_id, credentials=credentials)

df

import pandas
import pandas_gbq

# TODO: Set project_id to your Google Cloud Platform project ID.
# project_id = "my-project"
# TODO: Set table_id to the full destination table ID (including the
#       dataset ID).
# table_id = 'my_dataset.my_table'

df = pandas.DataFrame(
    {
        "my_string": ["a", "b", "c"],
        "my_int64": [1, 2, 3],
        "my_float64": [4.0, 5.0, 6.0],
        "my_bool1": [True, False, True],
        "my_bool2": [False, True, False],
        "my_dates": pandas.date_range("now", periods=3),
    }
)

pandas_gbq.to_gbq(df, 'gen_ai_consumption.ecologits_another_test', 'gen-lang-client-0626658913')

df = pandas_gbq.read_gbq('SELECT * FROM gen_ai_consumption.ecologits_another_test', 'gen-lang-client-0626658913')

