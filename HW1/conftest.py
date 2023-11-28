import pytest
import yaml
import requests


with open('config.yaml') as file:
    dict=yaml.safe_load(file)

url = dict['url']
url1 = dict['url1']


@pytest.fixture()
def login():
    all_data = requests.post(url=url, data={'username':'kitty89', 'password': '61d96a3985'})
    token = all_data.json()['token']
    return token

@pytest.fixture()
def postP():
    all_data = requests.post(url=url1, headers={"X-Auth-Token": dict['token']},data={
        'username':'kitty89',
        'password': '61d96a3985',
        'title': 'newTitle',
        'description': 'Anything',
        'content':'hello'})
    return all_data.json()['description']