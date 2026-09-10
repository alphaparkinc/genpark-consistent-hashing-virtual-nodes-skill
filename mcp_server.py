from client import ConsistentHashRing
import json

def handle_request(req):
    ring = ConsistentHashRing()
    action = req.get("action")
    if action == "map":
        nodes = req.get("nodes", [])
        key = req.get("key", "")
        for n in nodes:
            ring.add_node(n)
        return {"status": "ok", "target_node": ring.get_node(key)}
    return {"status": "error", "message": "Unknown action"}

if __name__ == "__main__":
    print(json.dumps(handle_request({"action": "map", "nodes": ["n1", "n2"], "key": "k1"})))
