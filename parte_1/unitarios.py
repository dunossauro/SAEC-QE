def soma(x, y):
    return x + y


def test_soma_1_1_retorna_2():
    assert soma(1, 1) == 2


def test_soma_0_0_retorna_0():
    assert soma(0, 0) == 0
