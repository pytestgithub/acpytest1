import pytest

@pytest.mark.parametrize(('iin','out'),((1,1),(2,2)))
def test_01(iin,out):
 assert iin==out,'no match'
