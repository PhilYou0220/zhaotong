from tools.log import log
from tools.read_config import read_config, read_yaml


class ParseData(object):
    def parse_data(self, case):
        my_config = read_config()
        # try:
        # url_web_prefix = 'http://192.168.101.184:8000'  # 测试环境web前缀
        # url_mobile_prefix = "http://192.168.101.184:8001"  # 测试环境手机前缀
        # url_web_prefix = 'http://192.168.101.116:8004'  # 测试环境web前缀
        url_web_prefix = my_config["zhaotong_test"]["url_web_prefix"]
        # url_mobile_prefix = "http://192.168.101.116:8001"  # 测试环境手机前缀
        url_mobile_prefix = my_config["zhaotong_test"]["url_mobile_prefix"]
        id = case["id"]
        method = case["method"]
        type = case["type"]
        url = None
        if type == 1:
            url = url_web_prefix + case["url"]
        elif type == 2:
            url = url_mobile_prefix + case["url"]
        else:
            log.error("错误的的类型，非手机端或者web端")
        data = case["data"]
        expect_return_data = case["expect_return_data"]
        username = case["username"]
        password = case["password"]
        status_code = case["status_code"]
        name = case["name"]
        case_step = case["case_step"]
        return id, method, url, data, expect_return_data, username, password, status_code, name, case_step, type

    def mq_parse_data(self, case):
        id = case["id"]
        method = case["method"]
        url = case["url"]
        data = case["data"]
        expect_return_data = case["expect_return_data"]
        username = case["username"]
        password = case["password"]
        status_code = case["status_code"]
        name = case["name"]
        case_step = case["case_step"]
        return id, method, url, data, expect_return_data, username, password, status_code, name, case_step

    def yaml_parse_data(self, filename: str, api_name: str, case_index: int):
        my_config = read_config()
        yaml_data = read_yaml(filename)
        url_web_prefix = my_config["zhaotong_test"]["url_web_prefix"]
        url_mobile_prefix = my_config["zhaotong_test"]["url_mobile_prefix"]
        method = yaml_data[api_name][case_index]["method"]
        type = yaml_data[api_name][case_index]["type"]
        url = None
        if type == 1:
            url = url_web_prefix + yaml_data[api_name][case_index]["url"]
        elif type == 2:
            url = url_mobile_prefix + yaml_data[api_name][case_index]["url"]
        else:
            log.error("错误的的类型，非手机端或者web端")
        data = yaml_data[api_name][case_index]["data"]
        # expect_return_data = case["expect_return_data"]
        username = yaml_data[api_name][case_index]["username"]
        password = yaml_data[api_name][case_index]["password"]
        status_code = yaml_data[api_name][case_index]["status_code"]
        title = yaml_data[api_name][case_index]["title"]

        return method, url, data, username, password, status_code, type, title


pd = ParseData()
if __name__ == '__main__':
    a = ParseData().yaml_parse_data()
