# # from websocket import create_connection
# # name = "ws://183.224.113.211:9001/api/ws?Authorization=Bearer%20eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcmVhX2NvZGUiOiI1MzA2IiwiZnVsbG5hbWUiOiJlV3A2ZVE9PSIsImlhdCI6MTY2NTQ4MDU3MCwiaW5zdGFuY2VfaWQiOjEwNCwibWVtYmVyX2lkIjoxMiwib3JnX2RlcHRfaWQiOjExNCwib3JnX2lkIjoxMTQsInBsYXRmb3JtX2lkIjoxLCJwb3NpdGlvbl9pZCI6MTExLCJyb2xlX2lkIjoxOCwicm9sZV90eXBlIjoyLCJzdWIiOjEyfQ.mwKQQTYOWadOuiZz-xVaX0RQfqVqmlg3oRA5Sr2heY0&platform=zt"
# # ws = create_connection(name)
# # print("Sending 'Hello, World'...")
# # # ws.send("Hello, World")
# # print("Sent")
# # print("Receiving...")
# # result = ws.recv()
# # print("Received '%s'" % result)
# # ws.close()
#
# import websocket
# from threading import Thread
# import time
# import sys
# import json
#
#
# def on_message(ws, message):
#     print(message)
#
#
# def on_error(ws, error):
#     # print("my_error", error)
#     if error:
#         return False
#     else:
#         return True
#
#
# def on_close(ws):
#     print("### closed ###")
#
#
# def on_open(ws):
#     def run(*args):
#         a = {"route": "/room_enter", "room": "point_104"}
#         b = json.dumps(a)
#         # for i in range(3):
#
#         # send the message, then wait
#         # so thread doesn't exit and socket
#         # isn't closed
#         ws.send(b)
#         #     time.sleep(1)
#
#         # time.sleep(3)
#         ws.close()
#         print("Thread terminating...")
#
#     Thread(target=run).start()
#
#
# if __name__ == "__main__":
#     websocket.enableTrace(True)# 打开跟踪，查看日志
#     host = "ws://183.224.113.211:9001/api1/ws?Authorization=Bearer%20eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcmVhX2NvZGUiOiI1MzA2IiwiZnVsbG5hbWUiOiJlV3A2ZVE9PSIsImlhdCI6MTY2NTQ4MDU3MCwiaW5zdGFuY2VfaWQiOjEwNCwibWVtYmVyX2lkIjoxMiwib3JnX2RlcHRfaWQiOjExNCwib3JnX2lkIjoxMTQsInBsYXRmb3JtX2lkIjoxLCJwb3NpdGlvbl9pZCI6MTExLCJyb2xlX2lkIjoxOCwicm9sZV90eXBlIjoyLCJzdWIiOjEyfQ.mwKQQTYOWadOuiZz-xVaX0RQfqVqmlg3oRA5Sr2heY0&platform=zt"
#     ws = None
#     try:
#         ws = websocket.create_connection(host)
#     except Exception as e:
#         assert (101, ws.getstatus(), 'websocket连接错误')
#         raise e
#     # ws = websocket.WebSocketApp(host,
#     #                             on_message=on_message,
#     #                             on_error=on_error,
#     #                             )
#     # assert(101, ws.getstatus(), 'websocket连接错误')
#     # ws.on_open = on_open
#     # ws.run_forever()

import websocket
import pytest_check as check
from tools.log import log


def test():
    print("测试开始")
    url = "ws://183.224.113.211:9001/api/ws?Authorization=Bearer%20eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcmVhX2NvZGUiOiI1MzA2IiwiZnVsbG5hbWUiOiJlV3A2ZVE9PSIsImlhdCI6MTY2NTk5MTQ5NywiaW5zdGFuY2VfaWQiOjEwNCwibWVtYmVyX2lkIjoxMiwib3JnX2RlcHRfaWQiOjExNCwib3JnX2lkIjoxMTQsInBsYXRmb3JtX2lkIjoxLCJwb3NpdGlvbl9pZCI6MTExLCJyb2xlX2lkIjoxOCwicm9sZV90eXBlIjoyLCJzdWIiOjEyfQ.zhG99Oe5RL2KmdQnCq1DKsKk3BWzaQZCXDDN8MEyujE&platform=zt"
    # 创建链接
    client = websocket.create_connection(url)
    # data = """{"route":"/room_enter","room":"point_104"}"""
    # print(data)
    #
    # # 发送数据
    # client.send(data)
    # # 接收数据
    # client_recv = client.recv()
    # print(client_recv)

    data = """{"route":"/heartbeat"}"""
    # print(data)
    client.send(data)
    client_recv = client.recv()
    # print(client_recv)
    expect_data = """{"route":"/heartbeat","data":true}\n"""
    # 断开连接

    check.equal(client_recv, expect_data, f"预期和实际不一致 预期状态码{client_recv}和实际状态码{expect_data}")

    client.close()
    print("测试结束")
    log.debug(
        f" \n url:{url}\n 请求参数: {data}\n实际返回值: {client_recv}\n ")


if __name__ == '__main__':
    test()
