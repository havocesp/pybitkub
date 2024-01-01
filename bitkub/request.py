import requests


def basic_request(method, url, headers=None, payload=None):
    headers = {} if headers is None else headers
    payload = {} if payload is None else payload
    return requests.request(method, url, headers=headers, data=payload).json()
