#!/usr/bin/env python3.7
# coding: UTF-8

import datetime
import json
import os
import requests

def get_room_temperature():
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + os.environ['REMOTOKEN'],
    }

    response = requests.get('https://api.nature.global/1/devices', headers=headers)
    json = response.json()
    return json[0]['newest_events']['te']['val']

def post_service_metrics(temperature):
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'X-Api-Key': os.environ['MACKERELKEY'],
    }

    now = datetime.datetime.now()
    metrics = [
        {
            'name': 'Temperature.temperature',
            'time': int(now.timestamp()),
            'value': temperature
        }
    ]

    json.dumps(metrics),
    response = requests.post('https://api.mackerelio.com/api/v0/services/nature-remo/tsdb', json.dumps(metrics), headers=headers)
    print(response.json())
    
def lambda_handler(event, context):
    temperature = get_room_temperature()
    post_service_metrics(temperature)
