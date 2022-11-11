import json
import pytest
import allure
# 适配终端/服务器运行 IDE运行没问题
import sys
sys.path.append("/python_project/zhaotong/")
from tools.DB import db3, emerg
from tools.log import log
import os
from tools.rmq import rmq_business_test
from tools.update_data import update_data
from api_level.apis import AllApis
import pytest_check as check
import jsonpath
from string import Template
from tools.current_time_about import my_time


@allure.epic("应急预案正向用例")
class TestEmergency:

    def setup_class(cls) -> None:
        """前置条件 删除造的数据相同名称的数据 """
        sql = "SELECT data FROM case_zhaotong  where  id =1"
        data = db3.select_real(sql)
        # 取name进行验证
        TestEmergency.verify_data = jsonpath.jsonpath(json.loads(data[0][0]), "$.name")
        # 删除应急预案历史数据
        del_emerg_case = f"DELETE from emerg_case WHERE name=\"{TestEmergency.verify_data[0]}\""
        emerg.delete(del_emerg_case)
        del_emerg_case_log = f"DELETE from emerg_case_log WHERE name=\"{TestEmergency.verify_data[0]}\""
        emerg.delete(del_emerg_case_log)

    def teardown_class(cls) -> None:
        print("星际闪耀光影,落入你的眼睛!")
        print("全部用例运行完成")

    @allure.title("01.创建应急预案")
    @pytest.mark.smoke
    # @pytest.mark.run(order=1)
    def test_emergency_01(cls):
        sql = "SELECT * FROM case_zhaotong  where  id =1"
        id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().all_api_requests(
            sql=sql)
        # 加到实例空间的属性中 data原是json字符串 现在转换成dict
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        check.equal(dict_expect_return_data, dict_return_data,
                    f"预期和实际不一致 预期返回值{dict_expect_return_data}和实际返回值{dict_return_data}不一致")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")

    @allure.title("02.查询刚创建的应急预案")
    @pytest.mark.smoke
    # @pytest.mark.run(order=2)
    def test_emergency_02(cls):
        sql = "SELECT * FROM case_zhaotong  where  id =2"
        id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().all_api_requests(
            sql=sql)
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        # 取最后一条数据进行比较因为是时间倒序排列的
        response_name = jsonpath.jsonpath(dict_return_data, "$.data[-1:].name")
        check.equal(TestEmergency.verify_data, response_name,
                    f"预期和实际不一致 预期返回值{TestEmergency.verify_data}和实际返回值{response_name}不一致")
        # 创建的应急预案主键ID 取到ID后面使用
        TestEmergency.verify_id = jsonpath.jsonpath(dict_return_data, "$.data[-1:].id")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")

    @allure.title("03.指挥中心发起应急预案")
    @pytest.mark.smoke
    # @pytest.mark.run(order=3)
    def test_emergency_03(cls):
        # 更新case3请求体数据 发起应急预案的预案的主键ID
        update_data(database="testgroup", table_name="case_zhaotong", id=3, key="emerg_case_id",
                    value=TestEmergency.verify_id[0])

        sql = "SELECT * FROM case_zhaotong  where  id =3"
        id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().all_api_requests(
            sql=sql)
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")

        check.equal(dict_expect_return_data, dict_return_data,
                    f"预期和实际不一致 预期返回值{dict_expect_return_data}和实际返回值{dict_return_data}不一致")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")

    @allure.title("04.指挥中心地图查看新增的预案")
    @pytest.mark.smoke
    # @pytest.mark.run(order=4)
    def test_emergency_04(cls):
        sql = "SELECT * FROM case_zhaotong  where  id =4"
        id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().all_api_requests(
            sql=sql)
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        # 发起的应急预案记录名称 倒序取第一条
        TestEmergency.data_emerge_log_name = jsonpath.jsonpath(dict_return_data, "$.data.log[0].name")
        # 发起的应急预案记录表主键ID 倒序取第一条
        TestEmergency.data_emerge_log_id = jsonpath.jsonpath(dict_return_data, "$.data.log[0].id")
        check.equal(TestEmergency.verify_data, TestEmergency.data_emerge_log_name,
                    f"预期和实际不一致 预期返回值{TestEmergency.verify_data}和实际返回值{TestEmergency.data_emerge_log_name}不一致")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")

    @allure.title("05.APP端查看发起的应急预案")
    @pytest.mark.smoke
    # @pytest.mark.run(order=5)
    def test_emergency_05(cls):
        # 更新get请求的参数 更新列表查询时间
        tmp = "\"page=1&limit=20&case_type=2&from=${from}&to=${to}&load_all=0\""
        start, end = my_time.current_timestamp()
        param = {"from": start, "to": end}
        res = Template(tmp).substitute(param)
        update_data(database="testgroup1", table_name="case_zhaotong", id=5, field="data",
                    content=res)

        sql = "SELECT * FROM case_zhaotong  where  id =5"
        id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().all_api_requests(
            sql=sql)
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        # 手机上列表发起预案的名称 由于是倒序选择最新一条
        verify_emerge_log_name = jsonpath.jsonpath(dict_return_data, "$.data[0].name")
        # 手机上列表发起预案的id 由于是倒序选择最新一条
        verify_emerge_log_id = jsonpath.jsonpath(dict_return_data, "$.data[0].id")
        # 断言名称
        check.equal(TestEmergency.verify_data, verify_emerge_log_name,
                    f"预期和实际不一致 预期返回值{TestEmergency.verify_data}和实际返回值{verify_emerge_log_name}不一致")
        # 断言id
        check.equal(TestEmergency.data_emerge_log_id, verify_emerge_log_id,
                    f"预期和实际不一致 预期返回值{TestEmergency.data_emerge_log_id}和实际返回值{verify_emerge_log_id}不一致")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")

    @allure.title("06.APP端点击应急预案")
    @pytest.mark.smoke
    # @pytest.mark.run(order=6)
    def test_emergency_06(cls):
        # 更新列表点击预案的ID
        tmp6 = "\"id=${id}\""
        param = {"id": TestEmergency.data_emerge_log_id[0]}
        res = Template(tmp6).substitute(param)
        update_data(database="testgroup1", table_name="case_zhaotong", id=6, field="data",
                    content=res)

        sql = "SELECT * FROM case_zhaotong  where  id =6"
        id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().all_api_requests(
            sql=sql)
        # 断言状态码
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")

        # 断言是否一致
        response_id = jsonpath.jsonpath(dict_return_data, "$.data.id")
        check.equal(TestEmergency.data_emerge_log_id, response_id,
                    f"预期和实际不一致 预期返回值{TestEmergency.verify_data}和实际返回值{response_id}不一致")

        # 断言是否有 回执按钮 能回执为1
        can_op = 1
        verify_can_op = jsonpath.jsonpath(dict_return_data, "$.data.can_op")
        check.equal(can_op, verify_can_op[0],
                    f"预期和实际不一致 预期返回值{can_op}和实际返回值{verify_can_op[0]}不一致")

        # 断言是否有 已执行干预 按钮,没有此按钮为1 有为0 此处为0 有按钮
        intervene_status = 0
        verify_intervene_status = jsonpath.jsonpath(dict_return_data, "$.data.intervene_status")
        check.equal(intervene_status, verify_intervene_status[0],
                    f"预期和实际不一致 预期返回值{intervene_status}和实际返回值{verify_intervene_status[0]}不一致")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")

    @allure.title("07.APP端应急预案-回执信息")
    @pytest.mark.smoke
    # @pytest.mark.run(order=7)
    def test_emergency_07(cls):
        # 更新case7请求体数据 发起了应急预案的log的主键ID
        update_data(database="testgroup", table_name="case_zhaotong", id=7, key="emerg_case_log_id",
                    value=TestEmergency.data_emerge_log_id[0])

        sql = "SELECT * FROM case_zhaotong  where  id =7"
        id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().all_api_requests(
            sql=sql)
        # 记录回执的内容
        TestEmergency.content = json.loads(data)["content"]
        # 断言请求发起预案的log_id
        emerge_log_07 = jsonpath.jsonpath(json.loads(data), "$.emerg_case_log_id")
        check.equal(TestEmergency.data_emerge_log_id, emerge_log_07,
                    f"预期和实际不一致 预期状态码{TestEmergency.data_emerge_log_id}和实际状态码{emerge_log_07}")

        # 断言状态码
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        # 断言返回值
        check.equal(dict_expect_return_data, dict_return_data,
                    f"预期和实际不一致 预期返回值{dict_expect_return_data}和实际返回值{dict_return_data}不一致")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")

    @allure.title("08.APP端应急预案-执行干预")
    @pytest.mark.smoke
    # @pytest.mark.run(order=8)
    def test_emergency_08(cls):
        # 更新准备修改的已执行干预的发起预案的log 请求体
        update_data(database="testgroup", table_name="case_zhaotong", id=8, key="emerg_case_log_id",
                    value=TestEmergency.data_emerge_log_id[0])
        sql = "SELECT * FROM case_zhaotong  where  id =8"
        id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().all_api_requests(
            sql=sql)
        # 断言请求发起预案的log_id
        emerge_log_08 = jsonpath.jsonpath(json.loads(data), "$.emerg_case_log_id")
        check.equal(TestEmergency.data_emerge_log_id, emerge_log_08,
                    f"预期和实际不一致 预期状态码{TestEmergency.data_emerge_log_id}和实际状态码{emerge_log_08}")
        # 断言状态码
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        # 断言返回值
        check.equal(dict_expect_return_data, dict_return_data,
                    f"预期和实际不一致 预期返回值{dict_expect_return_data}和实际返回值{dict_return_data}不一致")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")

    @allure.title("09.APP端应急预案-执行干预之后执行干预按钮消失")
    @pytest.mark.smoke
    # @pytest.mark.run(order=9)
    def test_emergency_09(cls):
        # APP端从列表点击应急预案查看执行干预的 应此复用第6条用例参数
        sql = "SELECT * FROM case_zhaotong  where  id =6"
        id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().all_api_requests(
            sql=sql)
        # 断言状态码
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        # 断言是id否一致
        response_id = jsonpath.jsonpath(dict_return_data, "$.data.id")
        check.equal(TestEmergency.data_emerge_log_id, response_id,
                    f"预期和实际不一致 预期返回值{TestEmergency.verify_data}和实际返回值{response_id}不一致")
        # 断言是否有 回执按钮 能回执为1
        can_op = 1
        verify_can_op = jsonpath.jsonpath(dict_return_data, "$.data.can_op")
        check.equal(can_op, verify_can_op[0],
                    f"预期和实际不一致 预期返回值{can_op}和实际返回值{verify_can_op[0]}不一致")
        # 断言是否有 已执行干预 按钮,没有此按钮为1 有为0 此处为1
        intervene_status = 1
        verify_intervene_status = jsonpath.jsonpath(dict_return_data, "$.data.intervene_status")
        check.equal(intervene_status, verify_intervene_status[0],
                    f"预期和实际不一致 预期返回值{intervene_status}和实际返回值{verify_intervene_status[0]}不一致")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")

    @allure.title("10.web端--查看应急事项记录列表")
    @pytest.mark.smoke
    # @pytest.mark.run(order=10)
    def test_emergency_10(cls):
        sql = "SELECT * FROM case_zhaotong  where  id =9"
        id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().all_api_requests(
            sql=sql)
        # 断言状态码
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        # 断言发起应急记录的id
        emerge_log_10 = jsonpath.jsonpath(dict_return_data, "$.data[0].id")
        check.equal(TestEmergency.data_emerge_log_id, emerge_log_10,
                    f"预期和实际不一致 预期返回值{TestEmergency.data_emerge_log_id}和实际返回值{emerge_log_10}不一致")

        # 断言发起应急记录的name
        emerge_log_10_name = jsonpath.jsonpath(dict_return_data, "$.data[0].name")
        check.equal(TestEmergency.data_emerge_log_name, emerge_log_10_name,
                    f"预期和实际不一致 预期返回值{TestEmergency.data_emerge_log_name}和实际返回值{emerge_log_10_name}不一致")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")

    @allure.title("11.web端--应急事项记录--查看回执信息")
    @pytest.mark.smoke
    # @pytest.mark.run(order=11)
    def test_emergency_11(cls):
        # 更新列表点击预案的ID
        tmp11 = "\"page=1&limit=10&emerg_case_log_id=${emerg_case_log_id}\""
        param = {"emerg_case_log_id": TestEmergency.data_emerge_log_id[0]}
        res = Template(tmp11).substitute(param)
        update_data(database="testgroup1", table_name="case_zhaotong", id=10, field="data",
                    content=res)

        sql = "SELECT * FROM case_zhaotong  where  id =10"
        id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().all_api_requests(
            sql=sql)

        # 断言状态码
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")

        # 断言发起应急记录的id
        sql = f"SELECT id FROM emerg_case_receipt_log WHERE emerg_case_log_id={TestEmergency.data_emerge_log_id[0]}"
        # 拿到回执表的id
        receipt_id = None
        try:
            receipt_id = emerg.select(sql)[0]["id"]
        except Exception as e:
            log.error(e)

        TestEmergency.receipt_log_id = jsonpath.jsonpath(dict_return_data, "$.data[0].id")
        check.equal(receipt_id, TestEmergency.receipt_log_id[0],
                    f"预期和实际不一致 预期返回值{receipt_id}和实际返回值{TestEmergency.receipt_log_id[0]}不一致")

        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")

    @allure.title("12.web端--应急事项记录--查看回执信息--查看详情")
    @pytest.mark.smoke
    # @pytest.mark.run(order=12)
    def test_emergency_12(cls):
        # 更新列表点击预案的ID
        tmp12 = "\"id=${id}\""
        param = {"id": TestEmergency.receipt_log_id[0]}
        res = Template(tmp12).substitute(param)
        update_data(database="testgroup1", table_name="case_zhaotong", id=11, field="data",
                    content=res)

        sql = "SELECT * FROM case_zhaotong  where  id =11"
        id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().all_api_requests(
            sql=sql)

        # 断言状态码
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")

        # 断言发起应急记录的id
        receipt_log_12 = jsonpath.jsonpath(dict_return_data, "$.data.id")
        check.equal(TestEmergency.receipt_log_id, receipt_log_12,
                    f"预期和实际不一致 预期返回值{TestEmergency.receipt_log_id}和实际返回值{receipt_log_12}不一致")
        # 断言回执的内容
        content = jsonpath.jsonpath(dict_return_data, "$.data.content")
        check.equal(TestEmergency.content, content[0],
                    f"预期和实际不一致 预期返回值:{TestEmergency.content}和实际返回值{content[0]}不一致")

        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")

    @allure.title("13.web端--应急事项记录--查看应急预案详情(是否执行干预)")
    @pytest.mark.smoke
    # @pytest.mark.run(order=13)
    def test_emergency_13(cls):
        # 更新列表点击预案的ID
        tmp13 = "\"emerg_case_log_id=${emerg_case_log_id}&page=1&limit=10\""
        param = {"emerg_case_log_id": TestEmergency.data_emerge_log_id[0]}
        res = Template(tmp13).substitute(param)
        update_data(database="testgroup1", table_name="case_zhaotong", id=12, field="data",
                    content=res)

        # 断言发起应急记录的id
        sql = f"SELECT id FROM emerg_case_intervene_log WHERE emerg_case_log_id={TestEmergency.data_emerge_log_id[0]}"
        # 拿到干预表的id
        intervene_id = None
        try:
            intervene_id = emerg.select(sql)[0]["id"]
        except Exception as e:
            log.error(e)

        sql = "SELECT * FROM case_zhaotong  where  id =12"
        id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().all_api_requests(
            sql=sql)

        # 断言发起应急记录的id
        intervene_log_13 = jsonpath.jsonpath(dict_return_data, "$.data[0].id")
        check.equal(intervene_id, intervene_log_13[0],
                    f"预期和实际不一致 预期返回值{intervene_id}和实际返回值{intervene_log_13[0]}不一致")

        # 断言状态码
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")

        # 断言回执的内容
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")

    @allure.title("14.web端--应急调度--指挥中心--进入会议室")
    @pytest.mark.smoke
    # @pytest.mark.run(order=14)
    def test_emergency_14(cls):
        # 更新进入会议发起的预案
        tmp14 = "\"id=${id}\""
        param = {"id": TestEmergency.data_emerge_log_id[0]}
        res = Template(tmp14).substitute(param)
        update_data(database="testgroup1", table_name="case_zhaotong", id=13, field="data",
                    content=res)

        sql = "SELECT * FROM case_zhaotong  where  id =13"
        id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().all_api_requests(
            sql=sql)

        # 断言状态码
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")

        # 断言发起的预案id
        emerge_log_14 = jsonpath.jsonpath(dict_return_data, "$.data.id")
        check.equal(TestEmergency.data_emerge_log_id, emerge_log_14,
                    f"预期和实际不一致 预期状态码{TestEmergency.data_emerge_log_id}和实际状态码{emerge_log_14}")

        # 断言发起的预案name
        emerge_log_14_name = jsonpath.jsonpath(dict_return_data, "$.data.name")
        check.equal(TestEmergency.data_emerge_log_name, emerge_log_14_name,
                    f"预期和实际不一致 预期状态码{TestEmergency.data_emerge_log_id}和实际状态码{emerge_log_14_name}")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")

    @allure.title("15.web端--结束应急预案")
    @pytest.mark.smoke
    # @pytest.mark.run(order=15)
    def test_emergency_15(cls):
        # 更新用例 需要结束的ID
        update_data(database="testgroup", table_name="case_zhaotong", id=14, key="id",
                    value=TestEmergency.data_emerge_log_id[0])

        sql = "SELECT * FROM case_zhaotong  where  id =14"
        id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().all_api_requests(
            sql=sql)

        # 断言状态码
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        # 断言返回值
        check.equal(dict_expect_return_data, dict_return_data,
                    f"预期和实际不一致 预期返回值{dict_expect_return_data}和实际返回值{dict_return_data}不一致")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")

    @allure.title("16.web端--验证发起的应急预案已关闭")
    @pytest.mark.smoke
    # @pytest.mark.run(order=16)
    def test_emergency_16(cls):
        sql = "SELECT * FROM case_zhaotong  where  id =15"
        id, method, url, data, dict_expect_return_data, username, password, status_code, ig, real_status_code, dict_return_data = AllApis().all_api_requests(
            sql=sql)

        # 断言状态码
        check.equal(status_code, real_status_code, f"预期和实际不一致 预期状态码{status_code}和实际状态码{real_status_code}")
        # 断言id
        emerge_log_id_16 = jsonpath.jsonpath(dict_return_data, "$.data[0].id")
        check.equal(TestEmergency.data_emerge_log_id, emerge_log_id_16,
                    f"预期和实际不一致 预期返回值{TestEmergency.data_emerge_log_id}和实际返回值{emerge_log_id_16}不一致")
        # 断言状态status 1 进行中 2已关闭
        status = 2
        emerge_log_status_16 = jsonpath.jsonpath(dict_return_data, "$.data[0].status")[0]
        check.equal(status, emerge_log_status_16, f"预期和实际不一致 预期返回值{status}和实际返回值{emerge_log_status_16}不一致")
        log.debug(
            f" \n url:{url}\n 请求参数: {data}\n 账号：{username}\n 密码：{password}\n 预期状态码{status_code}\n 实际返回状态码: {real_status_code}\n 预期返回值：{dict_expect_return_data}\n 实际返回值: {dict_return_data} ")


if __name__ == '__main__':
    # pytest.main(["-sv", "test_emergency.py"])
    pytest.main(["-sv", "test_emergency.py::TestEmergency::test_emergency_01"])
    # os.system("pytest -vs ./test_register_login.py --alluredir ../report/temp_jsonreport")

    # 若想使用pycharm的pytest框架 还能生成报告 在对应目录下 命令行执行 allure generate  ../report/temp_jsonreport -o ../report/html --clean
    # os.system(
    #     "allure generate  ../report/temp_jsonreport -o ../report/html --clean")

    os.system(
        "allure generate  ../report/temp_jsonreport -o ../report/html --clean")

    # os.system("copy ../environment.properties ../report/temp_jsonreport/environment.properties")
# 生成一个网址来访问测试报告 当然浏览器直接访问 html/index.html文件也是可以的
# os.system("allure open html -h 0.0.0.0 -p 8889")

# os.system("allure open ../report/html")
