export interface Metrics {
    cpu_usage: number;
    temperature: number;
}

export interface NodeMessage {
    type: string;
    node_id: string;
    timestamp: number;
    metrics?: Metrics;
}

export interface NodeState {
    node_id: string;
    created: number;
    status: "alive" | "dead";
    latest: NodeMessage;
    last_seen: number;
}