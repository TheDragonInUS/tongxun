"""
主程序函数

"""
import socket
import threading


class UdpChat(object):
    def __init__(self):
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp.bind(("", 1314))

    def broadcast(self):
        self.udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.udp.sendto('Client broadcast message!\n'.encode(
            'utf-8'), ('<broadcast>', 1314))

    def send_mas(self, ip_port):
        while True:
            massage = input("\n请输入您要的信息：\n")
            self.udp.sendto(massage.encode(), ip_port)

    def receive_mas(self):
        while True:
            massage = self.udp.recvfrom(2048)
            if massage[1][0] == "192.168.43.43":
                print("\n广播发送成功\n")
            else:
                print("接收发的消息是", massage[0].decode())

    def run(self):

        self.broadcast()
        send_mas_1 = threading.Thread(
            target=self.send_mas, kwargs={
                "ip_port": (
                    "192.168.43.233", 1314)})
        receive_mas_2 = threading.Thread(target=self.receive_mas)

        send_mas_1.start()
        receive_mas_2.start()


a = UdpChat()
a.run()
