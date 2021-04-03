import json
import requests

URL = 'https://proxy-prod.511.org/api-proxy/api/v1/transit/tracker/'


def lambda_handler(event, context):
    if 'min' in event['queryStringParameters']:
        min = int(event['queryStringParameters']['min'])
    else:
        min = 0
    if 'max' in event['queryStringParameters']:
        max = int(event['queryStringParameters']['max'])
    else:
        max = 99
    response = \
        requests.get(url=URL,
                     params={'uuid': event['queryStringParameters']['uuid']})
    result = []
    for value in response.json()['real_time_departure_objects']:
        for time in value['next_departure_time_min']:
            itime = int(time)
            if itime >= min and itime <= max:
                result.append([itime, value['route_code']])
    result.sort(key=lambda tup: tup[0] + 1 / (256 - ord(tup[1][0])))
    return {'statusCode': 200, 'body': json.dumps(result)}
