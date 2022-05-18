import psycopg2 as pg
import time
import pandas as pd
import time
from pathlib import Path
from dotenv import load_dotenv
import os


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
def get_data_cmdb(query):
    input_time = time.time()
    conn = pg.connect(host="cmdb-rr.cbo3ijdmzhje.ap-south-1.rds.amazonaws.com", database="cmdb", port="5432",
                      user=os.environ['CMDB_USERNAME'], password=os.environ['CMDB_PASSWORD'])
    print('Connected to Replica DB')
    df = pd.read_sql_query(query, con=conn)
    print('Number of rows in Data - ' + str(df.shape[0]))
    final_time = time.time()
    print('Data retrieved in ' + str(final_time - input_time) + 'seconds')
    conn.close()
    return df

