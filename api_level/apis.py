# from tools.DB import db3
from tools.api_requests_duration import outer
from tools.auth_requests import Auth
from tools.parse_data import pd
import json
import allure
from tools.log import log
from tools.read_config import read_yaml


class AllApis(object):
    # def all_api_requests(self, sql: str):
    #     auth = Auth()
    #     result = db3.select(sql=sql)
    #     id, method, url, data, expect_return_data, username, password, status_code, *ig, type = pd.parse_data(result[0])
    #     if method:
    #         with allure.step(f"{ig[1]}"):
    #             dict_expect_return_data = json.loads(expect_return_data)
    #             dict_return_data, real_status_code = auth.auth_requests(data2=data, url=url, username=username,
    #                                                                     password=password, method=method, type=type)
    #         return id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data
    #     else:
    #         log.error(f"未知请求方式:{method}")

    def yaml_api_requests(self, filename: str, api_name: str, case_index: int):
        auth = Auth()
        method, url, data, username, password, status_code, type, title = pd.yaml_parse_data(filename=filename,
                                                                                             api_name=api_name,
                                                                                             case_index=case_index)
        with allure.step(f"{title}"):
            dict_return_data, real_status_code = auth.auth_requests(data2=data, url=url,
                                                                    username=username,
                                                                    password=password, method=method,
                                                                    type=type)
        return method, url, data, username, password, status_code, real_status_code, dict_return_data

    def yaml_api_requests_export(self, filename: str, api_name: str, case_index: int):
        auth = Auth()
        method, url, data, username, password, status_code, type, title = pd.yaml_parse_data(filename=filename,
                                                                                             api_name=api_name,
                                                                                             case_index=case_index)
        with allure.step(f"{title}"):
            dict_return_data, real_status_code = auth.auth_requests(data2=data, url=url,
                                                                    username=username,
                                                                    password=password, method=method,
                                                                    type=type, export=1)
        return method, url, data, username, password, status_code, real_status_code, dict_return_data
