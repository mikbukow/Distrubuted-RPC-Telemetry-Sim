import { useEffect, useState } from "react";

import { getNodes } from "../api";
import type { NodeState } from "../types";

import NodeCard from "./node_card";

export default function Dashboard() {
  const [nodes, setNodes] = useState<NodeState[]>([]);

  useEffect(() => {
    const fetchNodes = async () => {
      try {
        const data = await getNodes();
        setNodes(data);
      } catch (err) {
        console.error(err);
      }
    };

    fetchNodes();

    const interval = setInterval(fetchNodes, 2000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h1>Fleet Dashboard</h1>

      {nodes.map((node) => (
        <NodeCard key={node.node_id} node={node} />
      ))}
    </div>
  );
}
