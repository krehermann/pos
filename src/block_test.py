import utils
import block

def test_hashable():
    p = block.Payload([],"f","123")
    ph = utils.hash(p)
    assert ph is not None

    b = block.Block(p)
    bh = utils.hash(b)
    assert bh is not None

def test_equals():
    p= block.Payload([],"f","123")
    b1 = block.Block(p)
    b2 = block.Block(p)

    assert b1 == b2

def test_toJSON():
    p= block.Payload([],"f","123")
    assert p.toJSON() is not None
    b1 = block.Block(p)
    assert b1.toJSON() is not None