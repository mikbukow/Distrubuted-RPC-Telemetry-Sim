import socket
import threading
import json
from node_manager import NodeManager

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) # gets local ipv4 address
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

#TCP socket server 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
nodes = NodeManager()

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # blocking until we get a msg from the client
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f"[{addr}] {msg}")
            try:
                data = json.loads(msg)
            except json.JSONDecodeError:
                print(f'[ERROR] bad json from {addr}: {msg}')
                continue
            
            if data.get("type") == 'disconnect':
                connected = False
                continue

            nodes.update_node(data['node_id'], data)
    
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() # this is blocking
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting ... ")
start()
