import os, sys, thread, socket, pdb

def main():
    port = 8080
    host = ''               
   # print "Proxy Server Running on ",host,":",port
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        s.bind((host, port))

        s.listen(50)
    
    except socket.error, (value, message):
        if s:
            s.close()
        print "Could not open socket:", message
        sys.exit(1)

    while 1:
        conn, client_addr = s.accept()
       
        thread.start_new_thread(server_handler, (conn, client_addr))
        
    s.close()
      

def server_handler(conn, client_addr):
   
    request = conn.recv(4096) 
    conn.close()
    sys.exit(1)
        
if __name__ == '__main__':
    main()
