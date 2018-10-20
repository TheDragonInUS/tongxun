"""
主程序

"""
import socket


def borad_(udp):
    udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    udp.sendto('Client broadcast message!\n'.encode('utf-8'), ('<broadcast>', 1314))


def send_mas(udp, massage, ip_port):
    udp.sendto(massage.encode(), ip_port)


def reci_mas(udp):
    massage = udp.recvfrom(2048)
    if massage[1][0] == "192.168.43.43":
        print("广播发送成功")
        return
    print(massage)


def run():

    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind(("", 1314))
    borad_(udp=udp)

    while True:

        print("ok")
        send_mas(
            udp=udp,
            massage="this is python",
            ip_port=(
                "192.168.43.233",
                1314))
        reci_mas(udp=udp)
        import time
        time.sleep(1)


run()
