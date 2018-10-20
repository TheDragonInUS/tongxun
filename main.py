"""
主程序

"""


def send_mas(udp, massage, ip_port):
    udp.sendto(massage.encode(), ip_port)


def reci_mas(udp):
    massage = udp.recvfrom(2048)
    print(massage)


def run():
    import socket
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind(("", 1314))

    while True:

        print("ok")
        send_mas(udp=udp, massage="this is python", ip_port=("192.168.43.233", 1314))
        reci_mas(udp=udp)
        import time
        time.sleep(1)

run()