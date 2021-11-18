import wallet
import transaction_pool
import transactions as txn
import blockchain as bc
import block
from Crypto.PublicKey import RSA
def test_app():
    
    testKeyStr = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCpQ2c9UvIiDOdU4i4yZG0Swyf2
8ylVMePPSTL0Lqh3Z8gcorYbMLEalUjXPIvuIcdRzjzVUDFt9wWPE4m0InaZH/ul
USpEiWpX6zbkrcXsSnVg6v4gHROrYoE0ZkvmuVUAKr/KhXe3S6SN75WQABJG9Ew9
JhG1hlWvS9TiCqIr6QIDAQAB
-----END PUBLIC KEY-----'''

    testKey = RSA.import_key(testKeyStr)

    alice = wallet.Wallet()
    bob = wallet.Wallet()
    exchange = wallet.Wallet()
    forger = wallet.Wallet()
    
    pool = transaction_pool.SecurePool()
    
    #seed alice with 10 tokens
    pool.addTransaction(txn.Transaction(exchange.publicKey,alice.publicKey,
    10,
    txn.TransactionType.EXCHANGE))


    chain = bc.Chain(testKey)
    block1 = block.Block(block.Payload(chain.listCoveredTransactions(pool.transactions()),forger.publicKey,chain.currentBlockHash()))
    chain.addBlock(block1)