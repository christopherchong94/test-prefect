from datetime import timedelta
from prefect import Flow
from prefect.schedules import IntervalSchedule
from prefect.storage import GitHub
from prefect.run_configs import DockerRun

import sys
sys.path.append('/app/src')
from task_flow_2 import task_test_flow


schedule = IntervalSchedule(interval=timedelta(minutes=1))

with Flow("test-flow-2", schedule) as flow:
    task_test_flow()

flow.storage = GitHub(repo="christopherchong94/test-prefect", path="/flows/test_flow_2.py")
flow.run_config = DockerRun(image="yuroitaki/prefect:v1")
