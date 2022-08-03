import socket

class WebServer:
    def __init__(self, port):
        self.port = port

    def read(self, client):
        raw = client.recv(8000)
        data = raw.decode("utf-8")

        if data.startswith("GET /hello HTTP/1.1") == True:
            file = open("hello.html", "r")
            html = file.read()
            file.close()

            print(html)

            size = len(html.encode("utf-8"))

            response = f"HTTP/1.1 200 OK\n \
                Content-Length: {size}\n\n{html}".encode("utf-8")
                
            client.send(response)
            pass
        else:
            print("error")

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("0.0.0.0", self.port))

        self.server = server
        server.listen()

        while True:
            client, addr = server.accept()
            WebServer.read(self, client)

            client.close()

my = WebServer(8888)
my.start()