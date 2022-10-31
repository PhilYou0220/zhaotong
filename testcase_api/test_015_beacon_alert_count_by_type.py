import pytest
import allure
# 适配终端/服务器运行 IDE运行没问题
import sys

sys.path.append("/python_project/zhaotong/")
from tools.log import log
import os
from api_level.apis import AllApis
import pytest_check as check
from tools.project_path import CASEYAML

# 搞两个全局变量指定用例文件及接口名称
filename = os.path.join(CASEYAML, "test_015_beacon_alert_count_by_type.yml")
api_name = "beacon_alert_count_by_type"


@allure.epic("驾驶舱告警分类")
class TestBeaconAlertCountByType:

    @allure.title("指挥中心--告警分类--市级")
    @pytest.mark.api
    @pytest.mark.run(order=1)
    def test_beacon_alert_count_by_type_0(cls):
        case_index = 0
        method, url, data, username, password, status_code, real_status_code, dict_return_data = AllApis().yaml_api_requests(
            filename=filename, api_name=api_name, case_index=case_index)
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码：{status_code}\n 实际返回状态码: {real_status_code}\n 实际返回值: {dict_return_data}\n ")

    @allure.title("指挥中心--告警分类--区县")
    @pytest.mark.api
    @pytest.mark.run(order=2)
    def test_beacon_alert_count_by_type_1(cls):
        case_index = 1
        method, url, data, username, password, status_code, real_status_code, dict_return_data = AllApis().yaml_api_requests(
            filename=filename, api_name=api_name, case_index=case_index)
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码：{status_code}\n 实际返回状态码: {real_status_code}\n 实际返回值: {dict_return_data}\n ")

    @allure.title("指挥中心--告警分类--镇街")
    @pytest.mark.api
    @pytest.mark.run(order=3)
    def test_beacon_alert_count_by_type_2(cls):
        case_index = 2
        method, url, data, username, password, status_code, real_status_code, dict_return_data = AllApis().yaml_api_requests(
            filename=filename, api_name=api_name, case_index=case_index)
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码：{status_code}\n 实际返回状态码: {real_status_code}\n 实际返回值: {dict_return_data}\n ")

    @allure.title("税收监管--告警分类--市级")
    @pytest.mark.api
    @pytest.mark.run(order=4)
    def test_beacon_alert_count_by_type_3(cls):
        case_index = 3
        method, url, data, username, password, status_code, real_status_code, dict_return_data = AllApis().yaml_api_requests(
            filename=filename, api_name=api_name, case_index=case_index)
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码：{status_code}\n 实际返回状态码: {real_status_code}\n 实际返回值: {dict_return_data}\n ")

    @allure.title("税收监管--告警分类--区县")
    @pytest.mark.api
    @pytest.mark.run(order=5)
    def test_beacon_alert_count_by_type_4(cls):
        case_index = 4
        method, url, data, username, password, status_code, real_status_code, dict_return_data = AllApis().yaml_api_requests(
            filename=filename, api_name=api_name, case_index=case_index)
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码：{status_code}\n 实际返回状态码: {real_status_code}\n 实际返回值: {dict_return_data}\n ")

    @allure.title("税收监管--告警分类--镇街")
    @pytest.mark.api
    @pytest.mark.run(order=6)
    def test_beacon_alert_count_by_type_5(cls):
        case_index = 5
        method, url, data, username, password, status_code, real_status_code, dict_return_data = AllApis().yaml_api_requests(
            filename=filename, api_name=api_name, case_index=case_index)
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码：{status_code}\n 实际返回状态码: {real_status_code}\n 实际返回值: {dict_return_data}\n ")

    @allure.title("指挥中心--某个具体的矿区告警分类")
    @pytest.mark.api
    @pytest.mark.run(order=7)
    def test_beacon_alert_count_by_type_6(cls):
        case_index = 6
        method, url, data, username, password, status_code, real_status_code, dict_return_data = AllApis().yaml_api_requests(
            filename=filename, api_name=api_name, case_index=case_index)
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码：{status_code}\n 实际返回状态码: {real_status_code}\n 实际返回值: {dict_return_data}\n ")

    @allure.title("税收监管--某个具体的矿区告警分类")
    @pytest.mark.api
    @pytest.mark.run(order=8)
    def test_beacon_alert_count_by_type_7(cls):
        case_index = 7
        method, url, data, username, password, status_code, real_status_code, dict_return_data = AllApis().yaml_api_requests(
            filename=filename, api_name=api_name, case_index=case_index)
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码：{status_code}\n 实际返回状态码: {real_status_code}\n 实际返回值: {dict_return_data}\n ")


if __name__ == '__main__':
    pass
