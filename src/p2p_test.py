import p2p
from socket import socket, AF_INET, SOCK_STREAM

def test_p2p_inbound():
    soc = socket(AF_INET, SOCK_STREAM)
    soc.bind(('', 0))
    node = p2p.P2PNode('localhost',soc.getsockname()[1])

    soc2 = socket(AF_INET, SOCK_STREAM)
    soc2.bind(('', 0))
    node2 = p2p.P2PNode('localhost',soc2.getsockname()[1])

    node.start()
    node2.start()

    node.connect_with_node(node2.host,node2.port)

    assert len(node.nodes_outbound) == 1
    assert len(node2.nodes_inbound) == 1

    node.stop()
    node2.stop()