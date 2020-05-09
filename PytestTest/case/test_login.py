"""
    登录相关的测试用例
"""
import pytest           # 管测试用例
import requests         # 实现如何请求接口


def test_login():
    url = "http://192.144.148.91:2333/login"
    data = {"username":"zhanghaha", "password":"a1234567"}
    res = requests.post(url=url, json=data)
    assert res.status_code == 200
    assert res.json().get("status") == 200
    # 数据库查询
    # 保存token：存到txt中:python读写文件
    with open("./token.txt", "w") as f:
        token = res.json().get("data").get("token")
        f.writelines(token)

def test_logout():
    # 1.获取token
    with open("./token.txt", "r") as f:
        token = f.read()
    url = "http://192.144.148.91:2333/logout"
    headers = {"Content-Type":"application/json","token": token}
    res = requests.get(url=url, headers=headers)

    assert res.status_code == 200
    assert res.json().get("status") == 200

