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
from tools import web_socket


@allure.epic("昭通web_socket心跳测试")
class TestMoatOrgFullTree:

    @allure.title("昭通web_socket心跳测试")
    @pytest.mark.api
    # @pytest.mark.run(order=1)
    def test_moat_org_full_tree_0(cls):
        web_socket.test()


if __name__ == '__main__':
    pass
