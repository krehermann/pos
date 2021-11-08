#import blockchain as bc
#from blockchain.blockchain import Blockchain
import blockchain
import block
import utils 

def test_gensis():
    chain = blockchain.Blockchain()
    assert chain.length() ==1 
    g = chain.genesis
    assert g.payload.time == blockchain.GENESIS_TIMESTAMP
    assert g.payload.forger == blockchain.GENESIS_FORGER
   
    assert g == chain.currentBlock()

def test_addBlock():
    chain = blockchain.Blockchain()
    nextBlockPayload = block.Payload([],'forgername',utils.hash(chain.currentBlock()).hexdigest())
    print(utils.hash(chain.currentBlock()).hexdigest())
    print(nextBlockPayload.previousHash)
    assert utils.hash(chain.currentBlock()).hexdigest() == nextBlockPayload.previousHash
    nextBlock = block.Block(nextBlockPayload)
    chain.addBlock(nextBlock)
    assert chain.length() == 2
    b = chain.currentBlock()
    assert isinstance(b, block.Block)
    assert chain.currentBlock().payload.time == nextBlock.payload.time
