#!/usr/bin/env python3

from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
import boto3

app = FastAPI()

class State(BaseModel):
    state: Optional[str] = None

@app.get("/")  # zone apex
def read_root():
    return {"Hello": "World"}

# Do things w/ EC2
@app.get("/instance")
def get_instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    Instances = []
    for r in response['Reservations']:
        for i in r['Instances']:
            Instances.append(i['InstanceId'])
    return {"Instances": Instances}

# Do things w/ EC2
@app.get("/instance/{instance_id}")
def get_one_instance(instance_id):
    ec2 = boto3.client("ec2")
    response = ec2.describe_instances(
        InstanceIds=[instance_id]
    )
    return response

@app.get("/instance/{instance_id}/state")
def get_instance_state(instance_id):
    ec2 = boto3.client("ec2")
    response = ec2.describe_instances(
        InstanceIds=[instance_id]
    )
    State = response['Reservations'][0]['Instances'][0]['State']['Name']
    return {"InstanceState": State}

@app.post("/instance/{instance_id}/state")
def update_state(instance_id, state: State):
    # ec2 = boto3.client("ec2")
    return state
