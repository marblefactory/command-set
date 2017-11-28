import socket
import sys


class Client():
    def __init__(self, HOST='127.0.0.1', PORT=9999):
        self.HOST = HOST
        self.PORT = PORT

    def _wrap(message: str):
        """
        Wraps the message in the appropriate envolope for sending.
        eg:
            messsage$END
        """
        # TODO What wrapper do I need?
        return message+"$"

    def send(message:str, stateless=True):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.HOST, self.PORT))
            sock.sendall(bytes(_wrap(data), "utf-8"))
            if not stateless:
                return str(sock.recv(1024, "utf-8"))
