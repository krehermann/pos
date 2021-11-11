

class Payload:
    def __init__(self,data) -> None:
        self._data = data

class Address:
    def __init__(self, id, port) -> None:
        self._id = id
        self._port = port

    def __eq__(self, o: object) -> bool:
        if  not isinstance(o):
            return False
        return self._id == o._id and self._port == o._port

        
class Router:
    def __init__(self,sender: Address,reciever: Address, payload:Payload) -> None:
        self._sender = sender
        self._reciever = reciever
        self._payload = payload