from socket import AF_INET, SOCK_STREAM, gethostname, gethostbyname, socket
from select import select
from concurrent.futures import ThreadPoolExecutor
import sys, pdb, time
import messages


class ChatRoom:
    def __init__(self):
        self.name = name
        self.ref = ref
        self.users = []

class ChatServer:
    def __init__(self, port):
        self.port = port
        self.connections = []

    def _route_message(self, conn, data):
        print("Routing message: " + repr(data))

        try:
        if data[:13] == "JOIN_CHATROOM":
          self.client_join_chatroom(conn, data)

        elif data[:14] == "LEAVE_CHATROOM":
          self.client_leave_chatroom(conn, data)

        elif data[:4] == "CHAT":
          self.client_sent_message(conn, data)

        elif data[:] == "DISCONNECT":
          self.client_disconnect(conn, data)

        else:
          self.client_error(conn, error_codes.BAD_MESSAGE, "Couldn't parse message")

        except Exception as e:
            self.client_error(conn, error_codes.SERVER, e.message)

    def client_join_chatroom(self, conn, data):
        print("Client joined chatroom")
f
        message = messages.JOINED_CHATROOM_MESSAGE.format(
        chatroom=None,
        server_ip=None,
        server_port=None,
        room_ref=None,
        client_id=None
        )
        conn.sendall(message)

    def client_leave_chatroom(self, conn, data):
        print("Client leaves chatroom")

        message = messages.LEAVE_CHATROOM_MESSAGE.format(
        room_ref=None,
        client_id=None
        )
        conn.sendall(message)

    def client_disconnect(self, conn, data):
        print("Client disconnected")
        conn.close()

    def client_sent_message(self, conn, data):
        print("Client sent message")


    def client_error(self, conn, code, reason):
        print("Client error %d: %s" % (code, reason))

        message = messages.ERROR_MESSAGE.format(
        code=code,
        reason=reason
        )
        conn.sendall(message)

    def _new_connection(self):
        client_sock, client_addr = self.sock.accept()
        self.connections.append(client_sock)
        self.pool.submit()



    def server_handler(self, sock, client_addr):
        LF = "\n"
        print('Got connection from', client_addr)

        msgbytes = sock.recv(512)
        msg = msgbytes.decode('utf-8')
        if 'KILL_SERVICE' in msg:
            sock.close()
            return "exit"
        elif msg[:4] == "HELO"
            response = [
                "IP:"+gethostname(),
                "Port:"+sys.argv[1],
                "StudentID:aa2d8671e0b9698d706dd81e9fdf63205dcaa89b2926e5df2ec7a594b66861ba",
                ]
            fullResponse = (msg + LF.join(response))
            sock.send(fullResponse.encode('utf-8'))
        else:
            self._route_message()
        print('Closed connection')
        sock.close()

    def server(self):
        self.pool = ThreadPoolExecutor(8)
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind((gethostname(), self.port))
        self.sock.listen(5)
        while True:
            try:
                read_sockets, write_sockets, error_sockets = select.select(self.connections + [self.sock],[],[])
                for sock in read_sockets:
                    if sock is self.sock:
                        self._new_connection()
                    else:
                        self._dispatch_thread(self._process_message, sock)
            except Exception, e:
                raise
            client_sock, client_addr = self.sock.accept()
            result = self.pool.submit(self.server_handler, client_sock)
           	if result.result() == "exit":
                print("Killing service")
                sys.exit()


def main():
    server = ChatServer(int(sys.argv[1]))
    server.server()
if __name__ == "__main__":
    main()