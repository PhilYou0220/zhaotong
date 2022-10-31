# # import  json
# # a={"code": 200, "message": "ok", "data": {
# #     "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTQ5OTg2NzIsImZ1bGxuYW1lIjoi5bqU5oCl5LiT5ZGYIiwiaWF0IjoxNjU0OTk4NjEyLCJwaG9uZSI6IjEyMyIsInNpZ25hdHVyZSI6ImQzYzFjYjFhLWRmMmEtNDVmOS05Y2MwLWFhZDAwMzY0ODY3ZSIsInN1YiI6MTJ9.YyvXKi8-kBvY-nty2axFs46Q_X7NDQXOKiB2bpjAQDg"},
# #  "status": "", "request_id": ""}
# #
# # print(a["data"]["token"])
# # resp = None
# # print(hash(resp))
#
# # import requests
# # r = requests.get(url="https://slack.com/intl/zh-cn/")
# # print(r.text)
#
# # a = {"schedule_department": "47", "allow_enable_department": "47", "allow_enable_user": "85",
# #      "files": [{"url": "file/0/2022/0610/9afede02-e56f-43c5-8de3-9e040270974e.jpg", "name": "123"}],
# #      "name": "test_应急预案", "case_type": 2}
#
#
# import jsonpath
# import json
#
# #
# # print(type(a))
# # data = jsonpath.jsonpath(a, "$.name")
# # print(data)
# #
# # # d = {"a": "1", "b": "$"}
# # d = {k: v.replace("$", "2") for k, v in d.items()}
# # print(d)
# #
# # e = jsonpath.jsonpath(d, "$.a")
# # print(e)
#
# # import jsonpath
# # import json
# # from tools.DB import db3, emerg
# # sql = "SELECT data FROM case_zhaotong  where  id =1"
# # data=db3.select_real(sql)
# # print(data[0][0])
# # verify_data = jsonpath.jsonpath(json.loads(data[0][0]), "$.name")
# # print(verify_data)
# # del_sql1 = f"DELETE from emerg_case WHERE name=\"{verify_data[0]}\""
# # emerg.delete(del_sql1)
#
# # import jsonpath
# # #
# # b = {"code": 200, "message": "ok", "data": [
# #     {"id": 85, "name": "一级应急预案", "schedule_department": "行政部,运维部,运维1部", "allow_enable": "行政部,行政部,行政部,行政部,行政部,行政部,应急专员",
# #      "files": [{"name": "123", "url": "file/0/2022/0609/cb0e85b3-a760-4042-a8e1-4f9e3c4b7c25.jpg"}]},
# #     {"id": 86, "name": "二级应急预案", "schedule_department": "行政部,运维部,运维1部,运维2部",
# #      "allow_enable": "行政部,行政部,行政部,行政部,行政部,行政部,82",
# #      "files": [{"name": "123", "url": "file/0/2022/0610/e83633e8-a80d-484a-a610-1e5e9dce1454.jpg"}]},
# #     {"id": 87, "name": "三级应急预案", "schedule_department": "行政部,行政部,行政部,行政部",
# #      "allow_enable": "行政部,行政部,行政部,行政部,行政部,行政部,wy,wy,wy,wy",
# #      "files": [{"name": "123", "url": "file/0/2022/0610/e8a5f36e-304c-45ec-81f2-97c278eef111.jpg"}]},
# #     {"id": 93, "name": "test_应急预案", "schedule_department": "行政部,行政部,行政部,行政部",
# #      "allow_enable": "行政部,行政部,行政部,行政部,行政部,行政部,wy,wy,wy,wy",
# #      "files": [{"name": "123", "url": "file/0/2022/0610/9afede02-e56f-43c5-8de3-9e040270974e.jpg"}]},
# #     {"id": 94, "name": "test_应急预案", "schedule_department": "行政部,行政部,行政部,行政部",
# #      "allow_enable": "行政部,行政部,行政部,行政部,行政部,行政部,wy,wy,wy,wy",
# #      "files": [{"name": "123", "url": "file/0/2022/0610/9afede02-e56f-43c5-8de3-9e040270974e.jpg"}]},
# #     {"id": 95, "name": "test_应急预案", "schedule_department": "行政部,行政部,行政部,行政部",
# #      "allow_enable": "行政部,行政部,行政部,行政部,行政部,行政部,wy,wy,wy,wy",
# #      "files": [{"name": "123", "url": "file/0/2022/0610/9afede02-e56f-43c5-8de3-9e040270974e.jpg"}]}],
# #      "page": {"total": 6, "page": 1, "limit": 10}, "status": "", "request_id": ""}
# # data = jsonpath.jsonpath(b, "$.data[-1:].id")
# # print(data)
#
# # class A:
# #     def __init__(self):
# #         pass
# #
# #     def fun(self):
# #         self.a = 1
# #         print(self.__dict__)
# #         # print(cls.__dict__)
# #         print(A.__dict__)
# #
# #     def fuc(self):
# #         self.b = 2
#
# #         print(self.a)
# #         print(self.b)
# #         print(self.__dict__)
# #         # print(cls.__dict__)
# #         print(A.__dict__)
# #     def func(cls):
# #         cls.c=3
# #         print(cls.c)
# #         # print(self.__dict__)
# #         print(cls.__dict__)
# #         print(A.__dict__)
# #
# # a=A()
# # a.fun()
# # a.fuc()
# # a.func()
#
# # from string import Template
# # from tools.current_time_about import my_time
#
# # param_data = {
# #     "shoolcode": "广州大学",
# #     "classCode": "1班",
# #     "gradeCode": "一年级",
# #     "student_mb": "001"
# # }
# # param = '{"shoolcode":"${shoolcode}","classCode":"${classCode}", "gradeCode":"${gradeCode}","student_mb":"${student_mb}"}'
# # res = Template(param).substitute(param_data)
# # print(res)
# # from tools.update_data import update_data
# # from string import Template
# # import json
# #
# # temp = {"from": "${from}", "to": "${to}"}
# # str_temp = json.dumps(temp)
# # start = 1
# # to = 2
# # param = {"from": start, "to": to}
# # res = Template(str_temp).substitute(param)
# # real_res = json.loads(res)
# # print(type(real_res))
# # print(real_res)
#
# # import jsonpath
# #
# # a = {"code": 200, "message": "ok", "data": [
# #     {"id": 32, "name": "test_应急预案", "schedule_department": "47", "schedule_department_name": "",
# #      "created_at": "2022-06-10T07:08:17Z", "created_at_unix": 1654844897, "status": 1, "status_name": "进行中",
# #      "enable_user": 0, "user_name": ""},{"id": 33, "name": "test_应急预案"}], "page": {"page": 1, "limit": 20, "total": 7}, "status": "",
# #      "request_id": ""}
# # data_emerge_log_name = jsonpath.jsonpath(a, "$.data[0].id")
# # print(data_emerge_log_name)
#
# # import jsonpath
# #
# # a = {"code": 200, "message": "ok", "data": [
# #     {"schedule_department": "行政部,行政部,行政部", "name": "test_应急预案", "id": 59, "username": "", "status": 2,
# #      "active_instance": "昭通市永盛经贸有限公司", "end_at": "2022-06-23T09:18:15Z", "created_at": "2022-06-23T09:18:11Z"},
# #     {"schedule_department": "行政部,行政部,行政部", "name": "三级应急预案", "id": 33, "username": "", "status": 1,
# #      "active_instance": "昭通市昌峻虬宇建材有限公司", "end_at": "", "created_at": "2022-06-14T11:56:37Z"},
# #     {"schedule_department": "行政部,行政部,行政部", "name": "三级应急预案", "id": 30, "username": "", "status": 1,
# #      "active_instance": "昭通市林予商贸有限责任公司", "end_at": "", "created_at": "2022-06-10T02:57:42Z"},
# #     {"schedule_department": "行政部,运维部,运维1部,运维2部", "name": "二级应急预案", "id": 29, "username": "", "status": 1,
# #      "active_instance": "昭通市昭阳区丰岭建筑建材有限公司", "end_at": "", "created_at": "2022-06-10T02:29:54Z"},
# #     {"schedule_department": "行政部,行政部,行政部,行政部,运维部,运维部,运维部,运维部,运维1部,运维1部,运维1部,运维1部", "name": "一级应急预案", "id": 27,
# #      "username": "", "status": 1, "active_instance": "昭通市昭阳区博昌砂石料有限公司", "end_at": "",
# #      "created_at": "2022-06-10T01:59:51Z"},
# #     {"schedule_department": "行政部,行政部,行政部,行政部,运维部,运维部,运维部,运维部,运维1部,运维1部,运维1部,运维1部", "name": "一级应急预案", "id": 26,
# #      "username": "", "status": 1, "active_instance": "昭通万亩禾山农业科技有限公司", "end_at": "",
# #      "created_at": "2022-06-10T01:47:16Z"},
# #     {"schedule_department": "行政部,行政部,行政部,行政部,运维部,运维部,运维部,运维部,运维1部,运维1部,运维1部,运维1部", "name": "一级应急预案", "id": 25,
# #      "username": "", "status": 1, "active_instance": "昭通晟煌建材有限公司", "end_at": "", "created_at": "2022-06-09T14:24:43Z"},
# #     {"schedule_department": "行政部,行政部,行政部,行政部,运维部,运维部,运维部,运维部,运维1部,运维1部,运维1部,运维1部", "name": "一级应急预案", "id": 24,
# #      "username": "", "status": 1, "active_instance": "昭通市昭阳区丰岭建筑建材有限公司", "end_at": "",
# #      "created_at": "2022-06-09T13:40:39Z"},
# #     {"schedule_department": "运维部", "name": "其它应急预案", "id": 6, "username": "", "status": 1, "active_instance": "",
# #      "end_at": "", "created_at": "2022-05-30T09:03:45Z"}], "page": {"total": 9, "page": 1, "limit": 10}, "status": "",
# #      "request_id": ""}
# #
# # data_emerge_log_name = jsonpath.jsonpath(a, "$.data[0].status")[0]
# # print(data_emerge_log_name)
# # from tools.DB import emerg
# #
# # sql = f"SELECT * FROM emerg_case_receipt_log WHERE emerg_case_log_id=48"
# # res = emerg.select(sql)[0]["id"]
# # print(res)
#
# # import yaml
# # import jsonpath
# #
# # with open(file="../config.yml",mode="r",encoding="utf8") as f:
# #     my_config=yaml.load(f,Loader=yaml.FullLoader)
# #     # print(my_config)
# # print(my_config["zhaotong_test"]["url_web_prefix"])
# # # print(a)
#
# # from tools.current_time_about import my_time
# #
# # print(my_time.current_datetime()[0])
# #
# # class F:
# #     def __call__(self, *args, **kwargs):
# #         print('执行了__call__')
# #         self.fun()
# #
# #     def fun(self):
# #         print("fun")
# #
# #
# # f = F()
# # f()  # 执行 __call_
# # print(f.fun)
#
#
# # cars = [432, 4, 1, 43, 454]
# # # cars.sort()
# # # cars.reverse()
# # print(sorted(cars, reverse=True))
#
# # digitals = {
# #     'wuyu': 3,
# #     'tangjing': 8,
# #     'youfei': 5,
# #     'huangshuai': 1,
# #     'ningfei': 6
# # }
# # for digital in digitals.items():
# #     print(digital)
#
#
# # river = {"yellow": "china", "nile": "egypt"}
# #
# # for i in river.items():
# #     print(f"The {i[0]}  runs  through  {i[1]} ")
#
# # favorite_languages = {
# #     'jen': 'python',
# #     'sarah': 'c',
# #     'edward': 'ruby',
# #     'phil': 'python',
# # }
# # surveys = ['jen', 'wuyu', 'edward']
# # for name in surveys:
# #     if favorite_languages.get(name):
# #         print(f"thanks {name}")
# #     else:
# #         print(f"invite {name}")
# # num = 10
# # for i in range(num):
# #     print("i为:",i)
# #     num -= 1
# #     print("num为:",num)
# # # print(num)
# # my = '123123123'
# # print(my[0:2])
# # print(sum(list(i for i in range(1,101))))
# # print(list(i for i in range(1,101)))
# # print(sum(range(1,101)))
# # my_list = []
# # while True:
# #
# #     reuslt=
# #     if p_id !=0:
# #
# #     else:
# #         break
#
#
#
# import requests
# import jsonpath
# import requests
#
# headers = {
#     'Accept': '*/*',
#     'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
#     'Cache-Control': 'no-cache',
#     'Connection': 'keep-alive',
#     'Origin': 'http://221.237.182.174:8016',
#     'Pragma': 'no-cache',
#     'Referer': 'http://221.237.182.174:8016/',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
#     # Already added when you pass json=
#     # 'content-type': 'application/json',
#     'shomes-sign': '2de0a9dc900c14dc447c8efadc24c144',
#     'shomes-time': '1658389655',
#     'shomes-type': 'city_web',
#     'shomes-user': '47893',
# }
#
# json_data = {
#     'currDate': '2022-07-04',
# }
#
# response = requests.post('http://221.237.182.175:8016/web/new_dashboard/getCenterData', headers=headers, json=json_data, verify=False).json()
# # print(response)
# a = jsonpath.jsonpath(response, "$.buildingList")
# # print(a)
# my_list=[]
# for i in a[0]:
#     if i["is_working"]==1:
#         my_list.append(i["id"])
# print(my_list)

a = b"\x88\x82\xbdn\x15\xf5\xbe\x86"
b = a.decode("utf-8")
print(b)
