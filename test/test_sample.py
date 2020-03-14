def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4
    assert inc(0) == 1
    assert inc(inc(4)) == 6