import time
import threading

class NodeManager:
    def __init__(self):
        self.nodes = {}
        self.lock = threading.Lock()

    def update_node(self, node_id, telemetry):
        now = time.time()

        with self.lock:
            if node_id not in self.nodes:
                self.nodes[node_id] = {
                    "created": now, 
                    "status": "alive"
                }
            
            self.nodes[node_id]["latest"] = telemetry
            self.nodes[node_id]["last_seen"] = now
            self.nodes[node_id]["status"] = "alive"