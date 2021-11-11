import p2p
from socket import socket, AF_INET, SOCK_STREAM
import time

def test_p2p_inbound():
    soc = socket(AF_INET, SOCK_STREAM)
    soc.bind(('', 0))
    port =soc.getsockname()[1]
    soc.close()
    node = p2p.P2PNode('localhost',50050)

    soc2 = socket(AF_INET, SOCK_STREAM)
    soc2.bind(('', 0))
    port2 =soc2.getsockname()[1]
    soc2.close()
    node2 = p2p.P2PNode('localhost',50051)

    soc3 = socket(AF_INET, SOCK_STREAM)
    soc3.bind(('', 0))
    port3 =soc3.getsockname()[1]
    soc3.close()
    node3 = p2p.P2PNode('localhost',50052)

    node.start()
    node2.start()
    node3.start()
    print("node1: ", node.id, node.port)
    print("node2: ", node2.id, node2.port)
    print("node3: ", node3.id,node3.port)
    
    # n2 -> n
    node.debug = True
    node2.debug = True
    node2.connect_with_node(node.host,node.port)
    #node2.identify(node)

    # poor mans sync
    time.sleep(2)
    assert len(node.nodes_outbound) == 0
    assert len(node.nodes_inbound) == 1

    assert len(node2.nodes_outbound) == 1
    assert len(node2.nodes_inbound) == 0
 
    assert len(node2.discoverablePeers) == 1
    assert len(node.discoverablePeers) == 1 
    
    node2.debug_print(str(node2.discoverablePeers))
    node.debug_print(str(node.discoverablePeers))
    #assert False
    # n3 -> n <- n2 ==> n3 -* n
    #                     \   *
    #                      *  |
    #                        n2
   # node3.debug = True
    node3.connect_with_node(node.host, node.port)
    time.sleep(2)
 
    time.sleep(2)
  
    assert len(node.nodes_outbound) == 0
    assert len(node.nodes_inbound) == 2

    assert len(node3.nodes_outbound) == 2
    assert len(node3.nodes_inbound) ==0

 
    assert len(node2.nodes_outbound) == 1
    assert len(node2.nodes_inbound) == 1

    node.stop()
    node2.stop()
    node3.stop()