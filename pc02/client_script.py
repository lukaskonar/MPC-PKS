import socket
import time
#adresa a port serveru
host = "147.229.150.222"
port = 50000

#vytvoreni socketu
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#otevrit kanal
tcp_socket.connect((host, port))


for i in range(5):
    #zaslani dat (odpoved je ukladana do bufferu)
    msg = "data" + str(i)
    tcp_socket.sendall(msg.encode('ascii'))


    data = tcp_socket.recv(1024)
    print(str(data, 'ascii'))

#uzavreni kanalu
tcp_socket.close()

