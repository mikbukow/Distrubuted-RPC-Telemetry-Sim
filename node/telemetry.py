import time
from sensor import read_sensor, disconnect_sensor

def build_telemetry(node_id):
    return {
        "node_id": node_id,
        "timestamp": time.time(),
        **read_sensor()
    }


def build_disconnect(node_id):
    return {
        "node_id": node_id,
        "timestamp": time.time(),
        **disconnect_sensor()
    }