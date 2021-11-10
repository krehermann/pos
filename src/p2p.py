from  p2pnetwork import node

class P2PNode(node.Node):
     # Python class constructor
    def __init__(self, host, port, id=None, callback=None, max_connections=0):
        super(P2PNode, self).__init__(host, port, id, callback, max_connections)
        print("MyPeer2PeerNode: Started")
