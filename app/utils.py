import requests

import os
import json


def fetch(url: str):
    ''' Generic function that returns the HTML content of a given URL. '''
    try:
        req = requests.get(url)
        status = req.status_code

        if str(status).startswith('2'):
            return req.text
        else:
            raise Exception
    except:
        return False


def storeAsJson(data, path: str):
    ''' Write a json file at a given filepath. '''
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def loadData(path: str):
    ''' Returns a python JSON object loaded from a file. If the provided file does not exists or is not stored with a json extension/as json, False will be returned. '''
    if os.path.exists(path):
        if path.lower().endswith('.json'):
            with open(path, 'r') as f:
                return json.load(f)
        else:
            return False
    else:
        return False
