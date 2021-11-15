
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import server

if __name__ == '__main__':
    print('running server server')
    server = server.Server(data="stuff")
    server.start()