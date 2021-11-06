import wallet

def test_wallet():


    w = wallet.Wallet()
    data = "123"
    d2 = "123"
    s = w.sign(data)
    assert s is not None
    assert w.sign(data) == w.sign(d2)
    print(s)