import wallet
import transaction_pool
import transactions as txn
import blockchain as bc
import block

def test_app():
    
    alice = wallet.Wallet()
    bob = wallet.Wallet()
    exchange = wallet.Wallet()
    forger = wallet.Wallet()
    
    pool = transaction_pool.SecurePool()
    
    #seed alice with 10 tokens
    pool.addTransaction(txn.Transaction(exchange.publicKey,alice.publicKey,
    10,
    txn.TransactionType.EXCHANGE))


    chain = bc.Chain()
    block1 = block.Block(block.Payload(chain.listCoveredTransactions(pool.transactions()),forger.publicKey,chain.currentBlockHash()))
    chain.addBlock(block1)