import requests
from dbtools import chaxun

url = "http://192.144.148.91:2333/login"
data = {"username":"liuyun1", "password":"a123456781"} # 传送的数据,一定要是字典
res = requests.post(url=url, json=data)
assert res.status_code == 200
assert res.json().get("status") == 200

# 查询数据
sql = "select * from t_user where username='{}'".format(data.get("username"))
assert len(chaxun(sql)) != 0
print("登录成功！")


# 获取token
token = res.json().get("data").get("token")

# 用户退出
u = "http://192.144.148.91:2333/logout"
h = {"Content-Type":"application/json","token":token}
r = requests.get(url=u, headers=h)
print(r.text)