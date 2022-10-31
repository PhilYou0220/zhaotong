import requests
import hashlib
import time
from tools.log import log
import json
from tools.read_config import read_config


class Auth(object):
    """requests请求时加上 verify=False 避免ssl认证 不然有时会报错 requests.exceptions.SSLError"""

    def base_post(self, username: str, password: str, type) -> str:
        """
        获取账号的token
        :param username:
        :param password:
        :return:
        """
        my_config = read_config()
        url = None

        if type == 1:
            # 测试环境地址
            # url = "http://192.168.101.184:8000/moat/phone/login"
            # url = "http://192.168.101.116:8004/moat/phone/login"
            url = my_config["zhaotong_test"]["url_web_login"]
        elif type == 2:
            # url = "http://223.85.203.92:8001/moat/phone/login"
            # url = "http://192.168.101.116:8001/moat/phone/login"
            url = my_config["zhaotong_test"]["url_mobile_login"]
        else:
            log.error(f"未知类型；{type}")
        username = username
        # 使用encode 防止密码中含有中文 把密码进行md5加密
        password = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
        headers = {"content-type": "application/json; charset=utf-8"}
        data = {
            "phone": username,
            "password": password,
            "platform_id": 1
        }
        # 由于指定了json不需要 转换 如果是json参数变为data则需要转换
        r1 = requests.post(url=url, json=data, headers=headers).json()

        try:
            if r1["data"].get("token"):  # 判断是否有能通过键获取值 如果不能会抛error
                pass
        except Exception as e:
            log.error(f"登录时获取不到token，报错类型：{e} ，帐号或密码错误 错误信息为：登录报错{r1}")
        token = r1["data"]["token"]
        # 进行职位确认 获得真实token
        temp_token = "Bearer" + " " + token
        headers = {
            "authorization": temp_token
        }
        if type == 1:
            # web端 url和职位先写死吧
            # confirm_url = "http://192.168.101.184:8000/moat/position/confirm"
            # confirm_url = "http://192.168.101.116:8004/moat/position/confirm"
            confirm_url = my_config["zhaotong_test"]["url_web_confirm"]
            position_data = {"position_id": 111}
            # position_data = {"position_id": 4}
            r2 = requests.post(url=confirm_url, json=position_data, headers=headers).json()
            try:
                if r2["data"].get("token"):  # 判断是否有能通过键获取值 如果不能会抛error
                    pass
            except Exception as e:
                log.error(f"报错类型：{e} ，职位确认错误 错误信息为：登录报错{r2}")
            real_token = r2["data"]["token"]
            return real_token
        elif type == 2:
            headers = {
                "authorization": temp_token,
                "platform": "zt",
                "udid": "f5e86a185452e87e",
                "os": "Android",
                "type": "mobile",
                "brand": "xiaomi Redmi Note 7 Pro",
                "app": "kuangshanjianguan",
                "app-version": "1.0.0",
                "user-agent": "Dart/2.14 (dart:io)"
            }

            # app端 url和职位先写死吧
            # confirm_url = "http://223.85.203.92:8001/mb/moat/position/confirm"
            # confirm_url = "http://192.168.101.116:8001/mb/moat/position/confirm"
            confirm_url = my_config["zhaotong_test"]["url_mobile_confirm"]
            position_data = {"position_id": 52}
            # position_data = {"position_id": 32}
            r2 = requests.post(url=confirm_url, json=position_data, headers=headers).json()
            try:
                if r2["data"].get("token"):  # 判断是否有能通过键获取值 如果不能会抛error
                    pass
            except Exception as e:
                log.error(f"报错类型：{e} ，职位确认错误 错误信息为：登录报错{r2}")
            real_token = r2["data"]["token"]
            return real_token
        else:
            log.error(f"未知类型")

    def auth_requests(self, url, data2, username, password, method, type, export=None):
        token = self.base_post(username, password, type)
        real_token = "Bearer" + " " + token
        headers = {
            "authorization": real_token
        }
        resp = None
        if method == "POST":
            try:
                resp = requests.post(url=url, json=json.loads(data2), headers=headers)
            except Exception as e:
                log.error(f"报错类型：{e}  ")
            real_r = resp.json()
            real_status_code = resp.status_code
            return real_r, real_status_code
        elif method == "PUT":
            try:
                resp = requests.put(url=url, json=json.loads(data2), headers=headers)
            except Exception as e:
                log.error(f"报错类型：{e}  ")
            real_r = resp.json()
            real_status_code = resp.status_code
            return real_r, real_status_code
        elif method == "DELETE":
            try:
                resp = requests.delete(url=url, json=json.loads(data2), headers=headers)
            except Exception as e:
                log.error(f"报错类型：{e}  ")
            real_r = resp.json()
            real_status_code = resp.status_code
            return real_r, real_status_code
        elif method == "GET":
            try:
                resp = requests.get(url=url, params=data2, headers=headers)
            except Exception as e:
                log.error(f"报错类型：{e}  ")
            #  解决二进制文件问题
            if export is None:
                real_r = resp.json()
                real_status_code = resp.status_code
                return real_r, real_status_code
            else:
                real_r = resp.content
                real_status_code = resp.status_code
                return real_r, real_status_code

        else:
            log.error(f"未知请求方式：{method}")

    def register_post(self, url, data):
        url = url
        data = data
        headers = {"content-type": "application/json; charset=utf-8"}
        res = requests.post(url=url, json=json.loads(data), headers=headers)
        real_status_code = res.status_code
        dict_r = res.json()
        if dict_r.get("error"):
            log.error(
                f" \n url:{url}\n 请求参数: {data}\n 返回状态码: {real_status_code}\n 返回值: {dict_r}")
        return dict_r, real_status_code


if __name__ == '__main__':
    a = Auth()
    b, c = a.auth_requests(username="15181195029", password="123", method="GET",
                           data2="page=1&limit=20&case_type=2&from=1654704000&to=1655308799&load_all=0",
                           url="http://192.168.101.184:8001/mb/emerg/emergencylist?", type=2)
    print(b)
    print(c)
