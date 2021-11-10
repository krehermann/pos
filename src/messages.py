

class Payload:
    def __init__(self,data) -> None:
        self._data = data

class Address:
    def __init__(self, id, port) -> None:
        self._id = id
        self._port = port

class Router:
    def __init__(self,sender: Address,reciever: Address, payload:Payload) -> None:
        self._sender = sender
        self._reciever = reciever
        self._payload = payload