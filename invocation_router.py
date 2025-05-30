# invocation_router.py
# Routes incoming voice assistant invocations to the correct Dharma agent

from typing import Dict

# Example registry of agents
AGENT_REGISTRY: Dict[str, str] = {
    "hanuma": "https://api.ramagpt.ai/hanuma",
    "tilakam": "https://api.tilakam.me/recommend",
    "ganga": "https://api.dharmanidhi.org/ganga"
}

def route_invocation(agent_name: str, payload: dict) -> str:
    agent = agent_name.lower()
    if agent not in AGENT_REGISTRY:
        return f"Unknown agent: {agent_name}"
    endpoint = AGENT_REGISTRY[agent]
    # Placeholder: simulate forwarding
    return f"Routing to {endpoint} with payload: {payload}"

# Example usage
if __name__ == "__main__":
    print(route_invocation("hanuma", {"query": "what tilakam today?"}))
