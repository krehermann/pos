import flask
from flask_classful import FlaskView, route
from multiprocessing import Process
from node import Node
from transactions import Payload, Transaction
import utils
import json
# this is a sad artifact of the flaskview inheritence, which seems to preclude private data
nodeToServe: Node

class Server(FlaskView):
    """
    REST server to p2p node
    """
    #todo something about my machine doesn't like "localhost"
    def __init__(self, host="127.0.0.1", port=5000, route="/") -> None:
        self._app = flask.Flask(__name__)
        self._route = route
        self._host = host
        self._server = None
        self._port = port

    # todo threading
    def start(self):
        Server.register(self._app, "/")#self._route)
        self._app.run(self._host,self._port)
 
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

    @route("/transaction", methods=['POST'])
    def transaction(self):
        payload = flask.request.get_json()

        if not 'transaction' in payload:
            print("no transaction ", payload)
            return "bad data, no transaction", 400
        rawTxn = payload['transaction']

        txn = utils.decode(rawTxn)
        if not isinstance(txn,Transaction):
            print("decoded message not txn?!")
            return "malformed data", 400
        nodeToServe.handleTransaction(txn)
        return "", 201


class TransactionMessage:
    def __init__(self,txn:Transaction = None) -> None:
        self.transaction=txn
    def toJSON(self):
        return json.dumps(self, default=lambda x: x.__dict__)
    def fromJSON(self,jsonObject):
        if not 'transaction' in jsonObject:
            raise ValueError("no transaction in ", jsonObject)
        rawTxn = jsonObject['transaction']
        txn = utils.decode(rawTxn)
        if  not isinstance(txn, Transaction):
            raise ValueError("raw data not decoded to transaction", rawTxn)

def importAccessbileNode(globalNode):
    global nodeToServe
    nodeToServe = globalNode
