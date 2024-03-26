import hashlib
import json

class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.blockchain = []

    def generate_key(self, data):
        return hashlib.sha256(data.encode()).hexdigest()

    def create_block(self, data):
        prev_block_hash = self.blockchain[-1]['hash'] if self.blockchain else None
        block_key = self.generate_key(str(prev_block_hash) + str(data))

        new_block = {
            'id': len(self.blockchain) + 1,
            'timestamp': int(time.time()),
            'data': data,
            'previous_hash': prev_block_hash,
            'hash': block_key
        }

        self.blockchain.append(new_block)

if __name__ == "__main__":
    node1 = Node('node1')
    node1.create_block('data1')

    print("Node 1 blockchain:")
    print(json.dumps(node1.blockchain, indent=4))

    print("\nNode 1 blockchain hash:")
    previous_hash = node1.blockchain[-1]['hash']
    print(previous_hash)


    # Let's suppose node 1 shares its blockchain with node 2

    node2 = Node('node2')

    node2.blockchain = node1.blockchain

    print("\nNode 2 blockchain after receiving blockchain from Node 1:")
    print(json.dumps(node2.blockchain, indent=4))
