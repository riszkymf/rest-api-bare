import json


def get_response(status_code,data,message):
    if status_code == 200:
        return response_success(data,message=message)
    else :
        return response_error(message=message)

def response_success(data,message):
    response = {
        "code": 200,
        "data": data,
        "message": message
    }
    return json.dumps(response)

def response_error(message):
    response = {
        "code": 400,
        "message": message
    }
    return json.dumps(response)