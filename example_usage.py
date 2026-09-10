from client import ConsistentHashRing

def main():
    print("=== Testing Consistent Hashing Ring ===")
    ring = ConsistentHashRing(replicas=5)
    
    nodes = ["cache_node_1", "cache_node_2", "cache_node_3"]
    for n in nodes:
        ring.add_node(n)
        
    keys = ["user_1001", "session_982", "order_5541", "cart_771", "token_889"]
    for k in keys:
        target = ring.get_node(k)
        print(f"Key '{k}' mapped to node '{target}'")
        assert target in nodes
        
    print("=== Consistent Hashing Verification Complete ===")

if __name__ == "__main__":
    main()
