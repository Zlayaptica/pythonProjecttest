import requests
import yaml


with open('config.yaml') as file:
    dict = yaml.safe_load(file)

url = dict['url']
url1 = dict['url1']
website = 'https://test-stand.gb.ru/api/posts'
username = 'kitty89'
password = '61d96a3985'


# def login(username, password):
#     obj_data = requests.post(url=url, data={'username':username, 'password': password})
#     token = obj_data.json()['token']
#     print(token)
#     return token


def token_auth(token):
    res = requests.get(url=dict["url1"], headers={"X-Auth-Token": token}, params={"owner": "notMe"})
    content_var = [item["content"] for item in res.json()['data']]
    return content_var


def test_step1(login):
    assert '' in token_auth(login)


def test_step2(postP):
    assert 'Anything' in postP


print(token_auth(dict['token']))
