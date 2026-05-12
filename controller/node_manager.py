
import time
class NodeManager:
    def __init__(self):
        self.nodes = {}

    def update_node(self, node_id, telemetry):
        if node_id not in self.nodes:
            self.nodes[node_id] = {}
        
        self.nodes[node_id]['latest'] = telemetry
        self.nodes[node_id]['last_seen'] = time.time()