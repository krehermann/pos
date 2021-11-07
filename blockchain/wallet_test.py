import wallet

def test_wallet():


    w = wallet.Wallet()
    data = "123"
    d2 = "123"
    s = w.sign(data)
    print(s)
    assert s is not None
    assert w.sign(data) == w.sign(d2)
    

def test_signature():
    w = wallet.Wallet()
    data = "123"
    s = w.sign(data)
    print(s)
    assert wallet.signatureValidate(s,data,w.publicKey) == True

def test_new_transaction():
    w = wallet.Wallet()
    txn = w.newTransaction("reciever",10,"transfer")
    assert txn.payload.recieverPublicKey == "reciever"
    assert txn.payload.amount == 10
    assert txn.payload.type == "transfer"