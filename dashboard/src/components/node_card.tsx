import type { NodeState } from "../types";

interface Props {
  node: NodeState;
}

export default function NodeCard({ node }: Props) {
  return (
    <div className="node-card">
      <h3>{node.node_id}</h3>

      <p>Status: {node.status}</p>

      <p>Last Message: {node.latest.type}</p>

      {node.latest.metrics && (
        <>
          <p>CPU: {node.latest.metrics.cpu_usage}</p>
          <p>Temp: {node.latest.metrics.temperature}</p>
        </>
      )}
    </div>
  );
}
