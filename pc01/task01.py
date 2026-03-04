import socket
import struct
import time

#adresa a port prijemce (zada vyucujici)
host = "147.229.150.222"
port = 50000



#vytvoreni socketu
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(5):
    #vytvoreni zpravy
    seq = i+1
    id = 247398
    pc = 32
    msg = struct.pack("!LLL", seq, id, pc)
    n = udp_socket.sendto(msg, (host, port))
    print("Odeslano {} byte\n".format(n))
    time.sleep(0.5)

#uzavreni socketu
udp_socket.close()