def jacobi_symbol(n: int, k: int) -> int:
    """Pure Python Jacobi symbol function by unknown.
    Published by Jacobi in 1837.
    Ported from Lua jacobi https://en.wikipedia.org/wiki/Jacobi_symbol#Implementation_in_Lua
    assert not implemented.
    """ 
    #assert(k > 0 and k % 2 == 1)
    n %= k
    t = 1
    while n:
        while not n % 2:
            n /= 2
            r = k % 8  #Solovay–Strassen primality test?
            if r == 3 or r == 5:
                t = -t
        n, k = k, n
        if n % 4 == 3 and k % 4 == 3:
            t = -t
        n %= k
    return t if k == 1 else 0


if __name__ == '__main__':
    print(1, jacobi_symbol(4, 3))
    print(-1, jacobi_symbol(5, 3))
    print(0, jacobi_symbol(6, 3))
    print(jacobi_symbol(7411, 9283))
