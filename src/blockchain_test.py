
from Crypto.PublicKey import RSA
import blockchain as bc
import block
import transactions as txn
import transaction_pool



testKeyStr = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCpQ2c9UvIiDOdU4i4yZG0Swyf2
8ylVMePPSTL0Lqh3Z8gcorYbMLEalUjXPIvuIcdRzjzVUDFt9wWPE4m0InaZH/ul
USpEiWpX6zbkrcXsSnVg6v4gHROrYoE0ZkvmuVUAKr/KhXe3S6SN75WQABJG9Ew9
JhG1hlWvS9TiCqIr6QIDAQAB
-----END PUBLIC KEY-----'''

testKey = RSA.import_key(testKeyStr)
def test_gensis():
    chain = bc.Chain(testKey)
    assert chain.length() ==1 
    g = chain.genesis
    assert g.payload.time == chain.genesisTimestamp
    assert g.payload.forger == chain.genesisForger
   
    assert g == chain.currentBlock()

def test_addBlock():
    chain = bc.Chain(testKey)
    nextBlockPayload = block.Payload([],'forgername',chain.currentBlockHash())
    print(chain.currentBlockHash())
    print(nextBlockPayload.previousHash)
    assert chain.currentBlockHash() == nextBlockPayload.previousHash
    nextBlock = block.Block(nextBlockPayload)
    chain.addBlock(nextBlock)
    assert chain.length() == 2
    b = chain.currentBlock()
    assert isinstance(b, block.Block)
    assert chain.currentBlock().payload.time == nextBlock.payload.time

def test_covered():
    pool = transaction_pool.Pool()
    
    #seed alice with 10 tokens
    ok_txn = txn.Transaction("exchange","reciever",
    10,
    txn.TransactionType.EXCHANGE)
    bad_txn = txn.Transaction("sender1","reciever1",
    10,
    txn.TransactionType.TRANSFER)
    pool.addTransaction(ok_txn)
    pool.addTransaction(bad_txn)
    
    chain = bc.Chain(testKey)
    #this is weird. needs work. account creation should somehow be derived from wallet creation?
    chain.addAccount("exchange")
    chain.addAccount("reciever")
    chain.addAccount("sender1")
    chain.addAccount("reciever1")
    
    covered = chain.listCoveredTransactions(pool.transactions())
    assert len(covered) == 1
    assert covered[-1] == ok_txn