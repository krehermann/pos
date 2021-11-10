#import pytest
import transactions as tx

def test_transaction():
    #pl = tx.Payload(
    txn = tx.Transaction("sender", "reciever",10,1)

    assert txn.payload.senderPublicKey == "sender"
    assert txn.payload.recieverPublicKey == "reciever"
    assert txn.payload.amount == 10 
    assert txn.payload.type == 1
    assert txn.toJSON() is not None
 
