import yaml
from tools.project_path import CONFIGYAMLDIR

def read_config():
    with open(file=CONFIGYAMLDIR, mode="r", encoding="utf8") as f:
        my_config = yaml.load(f, Loader=yaml.FullLoader)
        # print(my_config)
    # print(my_config["zhaotong_test"]["url_web_prefix"])
    return my_config


def read_yaml(filename):
    with open(file=filename, mode="r", encoding="utf8") as f:
        yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        # print(my_config)
    # print(my_config["zhaotong_test"]["url_web_prefix"])
    return yaml_data


if __name__ == '__main__':
    a = read_yaml("../testcase_api_yaml/test_015_beacon_alert_count_by_type.yml")
    print(a)
    # print(a["top_count2"][0], type(a["top_count2"][0]))  # {'status': [1, 2, 3, 4, 5]} <class 'dict'>
