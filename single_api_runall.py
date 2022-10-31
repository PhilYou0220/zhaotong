import pytest
import allure
import os

# pytest.main(["-sv", "./testcase_api/test_079_web_socket.py"])
pytest.main(["-sv", "./testcase_api"])
os.system(
    "allure generate  ./report/temp_jsonreport -o ./report/html --clean")
os.system("allure open ./report/html")
