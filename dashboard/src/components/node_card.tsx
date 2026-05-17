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
          <p>Temp (F): {node.latest.metrics.temperature_f}</p>
          <p>Temp (C): {node.latest.metrics.temperature_c}</p>
          <p>Humidity: {node.latest.metrics.humidity}</p>
          <p>Pressure: {node.latest.metrics.pressure}</p>
        </>
      )}
    </div>
  );
}
