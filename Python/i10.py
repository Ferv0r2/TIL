import socket

class WebServer:
    def __init__(self, port):
        self.port = port

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind("0.0.0.0", self.port)

        self.server = server

        server.listen()

        while True:
            client, addr = server.accept()

            raw = client.recv(8000)
            data = raw.decode('utf-8')

            if data.startswith("GET /hello HTTP1.1") == True:
                file = open("hello.html", "r")
                html = file.read()
                file.close()

                print(html)

                response = "HTTP/1.1 200 OK\r\nContents Length: {}\r\n\r\n{}".format(len(html.encode('utf-8'))), html
                client.send(response)
                print("굿")
            else:
                print("error")

            client.close()

my = WebServer(8888)