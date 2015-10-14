# Title: Lab1 echo server

import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8000))
request = [
    "GET /echo.php?message=hello HTTP/1.1",
    "",
    "",]
CRLF = "\r\n"
print CRLF.join(request)
client_socket.send(CRLF.join(request))
data = client_socket.recv(256)
print data
client_socket.close()

