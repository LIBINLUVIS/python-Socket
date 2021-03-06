import socket
import threading


PORT=5050
HEADER=64
FORMAT="utf-8"
DISCONNECT_MESSAGE="DISCONNECT"
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,adrr):
    print(f"[NEW CONNECTION]{adrr}connected.")
    connection=True
    while connection:
            msg_length=conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length=int(msg_length)
                msg=conn.recv(msg_length).decode(FORMAT)
                print(msg)
                conn.send("msg recived".encode(FORMAT))
                if msg==DISCONNECT_MESSAGE:
                    connection=False
                    print(f"[{adrr}]  {msg}")

    conn.close()
def start():
    server.listen()
    print(f"Server is listening on {SERVER}")
    while True:
        conn,adrr=server.accept()
        thread =threading.Thread(target=handle_client,args=(conn,adrr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")


print("Heyy the server started")
start()






