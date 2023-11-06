def fact(n:int):
    for i in range(2,n):
        if n>1 and n%i !=0:
            return False
        n=n/i
        if n==1:
            return True

print(fact(25))