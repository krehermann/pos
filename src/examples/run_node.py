import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from multiprocessing import Process
import nodeServer
import threading
import time
import argparse
import node
import server


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--p2phost',  type=str,
                    help='an integer for the accumulator',default="localhost") 
    parser.add_argument('--p2pport',  type=int,
                    help='an integer for the accumulator',default=50050) 
    parser.add_argument('--apiHost',  type=str,
                    help='an integer for the accumulator',default="127.0.0.1") 
    parser.add_argument('--apiPort',  type=int,
                    help='an integer for the accumulator',default=5000) 

    args = parser.parse_args()
    n = node.Node(host=args.p2phost, port=args.p2pport)
    s = server.Server(host=args.apiHost, port=args.apiPort)
    ns = nodeServer.NodeServer(p2pnode=n,apiServer=s)
 
   #p = Process(target=n.start)
   # p.start()
    t = threading.Thread(target=ns.start)
    t.start()
    time.sleep(60)
    