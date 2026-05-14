import socket
import json
import uuid
import time
import random

from node.telemetry import build_telemetry, build_disconnect, build_heartbeat

last_telemetry = 0
last_heartbeat = 0
TELEMETRY_INTERVAL = 10
HEARTBEAT_INTERVAL = 2

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) # gets local ipv4 address
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
NODE_ID = str(uuid.uuid4())

failure_roll = random.random()

if failure_roll < 0.01:
    FAILURE_MODE = "crash"
elif failure_roll < 0.03:
    FAILURE_MODE = "silent"
elif failure_roll < 0.06:
    FAILURE_MODE = "network_drop"
else:
    FAILURE_MODE = "none"


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

try:

    running = True

    while running:
        now = time.time()

        # ------ FAILURE CHECKS -------- 
        #simulating random disconnect
        if FAILURE_MODE == "crash":
            print("[NODE] Simulated crash/disconnect")
            client.close()
            break

        if FAILURE_MODE == "silent":
            print("[NODE] silent failure")
            while True:
                time.sleep(1000)

        if FAILURE_MODE == "network_drop":
            print("[NODE] network drop")
            client.shutdown(socket.SHUT_RDWR)
            client.close()
            break

        # -------------------------------
        # send heartbeat
        if now - last_heartbeat >= HEARTBEAT_INTERVAL:
            heartbeat = build_heartbeat(NODE_ID)
            send(json.dumps(heartbeat))
            last_heartbeat = now

        # send telemetry
        if now - last_telemetry >= TELEMETRY_INTERVAL:
            telemetry = build_telemetry(NODE_ID)
            send(json.dumps(telemetry))
            last_telemetry = now

        # packet loss simulation
        if FAILURE_MODE == "drop" and random.random() < 0.2:
            continue

        time.sleep(0.1) # small sleep to avoid CPU spin


except KeyboardInterrupt:
    running = False
    telemetry = build_disconnect(NODE_ID)
    send(json.dumps(telemetry))

finally:
    client.close()