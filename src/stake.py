

import utils
import sys 

class Stake:
    def __init__(self, id, amount) -> None:
        self._id = id
        self._amount = amount

    @property
    def id(self):
        """
        public key string
        """
        return self.id
    @property
    def amount(self):
        return amount

class Pool:
    def __init__(self, nonce, genesis:Stake) -> None:
        self._stakes = {}
        self._nonce = nonce
        self._stakes[genesis.id] = genesis.amount

    def update(self, previous:Stake, new:Stake):
        if self._stakes[previous.id] is not None:
            if previous.id == new.id:
                self._stakes[new.id] = new

    def get(self, id:str)->Stake:
        return self._stakes[id]

    def create(self, stake:Stake):
        if self._stakes[stake.id] is None:
            self._stakes[stake.id] = stake

    def delete(self, stake:Stake):
        if stake.id in self._stakes:
            del self.stake[stake.id]


    def lots(self):
        lotDict = {}
        for stake in self._stakes.values():
            lg = LotGenerator(stake, self._nonce)
            lotDict[stake.id] = lg.getLots()
        return lotDict

    def winner(self):
        winningStake = None
        winningDistance = sys.maxsize #int max
        target = int(utils.hash(self._nonce).hexdigest(),16)
        for id, lotValues in self.lots():
            assert self._stakes[id] is not None
            for lot in lotValues:
                proprosal = int(lot,16)
                if abs(target-proprosal) <winningDistance:
                    winningStake = self._stakes[id]
                    winningDistance =abs(target-proprosal)

        return winningStake

class LotGenerator:
    def __init__(self, stake:Stake, nonce) -> None:
        #self._publicKey = publicKey
        self._stake = stake
        self._nonce = nonce
        
        self._lots = None

    def value(self):
        hash = self._stake.id + self._nonce
        for _ in range(self._stake.amount):
            hash = utils.hash(hash)
        return hash

    def getLots(self):
        lots =  []
        hash = self._stake.id + self._nonce
        for _ in range(self._stake.amount):
            hash = utils.hash(hash).hexdigest()
            lots.append(hash)
        
        #out = {}
        #out[self._publicKey] = lots
        return lots

        