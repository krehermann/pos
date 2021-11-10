
import blockchain as bc
import block
import transactions as txn
import transaction_pool

def test_gensis():
    chain = bc.Chain()
    assert chain.length() ==1 
    g = chain.genesis
    assert g.payload.time == chain.genesisTimestamp
    assert g.payload.forger == chain.genesisForger
   
    assert g == chain.currentBlock()

def test_addBlock():
    chain = bc.Chain()
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
    
    chain = bc.Chain()
    #this is weird. needs work. account creation should somehow be derived from wallet creation?
    chain.addAccount("exchange")
    chain.addAccount("reciever")
    chain.addAccount("sender1")
    chain.addAccount("reciever1")
    
    covered = chain.listCoveredTransactions(pool.transactions())
    assert len(covered) == 1
    assert covered[-1] == ok_txn