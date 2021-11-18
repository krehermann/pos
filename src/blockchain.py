
from types import TracebackType
from typing import List

from Crypto.PublicKey.RSA import RsaKey
import block
import utils
from datetime import datetime, timezone
import accounts
import transactions as txn
import json
import stake

class Chain:
    def __init__(self, genesisPublicKey:RsaKey) -> None:
        self._GENESIS_FORGER =  genesisPublicKey.export_key("PEM").decode('utf-8')  #"genesis"
        self._GENESIS_ID = utils.hash(self._GENESIS_FORGER).hexdigest()

        self._GENESIS_TIMESTAMP = datetime( 2021, 1, 1, 0, 0, 0, tzinfo=timezone.utc ).timestamp()

        self._genesis = self.createGenesis()
        self.blocks = [self._genesis]
        # this seems like a weird model where the account are kept seperately from the blocks
        # TODO learn more about real world account models
        self._accountBook = accounts.AccountBook()

        self._txnPerBlock=1
    @property
    def genesis(self):
        return self._genesis

    @property
    def genesisForger(self):
        return self._GENESIS_FORGER
    @property 
    def genesisId(self):
        return self._GENESIS_ID
    @property
    def genesisTimestamp(self):
        return self._GENESIS_TIMESTAMP

    def createGenesis(self) -> block.Block:
        genesisStake = 100
        genesisTransaction = txn.Transaction(self._GENESIS_FORGER,self._GENESIS_FORGER,genesisStake,txn.TransactionType.STAKE)
        genesisPayload = block.Payload([genesisTransaction],self._GENESIS_FORGER,self._GENESIS_ID)
        genesisPayload.time = self._GENESIS_TIMESTAMP   
        b =  block.Block(genesisPayload)
        return b

    def addBlock(self, nextBlock: block.Block) -> None:
        if self.currentBlockHash() != nextBlock.payload.previousHash:
           raise ValueError()
        else:
            self.blocks.append(nextBlock)

    
    def currentBlock(self) -> block.Block:
        return self.blocks[-1]

    def currentBlockHash(self) -> str:
        return utils.hash(self.currentBlock()).hexdigest()
        
    def length(self) -> int :
        return len(self.blocks)

    def transactionCovered(self, transaction:txn.Transaction):
        if transaction.type == txn.TransactionType.TRANSFER:
            return self._accountBook.get(transaction.payload.senderPublicKey).balance >= transaction.payload.amount 
        # assuming unlimited exchange tokens
        if transaction.type == txn.TransactionType.EXCHANGE:
            return True

    def listCoveredTransactions(self, transactions:List[txn.Transaction]) -> List[txn.Transaction]:
        output = []
        for tx in transactions:
            if self.transactionCovered(tx):
                output.append(tx)
        return output

    #this seems weird and hacky
    def addAccount(self, account):
        self._accountBook.create(account)

    def toJSON(self):
        return json.dumps(self, default=lambda x: x.__dict__)
        