import type { NodeState } from "./types";

export async function getNodes(): Promise<NodeState[]> {
  const response = await fetch("http://localhost:8000/nodes");

  if (!response.ok) {
    throw new Error("Failed to fetch nodes");
  }

  return response.json();
}