def fibo(n):
    """returnt the nth fibonacci number using
    bottom-up dynamic programming - uses iteration and caching (Tabulation) 

    Args:
        n (integer): the nth required number

    Returns:
        integer: the nth number in Fibonacci series
    """
    
    f=[0,1]

    for i in range(2,n+1):
        f.append( f[i-1]+f[i-2])
    return (f[n])


print(fibo(6))