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
filename = os.path.join(CASEYAML, "test_050_boss_company.yml")
api_name = "boss_company"


@allure.epic("企业管理--矿企管理--企业详情")
class TestMoatOrgFullTree:

    @allure.title("企业管理--矿企管理--企业详情")
    @pytest.mark.api
    @pytest.mark.run(order=1)
    def test_moat_org_full_tree_0(cls):
        case_index = 0
        method, url, data, username, password, status_code, real_status_code, dict_return_data = AllApis().yaml_api_requests(
            filename=filename, api_name=api_name, case_index=case_index)
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码：{status_code}\n 实际返回状态码: {real_status_code}\n 实际返回值: {dict_return_data}\n ")


if __name__ == '__main__':
    pass
