from socket import AF_INET, SOCK_STREAM, socket
from concurrent.futures import ThreadPoolExecutor
import sys, pdb, time

def server_handler(sock, client_addr):
    LF = "\n"
    print('Got connection from', client_addr)
    while True:
        msg = sock.recv(256)
        if 'KILL_SERVICE' in msg.decode('utf-8'):
            sock.close()
            return "exit"
        elif "HELO text"  in msg.decode('utf-8'):
            response = [
                "HELO text",
                "IP:"+client_addr,
                "Port:"+sys.argv[1],
                "StudentID:aa2d8671e0b9698d706dd81e9fdf63205dcaa89b2926e5df2ec7a594b66861ba",
                ""
                ]
            socket.sendall(LF.join(response))
            sock.close()
        else:
            print(msg)
    print('Client closed connection')
    sock.close()

def server(port):
    pool = ThreadPoolExecutor(5)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(port)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        result = pool.submit(server_handler, client_sock, client_addr)
       	if result.result() == "exit":
            print("Killing service")
            sys.exit()
server(('',int(sys.argv[1])))
