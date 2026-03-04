# UDP integer logger
import struct
import socket


DST_PORT = 50000 # The port number on which we will listen


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Use IPv4 and UDP
udp_socket.bind(("0.0.0.0", DST_PORT)) # Listen on all addresses and specified port
udp_socket.setblocking(0) # Set recvfrom() function to be non-blocking (the blocking was buggy on Windows)

print(f"Listening on UDP port {DST_PORT}")

while True:
    try:
        # Try to receive data from a client
        data, address = udp_socket.recvfrom(512)

        try:
            seq, n1, n2 = struct.unpack("!LLL", data)

        except struct.error:
            # Handle the case where we receive a malformed packet
            print("Unable to unpack packet from {}".format(address))
            # Print the received data to the console
            log = 'a = {}, p = {}, msg = {}'.format(*address, data)
        
        else:
            log = 'a = {}, p = {}, seq = {}, id = {}, pc = {}'.format(*address, seq, n1, n2)

        # Print and save the data to a file
        print(log)
        with open("02-log.txt", "a") as f:
            f.write(log+"\n")
        
    except BlockingIOError:
        # If no data are available to be received try again
        continue