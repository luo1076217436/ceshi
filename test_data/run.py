from selenium import webdriver
from test_data import py_data
from test_data import hanshu
import time
drver=webdriver.Chrome()
drver.implicitly_wait(10)
url=py_data.url["url"]
user = py_data.login_data["user_name"]
password = py_data.login_data["password"]
key = py_data.key["key"]
hanshu.search_key(url=url,drver=drver,user_name=user,password=password,key=key)

