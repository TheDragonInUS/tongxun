"""
主程序口

"""

import socket
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(("", 1314))
udp.sendto("hello".encode(), ("192.168.43.233", 1314))
massage = udp.recvfrom(1024)
print(massage[0].decode())

