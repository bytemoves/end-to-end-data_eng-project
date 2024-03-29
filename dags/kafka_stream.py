from datetime import datetime
# from airflow import DAG
import pendulum

# AIRFLOW_TIMEZONE = pendulum.timezone("UTC")


# from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'morgan',
    'start_date' : datetime(2024,3,29,15) # March 29th,
    
}

def stream_data():
    import requests
    import json
    
    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]
    print(json.dumps(res,indent=3))
    



# with DAG ( 'user_automation',
#           default_args = default_args,
#           schedule_interval = '@daily',
#           cathup = False) as dag:

#  streaming_task = PythonOperator(
#     task_id = 'stream_data_from_api',
#     python_callable = stream_data
# )
if __name__ == "__main__":
    stream_data()




