

def find_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

array = [5, 6, 4, 12]

# Initialize the GCD with the first number in the list
gcd_result = array[0]

# Iterate through the remaining numbers in the list and find their GCD with the current result
for num in array[1:]:
    gcd_result = find_gcd(gcd_result, num)

print("GCD of the numbers:", gcd_result) 