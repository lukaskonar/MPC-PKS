import socket
import struct
import time

# Adresa a port serveru
host = "147.229.150.222"
port = 50000


id_val = 247398
pc_val = 32

file = "udp.log"


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.settimeout(2)  # nastavení timeoutu

for i in range(5):
    seq = i+1
    msg = struct.pack("!LLL", seq, id_val, pc_val)

    udp_socket.sendto(msg, (host, port))
    print("Odesláno: seq={}, id={}, pc={}".format(seq, id_val, pc_val))


    try:
        data, address = udp_socket.recvfrom(512)
        Rseq, Rn1, Rn2 = struct.unpack("!LLL", data)

    except TimeoutError:
        print("No response from server")

    except struct.error:
        print("Unable to unpack packet from {}".format(address))

    else:
        log = "Received: a={}, p={}, s={}, n1={}, n2={}".format(
            address[0], address[1], Rseq, Rn1, Rn2
        )
        print(log)

        fo = open(file, "a")
        fo.write(log + "\n")
        fo.close()

        time.sleep(0.5)

# Uzavření socketu
udp_socket.close()
print("Socket uzavřen")
