def print_primes_in_range(limit):
    print(f"Prime numbers up to {limit}:")
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
    print() # Newline

n = int(input("Enter range: "))
print_primes_in_range(n)