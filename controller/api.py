from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import threading

from controller.server import start, monitor_nodes
from controller.shared_state import nodes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/nodes")
def get_nodes():
    return [
        {"node_id": node_id,
         **node_data
        }
        for node_id, node_data in nodes.nodes.items()
    ]



@app.on_event("startup")
def startup_event():
    print("[STARTING] system booting...")
    threading.Thread(
        target=start,
        daemon=True
    ).start()

    threading.Thread(
        target=monitor_nodes,
        daemon=True
    ).start()
