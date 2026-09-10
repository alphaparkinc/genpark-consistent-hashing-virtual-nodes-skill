import hashlib

class ConsistentHashRing:
    """
    Consistent Hashing Ring with Virtual Nodes.
    Distributes keys uniformly across cluster nodes with minimal remapping on topology changes.
    """
    def __init__(self, replicas=3):
        self.replicas = replicas
        self.ring = {}
        self.sorted_keys = []

    def _hash(self, key):
        return int(hashlib.md5(key.encode("utf-8")).hexdigest()[:8], 16)

    def add_node(self, node_id):
        for r in range(self.replicas):
            h = self._hash(f"{node_id}:{r}")
            self.ring[h] = node_id
        self.sorted_keys = sorted(self.ring.keys())

    def remove_node(self, node_id):
        for r in range(self.replicas):
            h = self._hash(f"{node_id}:{r}")
            self.ring.pop(h, None)
        self.sorted_keys = sorted(self.ring.keys())

    def get_node(self, key):
        if not self.ring:
            return None
        h = self._hash(key)
        for ring_h in self.sorted_keys:
            if h <= ring_h:
                return self.ring[ring_h]
        return self.ring[self.sorted_keys[0]]
