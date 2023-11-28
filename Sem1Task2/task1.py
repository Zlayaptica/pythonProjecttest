import pytest
import requests

url = 'https://test-stand.gb.ru/gateway/login'
login = "kitty89",
password = "61d96a3985"

result = requests.post(url=url, data={"username": login, "password": password})
token=result.json()["token"]

res_get = requests.get(url="https://test-stand.gb.ru/api/posts", headers={"X-Auth-Token": token}, params={"owner": "notMe"})
print(res_get)
print(res_get.json())