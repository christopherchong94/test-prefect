from datetime import timedelta
from prefect import Flow
from prefect.schedules import IntervalSchedule
from prefect.storage import Github
from prefect.run_configs import DockerRun

import sys
sys.path.append('//Users/christopher.chong/Documents/src/backend-analytics/python/orchestration/prefect/prefect-client/src')
from task_flow_2 import task_test_flow


schedule = IntervalSchedule(interval=timedelta(minutes=1))

with Flow("test-flow-2", schedule) as flow:
    task_test_flow()

flow.storage = Github(repo="christopherchong94/test-prefect", path="/flows/test_flow_2.py")
flow.run_config = DockerRun(image="yuroitaki/prefect:v1")
