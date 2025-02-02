def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True  

def filter_prime(numbers):
    return [num for num in numbers if isprime(num)]


numbers = list(map(int, input().split()))
primenumbers = filter_prime(numbers)  
print(primenumbers)
