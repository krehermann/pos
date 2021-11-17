from typing import List
from  p2pnetwork import node
from transactions import Transaction
import utils
import json
from transaction_pool import SecurePool
class P2PNode(node.Node):
     # Python class constructor
    def __init__(self, host, port, txn_pool: SecurePool= None,peer=None, peerHost=None, peerPort= None, id=None, callback=None, max_connections=0, debug=False):
        super(P2PNode, self).__init__(host, port, id, callback, max_connections)
        self.debug = debug
 
        self._initPeer = peer
        self._peerHost = peerHost
        self._peerPort = peerPort
        self._host=host
        self._port=port
        self.discoverablePeers= []
        self._transaction_pool = txn_pool

    @property
    def publicHost(self):
        return self._host
    @property
    def publicPort(self):
        return self._port
    
    
    @property
    def pool(self):
        return self._transaction_pool
    @pool.setter
    def pool(self, p: SecurePool):
        self._transaction_pool = p

    def start(self) -> None:
        print("MyPeer2PeerNode: Starting...")
        super().start()

        #if self._initPeer is not None:
        if (self._peerHost is not None) and (self._peerHost is not None):
            self.debug_print("bootstapping")
            self.connect_with_node(self._peerHost, self._peerPort)

    def inbound_node_connected(self, node):
        self.debug_print("inbound_node_connected: " + str(node) +"\n")
 
        return self.handshake(node)
    
    def outbound_node_disconnected(self, node):
        return super().outbound_node_disconnected(node)
        
    def outbound_node_connected(self, node):
        #on outbound connections we need to pass our contact info back because under the covers
        #node is connected to a different port than self.port do to threading socket connections in the lib
        #by identifying self, a 3rd party that connect to node can find route to self
        self.identify(node)
        return self.handshake(node)

    #this needs to be implemented with typed messages rather than dictionaries
    def node_message(self, node, data):
        self.debug_print(str("node_message recv " + node.id + " " + json.dumps(data))+"\n")
        
        if isinstance(data,dict):
            data = json.dumps(data)
        msg = utils.decode(data)
        if isinstance(msg, Transaction): #msg["type"] == "TRANSACTION":
            if self.pool.addTransaction(msg):
                #broadcast to peers. this simple implementation is an echo chamber
                self.send_to_nodes(data)
        elif msg["type"] == "HANDSHAKE":
            peers = msg["peers"]
            self.debug_print("HANDSHAKE: peers to connect to:" + str(peers)+ "\n")
            for p in peers:
                if p["id"] != self.id and p["id"] not in self.nodes_outbound :
                    self.connect_with_node(p["host"], p["port"])

        elif msg["type"] == "IDENTIFY":
            # this needs to be refactored to check against a dict or something
            incoming = msg["reciever"]
            p = SimplePeer(incoming["host"],incoming["port"], incoming["id"])
            if (p != SimplePeer(self.host, self.port, self.id)):
                doAppend = True
                for dp in self.discoverablePeers:
                    if dp == p:
                        doAppend = False
                        break

                if doAppend: self.discoverablePeers.append(incoming)
                self.debug_print("IDENTIFY: discoverablePeers now " + str(self.discoverablePeers) +"\n")


        #except Exception as e:
        #    print(e)
        #    print(data)
        # try: 
        #     msg = utils.decode(data,classes=[Message])
        #     print(msg)
        #     assert isinstance(msg, Message)
        #     if msg.type == "HANDSHAKE":
        #         print("node ", self.id, "recieve Handshake" )
        #         peers = msg.data
        #         for p in peers:
        #             print("node ", self.id, "connecting to ", p.id)
                    
        #             self.connect_with_node(p.host, p.port)

        # except Exception as e:
        #     print(e)


    def bootstrap(self, peer):
        if peer is not None:
            #self.debug_print(str("bootstraping to peer ", peer))
            self.connect_with_node(peer.host, peer.port)


    def identify(self, node):
        """
        self identify back to the other node
        this seems to be needed to communicate the open port this is listening for self
        under the covers the lib invokes thread for each incoming request, which have a different port
        need a mechanism to identify self to node so that if 3rd party connects to node it can figure out how to 
        connect to self
        """
        payload = {}
        # hack need real messages. debugged this way b/c unknown to me the lib was deserializing data messages.
        payload["type"] ="IDENTIFY"
        payload["reciever"] = {"id": self.id, "host": self.host, "port": self.port}
        m = utils.encode(payload)
        self.send_to_node(node, m)

    def handshake(self, node):
        """
        send list of peers
        """
        
        peers = self.nodes_outbound #self.nodes_inbound
        # hack need real messages. debugged this way b/c unknown to me the lib was deserializing data messages.
        payload = {}
        payload["type"] ="HANDSHAKE"
        others = self.discoverablePeers
        for p in peers:
            others.append({"id": p.id, "host": p.host, "port": p.port})
        payload["peers"] = others
        m = utils.encode(payload)
        self.send_to_node(node, m)


class Message:
    def __init__(self, type, data) -> None:
        self.type = type
        self.data = data


class SimplePeer:
    def __init__(self, host, port, id) -> None:
        self._host = host
        self._port = port
        self._id = id

    @property
    def host(self):
        return self._host
    @property
    def id(self):
        return self._id
    @property
    def port(self):
        return self._port

    def __eq__(self, o: object) -> bool:
        if not isinstance(o,SimplePeer):
            return False
        return self.host == o.host and self.port == o.port and self.id == o.id