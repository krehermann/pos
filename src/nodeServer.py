from node import Node
import server 

class NodeServer:
    """
    Class composed of p2p node and api server
    """
    def __init__(self, p2pnode:Node =None, apiServer:server.Server=None) -> None:
 
        self._node = p2pnode
        if self._node is None:
            self._node=Node()
        
        self._apiServer = apiServer
        if self._apiServer is None:
            self._apiServer = server.Server()

    def start(self):
        self._node.start()
        server.importAccessbileNode(self._node)
        self._apiServer.start()