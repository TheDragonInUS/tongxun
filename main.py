"""
主程序函数

"""
import socket
import threading


class UdpChat(object):
    def __init__(self):
        """
        创建udp_socket
        绑定端口和ip
        """
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp.bind(("", 1314))
        self.usr_list = []  # 维护的用户列表

    def broadcast(self, massage):
        """
        设置udp广播，发送上线通知
        :return:
        """
        self.udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.udp.sendto(massage.encode(
            'utf-8'), ('<broadcast>', 1314))

    def send_mas(self, ip_port):
        """
        设置ip和port 发送信息
        :param ip_port:
        :return:
        """

        while True:
            massage = input("\n请输入您要的信息：\n")
            if massage == "myself:exit":
                self.broadcast('BYE EVERYONE !\r\n')

                import os
                print(os.getpid())
                os.kill(os.getpid(), 9)

            massage = massage + "\r\n"
            self.udp.sendto(massage.encode(), ip_port)

    def pan_usr(self, ip):
        """
        判断用户是不是在用户列表中
        :param ip:
        :return:
        """
        if ip in self.usr_list:
            pass
        else:
            self.usr_list.append(ip)
        print(self.usr_list)

    def receive_mas(self):
        """
        接收信息并提取
        :return:
        """

        while True:
            massage = self.udp.recvfrom(2048)
            if massage[1][0] == "192.168.43.43":
                print("\n广播发送成功\n")
            else:
                # 判断用户是不是在用户列表中
                self.pan_usr(massage[1][0])
                print("接收发的消息是", massage[0].decode())

    def run(self):

        self.broadcast('hello I am coming!\r\n')
        send_mas_1 = threading.Thread(
            target=self.send_mas, kwargs={
                "ip_port": (
                    "192.168.43.233", 1314)})
        receive_mas_2 = threading.Thread(target=self.receive_mas)

        send_mas_1.start()
        receive_mas_2.start()


if __name__ == '__main__':

    a = UdpChat()
    a.run()
