#!/usr/bin/env python
from distutils.log import log

from kafka import KafkaConsumer
import sys
import json
import pprint

if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise ValueError('Usage: optima-example-consumer.py host port topic')

    host = sys.argv[1]
    port = sys.argv[2]
    topic = sys.argv[3]

    pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)

    consumer = KafkaConsumer(topic,
                             bootstrap_servers=host + ':' + port,
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                             auto_offset_reset='latest')
    for msg in consumer:
        data_dict = msg.value
        pp.pprint(data_dict)
