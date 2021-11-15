import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from multiprocessing import Process
import nodeServer
import threading
import time 
if __name__ == '__main__':
    n = nodeServer.NodeServer()

   #p = Process(target=n.start)
   # p.start()
    t = threading.Thread(target=n.start)
    t.start()
    time.sleep(60)
    