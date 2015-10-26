from socket import AF_INET, SOCK_STREAM, gethostname, gethostbyname, socket
from concurrent.futures import ThreadPoolExecutor
import sys, pdb, time

def server_handler(sock, client_addr):
    LF = "\n"
    print('Got connection from', client_addr)

    msgbytes = sock.recv(256)
    msg = msgbytes.decode('utf-8')
    if 'KILL_SERVICE' in msg:
        sock.close()
        return "exit"
    elif "HELO"  in msg:
        response = [
            "IP:"+gethostname(),
            "Port:"+sys.argv[1],
            "StudentID:aa2d8671e0b9698d706dd81e9fdf63205dcaa89b2926e5df2ec7a594b66861ba",
            ]
        fullResponse = (msg + LF.join(response))
        sock.send(fullResponse.encode('utf-8'))
    else:
        print(msg)
    print('Client closed connection')
    sock.close()

def server(port):
    pool = ThreadPoolExecutor(8)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((gethostname(), port))
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        result = pool.submit(server_handler, client_sock, client_addr)
       	if result.result() == "exit":
            print("Killing service")
            sys.exit()
server(int(sys.argv[1]))
