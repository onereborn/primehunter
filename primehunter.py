import os
import random
import datetime

def generate_candidate(min_digits):

    min_value = 10**(min_digits - 1)
    max_value = 10**min_digits - 1

    candidate = random.randint(min_value, max_value)
    if candidate % 2 == 0:
        candidate += 1

    return candidate

def count_digits(number):
    return len(str(number))

def main():
    attempts = 0
    
    while True:
        attempts += 1
        candidate = generate_candidate(500)
        if is_prime(candidate):
            print(f"Found a prime number: {candidate} after {attempts} attempts")
            break

        if attempts % 100 == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Attempt {attempts}: Still searching for a prime number...")   

        save_prime_to_file(candidate, attempts)

def is_prime(n, rounds = 10):

    if n == 2 or n == 3:
        return True
    
    if n % 2 == 0 or n < 2:
        return False
    
    d = n - 1
    r = 0
    while d % 2 == 0:
        d = d // 2
        r += 1

    for _ in range(rounds):
        a = random.randint(2, n - 1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def save_prime_to_file(prime, attempts, filename="found_primes.txt"):
    with open(filename, "a") as file:
        file.write(f"Prime found: {prime}" + "\n")
        file.write(f"=================================" + "\n")
        file.write(f"Digits: {count_digits(prime)}" + "\n")
        file.write(f"Timestamp: {datetime.datetime.now()}" + "\n")
        file.write(f"attempts: {attempts}" + "\n")

if __name__ == "__main__":
    main()