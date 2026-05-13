import time
from sensor import read_sensor

def build_telemetry(node_id):
    return {
        "type": "telemetry",
        "node_id": node_id,
        "timestamp": time.time(),
        **read_sensor()
    }

def build_disconnect(node_id):
    return {
        "type": "disconnect",
        "node_id": node_id,
        "timestamp": time.time(),
    }

def build_heartbeat(node_id):
    return {
        "type": "heartbeat",
        "node_id": node_id,
        "timestamp": time.time(),
    }