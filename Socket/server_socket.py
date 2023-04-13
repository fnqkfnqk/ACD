from socket import *
from _thread import *

################################
###  단말기, 라즈베리파이 번호 할당 ###
################################
#------------------------------------------------------------#
RASP = 1001
ANDORID = 1002
#------------------------------------------------------------#

# 서버 IP 주소, 연결 포트 #
#------------------------------------------------------------#
host = "ec2-3-36-94-18.ap-northeast-2.compute.amazonaws.com"
port = 9000
#------------------------------------------------------------#

# 클라이언트 소켓 정보를 저장하는 리스트 #
#------------------------------------------------------------#
client_list = []
#------------------------------------------------------------#

# 서버 소켓 생성 #
#------------------------------------------------------------#
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1024)
serverSocket.bind((host, port))
serverSocket.listen(1)
#------------------------------------------------------------#

###########################
###  클라이언트의 소켓 생성  ###
###########################
# 1. 서버에 클라이언트가 접속할 때마다 소켓 생성 후 리스트에 정보 저장
#------------------------------------------------------------#
def client_socket(connectionSocket, addr):

    while True:
        try:
            # 데이터 수신
            data = connectionSocket.recv(1024)

            data_ = data.decode('utf-8')
            print("--------------------------------")
            print("sendclient: ", connectionSocket)
            print("receive data: ", data_)
            print("--------------------------------")

            """
            # 서버에 접속한 클라이언트들에게 채팅 보내기
            # 메세지를 보낸 본인을 제외한 서버에 접속한 클라이언트에게 메세지 보내기
            for client in client_list :
                if client != client_list :
                    client.send(data)
            """
        except ConnectionResetError as e:
            break

    # 클라이언트 연결 종료 시 리스트에서 정보 삭제
    if client_socket in client_list :
        client_list.remove(client_socket)

    client_socket.close()
#------------------------------------------------------------#



try:
    while True:
        print("<< READY TO CONNECT >>")

        connectionSocket, addr = serverSocket.accept()
        client_list.append(connectionSocket) # 클라이언트 소켓 정보 리스트에 저장
        start_new_thread(client_socket, (connectionSocket, addr))

except Exception as e:
    print("Error: ", e)

finally:
    serverSocket.close()