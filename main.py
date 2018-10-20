"""
主程序函数

"""
import socket
import threading


def borad_(udp):
    udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    udp.sendto('Client broadcast message!\n'.encode(
        'utf-8'), ('<broadcast>', 1314))


def send_mas(udp, ip_port):
    while True:
        massage = input("\n请输入您要的信息：\n")
        udp.sendto(massage.encode(), ip_port)


def reci_mas(udp):
    while True:
        massage = udp.recvfrom(2048)
        if massage[1][0] == "192.168.43.43":
            print("\n广播发送成功\n")
        else:
            print("接收发的消息是", massage[0].decode())


def run():

    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind(("", 1314))
    borad_(udp=udp)

    send_mas_1 = threading.Thread(target=send_mas, kwargs={"udp": udp, "ip_port": ("192.168.43.233", 1314)})
    reci_mas_2 = threading.Thread(target=reci_mas, kwargs={"udp": udp})

    send_mas_1.start()
    reci_mas_2.start()


run()


