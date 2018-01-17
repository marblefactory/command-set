import socketserver
import json


class BasicHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        # just send back the same data, but upper-cased
        j = json.loads(self.data[])
        print(json.dumps(j))
        self.request.sendall(self.data)



def start_server(HOST='127.0.0.1', PORT=9999):
    """
    Starts a server that will run forever unless interrupted with a Ctrl-C.
    """

    print("Starting server on " + HOST +":"+str(PORT))

    with socketserver.TCPServer((HOST, PORT), BasicHandler) as server:
        server.serve_forever()



if __name__ == "__main__":
    start_server('127.0.0.1', 9090)
