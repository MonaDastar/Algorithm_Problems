from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    if n == 1 :
        return 1
    elif n == 2: 
        return 1
    elif n>2:
        return fibonacci(n-2)+fibonacci(n-1)
    
    
    
n=5
print(fibonacci(500))