import pytest

class ZeroError(Exception):
    def __init__(self, message = "Value can't be zero"):
        self.message = message
        super().__init__(self.message)

def test_generic():
    a = 0
    b = 6
    with pytest.raises(ZeroError):
        if a == 0:
            raise ZeroError
        else:
            assert a==b