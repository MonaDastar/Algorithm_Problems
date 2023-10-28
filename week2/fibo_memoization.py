# Create a dictionary to store already calculated Fibonacci numbers
fibo_cach = {}
def fibonacci(n):
    
    if n in fibo_cach:
        return fibo_cach[n] # Check if the result is already calculated
    
    elif n==0:
        return 1
    elif n==1:
        return 1


    fib_number = fibonacci(n-2)+fibonacci(n-1)
        
        
    fibo_cach[n]=fib_number
    
    return(fib_number)

# Test the function
# Replace with the desired Fibonacci number
n=5
print(f"the {n}th number of fibonacci is : {fibonacci(n)}")