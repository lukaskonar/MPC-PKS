# UDP text logger
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
        
        # Print the received data to the console
        log = 'a = {}, p = {}, msg = {}'.format(*address, data)
        print(log)

        # Save the data to a file
        with open("01-log.txt", "a") as f:
            f.write(log+"\n")
        
    except BlockingIOError:
        # If no data are available to be received try again
        continue