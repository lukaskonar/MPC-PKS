import socketserver

# Constants
LISTEN_IP = "0.0.0.0"
LISTEN_PORT = 50000

# Mix TCPServer class with the threading functionality
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class ConnectionHandler(socketserver.StreamRequestHandler):
    # This function is called for every new connection
    def handle(self):
        clientIP, clientPort = self.client_address
        print(f"New client {clientIP}:{clientPort} connected")

        while True:
            try:
                data = self.request.recv(1024)
                if not data:
                    # If the data variable is empty, it means that the client disconnected
                    print(f"Client {clientIP}:{clientPort} disconnected")
                    break # Exit the loop

                # Send back the modified data to the client
                response_data = data.upper()+b"|"
                self.request.sendall(response_data)
                print(f"{clientIP}:{clientPort} - {data}->{response_data}")

            except Exception as e:
                print(f"Client {clientIP}:{clientPort} connection lost")
                break # Exit the loop

# Start of the code
if __name__ == "__main__":
    server = ThreadedTCPServer((LISTEN_IP, LISTEN_PORT), ConnectionHandler)
    print(f"Listening on TCP port {LISTEN_PORT}")
    server.serve_forever()