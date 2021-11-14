import utils
def test_roundtrip():

    payload = {}
    payload["type"] ="HANDSHAKE"
    others = []
    for p in [1,2]:
        others.append({"id": p, "host": p, "port": p})
    payload["peers"] = others
    print(payload)
    e = utils.encode(payload)
    print(e)
    dd = utils.decode(e)
    print(dd)
    assert payload == dd
    assert payload == 3