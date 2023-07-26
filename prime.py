def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Test the function
max_limit = int(input("Enter the maximum limit to find prime numbers: "))
result = prime_numbers(max_limit)
print("Prime Numbers:", result)
