#!/usr/bin/env python

# This is an example producer for the optima project
from kafka import KafkaProducer
import sys
import random
import time
import json
import pprint
from datetime import datetime, timedelta


def generate_example_data():
    predictions = []
    now = int(time.time())
    last_interval = now - (now % (10 * 60))
    next_interval = last_interval + 600
    for i in range(1440):
        # Random data points for every minute of the next 24 hours and random values
        point = {'ts': str(next_interval + i * 60), 'v1': str(random.uniform(0.0, 1000.0))}
        predictions.append(point)
    data = {'pump_id': str(666), 'interval_start': str(next_interval), 'predictions': predictions}

    print("Record generated at " + str(datetime.utcnow()) + " or in unix timestamp format: " + str(now))
    return data


if __name__ == '__main__':

    if len(sys.argv) != 4:
        raise ValueError('Usage: optima-example-producer.py host port topic')

    host = sys.argv[1]
    port = sys.argv[2]
    topic = sys.argv[3]

    pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)

    while 1:
        data_dict = generate_example_data()
        pp.pprint(data_dict)
        producer = KafkaProducer(bootstrap_servers=host + ':' + port,
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))

        producer.send(topic, data_dict)
        producer.close()

        dt = datetime.now() + timedelta(seconds=60)
        dt = dt.replace(second=15)

        while datetime.now() < dt:
            time.sleep(1)
