##############################
###  라즈베리파이 서버 소켓 연결  ###
##############################

from socket import *
from _thread import *
import time
#import serial   # 아두이노 시리얼 통신을 위한 라이브러리
# 난수 생성
import random

# 라즈베리파이 번호 할당
RASP = 1001

# 서버 ip 주소 및 포트 번호
host_ip = 'ec2-13-125-228-114.ap-northeast-2.compute.amazonaws.com'
port_ip = 9000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((host_ip, port_ip))

def recv_data(client_socket):
    while True :
        data = client_socket.recv(1024)

        print("recv data: ", data.decode())
        
        if data.decode() == 'quit':
            client_socket.close()

#start_new_thread(recv_data, (clientSocket, ))

clientSocket.send(str(RASP).encode('utf-8'))

while True:
    #for _ in range(5):
    num = random.randint(1,101)
    clientSocket.send(str(num).encode('utf-8'))
    time.sleep(0.1)
