from node import Node
import server 

class NodeServer:
    """
    Class composed of p2p node and api server
    """
    def __init__(self, p2pnode:Node =None, apiServer:server.Server=None) -> None:
        if p2pnode is not None:
            self._node = p2pnode
        else:
            self._node=Node()
        if apiServer is not None:
            self._apiServer = apiServer
        else:
            self._apiServer = server.Server()

    def start(self):
        self._node.start()
        server.importAccessbileNode(self._node)
        self._apiServer.start()