import flask
from flask_classful import FlaskView, route
from multiprocessing import Process
from node import Node
# this is a sad artifact of the flaskview inheritence, which seems to preclude private data
nodeToServe: Node

class Server(FlaskView):
    """
    REST server to p2p node
    """
    #todo something about my machine doesn't like "localhost"
    def __init__(self, data=None, host="127.0.0.1", route="/") -> None:
        print("n", __name__)
        self._app = flask.Flask(__name__)
        self._route = route
        self._host = host
        self._server = None

    # todo threading
    def start(self):
        Server.register(self._app, "/")#self._route)
        self._app.run(self._host)
 
    # todo implement once start is threaded
    def stop(self):
       raise NotImplemented


    @route("/info")
    def info(self):
        return "POS info..."

    @route("/blockchain")
    def blockchain(self):
        return nodeToServe.blockchain.toJSON()

    @route("/pool")
    def pool(self):
        return nodeToServe.pool.toJSON()

def importAccessbileNode(globalNode):
    global nodeToServe
    nodeToServe = globalNode
