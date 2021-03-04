import random
import json

if __name__ == '__main__':
    predictions = []
    for i in range(1440):
        point = {}
        point['ts'] = str(i)
        point['v1'] = str(random.uniform(0.0,1000.0))
        predictions.append(point)
    data = {}
    data['pumpid'] = str(666)
    data['predictions'] = predictions

    json_data = json.dumps(data)
    print(json_data)
    print(len(json_data))