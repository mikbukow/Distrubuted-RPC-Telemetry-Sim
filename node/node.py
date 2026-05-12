import socket
import json
import uuid
import time

from telemetry import build_telemetry, build_disconnect


HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) # gets local ipv4 address
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
NODE_ID = str(uuid.uuid4())


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

countdown = 10
while countdown > 0:
    telemetry = build_telemetry(NODE_ID)
    send(json.dumps(telemetry))
    time.sleep(5)
    countdown -= 1

telemetry = build_disconnect(NODE_ID)
send(json.dumps(telemetry))