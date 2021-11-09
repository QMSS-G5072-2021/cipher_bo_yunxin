from cipher_yb2503 import cipher_yb2503
import pytest 

def test_cipher_single():
    example = 'test'
    expected = 'vguv'
    actual = cipher_yb2403.cipher(example, 2, True)
    assert actual == expected, 'not works for a single word'