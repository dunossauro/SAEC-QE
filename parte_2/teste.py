from isolados import exp
from unittest.mock import patch


@patch('isolados.soma', return_value=0)
def test_isolado(soma):
    assert exp(1, 1, 1) == 1
