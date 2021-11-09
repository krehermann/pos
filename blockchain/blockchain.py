
import block
import utils
from datetime import datetime, timezone
import accounts
import transactions

GENESIS_FORGER = "genesis"
GENESIS_ID = "1234"
GENESIS_TIMESTAMP = datetime( 2021, 1, 1, 0, 0, 0, tzinfo=timezone.utc ).timestamp()


def genesis() -> block.Block:
    genesisPayload = block.Payload([],GENESIS_FORGER,utils.hash(GENESIS_ID).hexdigest)
    genesisPayload.time = GENESIS_TIMESTAMP   
    b =  block.Block(genesisPayload)
    return b


class Blockchain:

    def __init__(self) -> None:
        self._genesis = genesis()
        self.blocks = [self._genesis]
        # this seems like a weird model where the account are kept seperately from the blocks
        # TODO learn more about real world account models
        self.accountBook = accounts.AccountBook()

    @property
    def genesis(self):
        return self._genesis

    def addBlock(self, nextBlock: block.Block) -> None:

        if utils.hash(self.currentBlock()).hexdigest() != nextBlock.payload.previousHash:
           raise ValueError()
        else:
            self.blocks.append(nextBlock)

    
    def currentBlock(self) -> block.Block:
        return self.blocks[-1]

    def length(self) -> int :
        return len(self.blocks)

    def transactionCovered(self, transaction:transactions.Transaction):
        if transaction.type == transactions.TransactionType.TRANSFER:
            return self.accountBook.get(transaction.payload.senderPublicKey).balance >= transaction.payload.amount 