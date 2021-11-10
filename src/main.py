import wallet
import  blockchain as bc
import transaction_pool
import transactions as txn
import block
def main():
    alice = wallet.Wallet()
    bob = wallet.Wallet()
    exchange = wallet.Wallet()
    forger = wallet.Wallet()

    
    pool = transaction_pool.Pool()
    
    #seed alice with 10 tokens
    pool.addTransaction(txn.Transaction(exchange.publicKey,alice.publicKey,
    10,
    txn.TransactionType.EXCHANGE))

    chain = bc.Chain()
    block1 = block.Block(block.Payload(chain.listCoveredTransactions(),forger.publicKey,chain.currentBlockHash()))
    chain.addBlock(block1)
    chain.
    

if __name__ == 'main':
    main()
