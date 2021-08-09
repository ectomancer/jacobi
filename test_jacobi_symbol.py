import pytest

import jacobi_symbol

def test_jacobi_symbol():
    """Test Jacobi symbol function. Test data by clux @github.com
    Copyright (c) 2015 Eirik Albrigtsen.
    """
    assert jacobi_symbol.jacobi_symbol(-1, 5) == 1
    assert jacobi_symbol.jacobi_symbol(-1, 13) == 1
    assert jacobi_symbol.jacobi_symbol(-1, 3) == -1
    assert jacobi_symbol.jacobi_symbol(-1, 7) == -1
    assert jacobi_symbol.jacobi_symbol(2, 3) == -1
    assert jacobi_symbol.jacobi_symbol(2, 5) == -1
    assert jacobi_symbol.jacobi_symbol(2, 7) == 1
    assert jacobi_symbol.jacobi_symbol(2, 17) == 1
    assert jacobi_symbol.jacobi_symbol(3, 3) == 0
    assert jacobi_symbol.jacobi_symbol(3, 5) == -1
    assert jacobi_symbol.jacobi_symbol(3, 7) == -1
    assert jacobi_symbol.jacobi_symbol(3,5) == jacobi_symbol.jacobi_symbol(-2,5)
    assert jacobi_symbol.jacobi_symbol(-1,5) == jacobi_symbol.jacobi_symbol(4,5)
    assert jacobi_symbol.jacobi_symbol(11,7) == jacobi_symbol.jacobi_symbol(4,7)
    assert jacobi_symbol.jacobi_symbol(-3,7) == jacobi_symbol.jacobi_symbol(4,7)
    assert jacobi_symbol.jacobi_symbol(10,7) == jacobi_symbol.jacobi_symbol(3,7)
    assert jacobi_symbol.jacobi_symbol(2, 45) == -1
    assert jacobi_symbol.jacobi_symbol(3, 45) == 0
    assert jacobi_symbol.jacobi_symbol(7, 45) == -1
    assert jacobi_symbol.jacobi_symbol(2, 15) == 1
    assert jacobi_symbol.jacobi_symbol(1001, 9907) == -1  #wikepedia example
