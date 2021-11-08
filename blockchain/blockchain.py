
import block
import utils
from datetime import datetime, timezone

GENESIS_FORGER = "genesis"
GENESIS_ID = "1234"
GENESIS_TIMESTAMP = 0#datetime( 2021, 1, 1, 0, 0, 0, tzinfo=timezone.utc ).time()


def genesis() -> block.Block:
    genesisPayload = block.Payload([],GENESIS_FORGER,utils.hash(GENESIS_ID).hexdigest)
    genesisPayload.time = GENESIS_TIMESTAMP   
    b =  block.Block(genesisPayload)
    return b


class Blockchain:

    def __init__(self) -> None:
        self._genesis = genesis()
        self.blocks = [self._genesis]
   
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