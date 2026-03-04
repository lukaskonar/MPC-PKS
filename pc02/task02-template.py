import socketserver

# Mix TCPServer class with the threading functionality
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class MyTCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        try:
            print("[{}]: open".format(self.client_address[0]))
            self.wfile.write(b"--- PKS server ---\r\n")
            
            while True:
                line = self.rfile.readline()
                if not line: #client closed the connection
                    break
                    
                sline = line.rstrip().upper()
                print("[{}]: RX: {}".format(self.client_address[0], sline))
                
                #command processing
                match sline:
                    case b'HELP' | b'?':
                        self.wfile.write(b"commands:\r\n")
                        self.wfile.write(b" help\r\n")
                        self.wfile.write(b" quit\r\n")
                    case b'ID':
                        self.wfile.write(b" 247398\r\n")
                    case b'PC':
                         self.wfile.write(b" 32\r\n")
                    case b'QUIT':
                        self.wfile.write(b"Goodbye\r\n")
                        return
                        
        except Exception as e:
            print("[{}]: ER: {}".format(self.client_address[0], e))
            print("[{}]: disconnected".format(self.client_address[0]))
    
    
if __name__ == "__main__":
    HOST, PORT = "", 50000
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever() #can be terminated by Ctrl-C