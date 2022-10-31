# """ 2.1 conftest.py文件名不能修改
#         conftest.py文件中存放项目所有的fixture
#         方便对fixture管理和维护
#     2.2 在conftest.py定义函数
#         在函数前添加@pytest.fixture()装饰器
#         在测试用例的函数中传入fixture标识的函数名。
# 提示：conftest.py文件放在项目的根目录，作用域是全局的。
#     conftest.py文件放在某一个包下，作用域只在该包内。
# """
# import pytest
# from tools.DB import db2, db3
#
#
#
# @pytest.fixture(scope="class")
# def non_directory_car():
#     # 删除联单、告警、车辆进出数据
#     del_ticket_sql = """DELETE FROM ss_electric_ticket WHERE created_time BETWEEN CURDATE() AND FROM_UNIXTIME((UNIX_TIMESTAMP(ADDDATE(CURDATE(), INTERVAL 1 DAY))-1)) AND (start_id in (14341,260,779) or end_id in (14341,260,779));"""
#     db2.delete(del_ticket_sql)
#     del_alarm_sql = """DELETE FROM alarm_dog WHERE create_time BETWEEN UNIX_TIMESTAMP(CURDATE()) AND UNIX_TIMESTAMP(ADDDATE(CURDATE(), INTERVAL 1 DAY))-1) AND instance_id in (14341,260,779) AND area_id=24;"""
#     db2.delete(del_alarm_sql)
#     del_car_inout_sql = """DELETE from car_inout_data WHERE door_id IN (SELECT id FROM building_door WHERE area_id=24) AND create_time  BETWEEN UNIX_TIMESTAMP(CURDATE()) AND UNIX_TIMESTAMP(ADDDATE(CURDATE(), INTERVAL 1 DAY))-1);"""
#     db2.delete(del_car_inout_sql)
#     # 启用锦江区测试固定源
#     up_building_sql = """UPDATE building SET deleted=0 WHERE id in (14341);"""
#     db2.update(up_building_sql)
#     up_sand_factory_sql = """UPDATE sand_factory SET deleted=0 WHERE id in (260);"""
#     db2.update(up_sand_factory_sql)
#     up_consum_sql = """UPDATE consum SET deleted=0 WHERE id in (779);"""
#     db2.update(up_consum_sql)
#     # 启用锦江区测试固定源摄像头
#     up_camare_sql="""UPDATE `building_door` SET deleted=0 WHERE area_id=24;"""
#     db2.update(up_camare_sql)
#     yield print("非名录车前置条件执行完成")
#
#     print("正在恢复数据库默认设置")
#     # # 删除联单、告警、车辆进出数据
#     # del_ticket_sql1 = """DELETE FROM ss_electric_ticket WHERE created_time BETWEEN CURDATE() AND FROM_UNIXTIME((UNIX_TIMESTAMP(ADDDATE(CURDATE(), INTERVAL 1 DAY))-1)) AND (start_id in (14341,260,779) or end_id in (14341,260,779));"""
#     # db2.delete(del_ticket_sql1)
#     # del_alarm_sql1 = """DELETE FROM alarm_dog WHERE create_time BETWEEN UNIX_TIMESTAMP(CURDATE()) AND UNIX_TIMESTAMP(ADDDATE(CURDATE(), INTERVAL 1 DAY))-1) AND instance_id in (14341,260,779) AND area_id=24;"""
#     # db2.delete(del_alarm_sql1)
#     # del_car_inout_sql1 = """DELETE from car_inout_data WHERE door_id IN (SELECT id FROM building_door WHERE area_id=24) AND create_time  BETWEEN UNIX_TIMESTAMP(CURDATE()) AND UNIX_TIMESTAMP(ADDDATE(CURDATE(), INTERVAL 1 DAY))-1);"""
#     # db2.delete(del_car_inout_sql1)
#     # 禁用锦江区测试固定源
#     up_building_sql1 = """UPDATE building SET deleted=1 WHERE id in (14341);"""
#     db2.update(up_building_sql1)
#     up_sand_factory_sql1 = """UPDATE sand_factory SET deleted=1 WHERE id in (260);"""
#     db2.update(up_sand_factory_sql1)
#     up_consum_sql1 = """UPDATE consum SET deleted=1 WHERE id in (779);"""
#     db2.update(up_consum_sql1)
#     # 禁用锦江区测试固定源摄像头
#     up_camare_sql1 = """UPDATE `building_door` SET deleted=1 WHERE area_id=24;"""
#     db2.update(up_camare_sql1)
#     print("已恢复数据库默认设置，已删除生成的联单、告警、车辆进出图片")
#
