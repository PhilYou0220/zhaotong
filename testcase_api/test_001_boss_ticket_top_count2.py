import json
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
filename = os.path.join(CASEYAML, "test_001_boss_ticket_top_count2.yml")
api_name = "boss_ticket_top_count2"


@allure.epic("指挥中心顶部看板")
class TestTopCount2:
    # def setup_class(cls) -> None:
    #     """前置条件 删除造的数据相同名称的数据 """
    #     sql = "SELECT data FROM case_zhaotong  where  id =1"
    #     data = db3.select_real(sql)
    #     # 取name进行验证
    #     TestEmergency.verify_data = jsonpath.jsonpath(json.loads(data[0][0]), "$.name")
    #     # 删除应急预案历史数据
    #     del_emerg_case = f"DELETE from emerg_case WHERE name=\"{TestEmergency.verify_data[0]}\""
    #     emerg.delete(del_emerg_case)
    #     del_emerg_case_log = f"DELETE from emerg_case_log WHERE name=\"{TestEmergency.verify_data[0]}\""
    #     emerg.delete(del_emerg_case_log)
    #
    # def teardown_class(cls) -> None:
    #     print("星际闪耀光影,落入你的眼睛!")
    #     print("全部用例运行完成")

    @allure.title("指挥中心顶部看板市级")
    @pytest.mark.api
    # # @pytest.mark.run(order=1)
    def test_top_count2_0(cls):
        case_index = 0
        # my_request = AllApis()
        method, url, data, username, password, status_code, real_status_code, dict_return_data = AllApis().yaml_api_requests(
            filename=filename, api_name=api_name, case_index=case_index)
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码：{status_code}\n 实际返回状态码: {real_status_code}\n 实际返回值: {dict_return_data}\n ")

    @allure.title("指挥中心顶部看板区县")
    @pytest.mark.api
    # # @pytest.mark.run(order=2)
    def test_top_count2_1(cls):
        case_index = 1
        # my_request = AllApis()
        method, url, data, username, password, status_code, real_status_code, dict_return_data = AllApis().yaml_api_requests(
            filename=filename, api_name=api_name, case_index=case_index)
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码：{status_code}\n 实际返回状态码:{real_status_code}\n 实际返回值: {dict_return_data}\n ")

    @allure.title("指挥中心顶部看板镇街")
    @pytest.mark.api
    # @pytest.mark.run(order=3)
    def test_top_count2_2(cls):
        case_index = 2
        # my_request = AllApis()
        method, url, data, username, password, status_code, real_status_code, dict_return_data = AllApis().yaml_api_requests(
            filename=filename, api_name=api_name, case_index=case_index)
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码：{status_code}\n 实际返回状态码:{real_status_code}\n 实际返回值: {dict_return_data}\n ")


if __name__ == '__main__':
    pytest.main(["-sv", "test_1_boss_ticket_top_count2.py"])
    os.system(
        "allure generate  ../report/temp_jsonreport -o ../report/html --clean")
    os.system("allure open ../report/html")
