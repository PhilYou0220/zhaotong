# 操作rabbitmq的包

import pika
import json

from tools.log import log
from tools.DB import db3
import allure

from tools.parse_data import pd


class RMQProducer:
    def __init__(self, username: str, password: str, host: str, port: int):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.credentials = pika.PlainCredentials(username=self.username, password=self.password)

    def mq_open(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host, port=self.port, credentials=self.credentials))
        self.channel = self.connection.channel()

    def mq_close(self):
        self.connection.close()

    def mq_use(self, sql: str):
        self.mq_open()

        result = db3.select(sql=sql)
        id, method, url, data, expect_return_data, username, password, status_code, *ig = pd.mq_parse_data(result[0])
        with allure.step(f"{ig[1]}"):
            b_body = data.encode("utf-8")
            # # 声明一个队列 没有就创建 不需要
            # self.my_queue = self.channel.queue_declare(queue=queue_name, durable=True)

            # 由于消息队列具有持久性 需保证能推出去
            try:
                self.channel.basic_publish(exchange="",
                                           routing_key=url,  # 消息队列名称
                                           body=b_body  # 需要字节格式
                                           )
            except Exception as e:
                log.error(e)

            self.mq_close()
        return url, data, expect_return_data,username


# rmq_iot_test = RMQProducer(username="root", password="nA0!kL1iX0.fF8xB5&sF9uZ7wY3", host="47.108.233.145", port=5673)
# rmq_iot_product = RMQProducer(username="root", password="nA0!kL1iX0.fF8xB5&sF9uZ7wY3", host="47.108.233.145", port=5672)
# rmq_business_test = RMQProducer(username="epuser", password="epuser@123", host="106.75.154.221", port=5672)
# rmq_business_product = RMQProducer(username="epuser", password="epuser@123-New", host="http://221.237.182.170/",
#                                    port=5672)
if __name__ == '__main__':
    # rmq_iot_test.mq_use()
    pass
