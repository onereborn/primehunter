import sys
import random
import datetime
 
 
def generate_candidate(min_digits):
    min_value = 10 ** (min_digits - 1)
    max_value = 10 ** min_digits - 1
 
    candidate = random.randint(min_value, max_value)
    if candidate % 2 == 0:
        candidate += 1  # primes above 2 are odd
 
    return candidate
 
 
def count_digits(number):
    return len(str(number))
 
 
def is_prime(n, rounds=10):
    """Miller-Rabin test. Returns True if n is *probably* prime."""
    if n == 2 or n == 3:
        return True
 
    if n % 2 == 0 or n < 2:
        return False
 
    # write n - 1 as d * 2^r with d odd
    d = n - 1
    r = 0
    while d % 2 == 0:
        d = d // 2
        r += 1
 
    for _ in range(rounds):
        a = random.randint(2, n - 2)  # n - 1 is not a useful witness
        x = pow(a, d, n)
 
        if x == 1 or x == n - 1:
            continue
 
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # definitely composite
    return True
 
 
def save_prime_to_file(prime, attempts, filename="found_primes.txt"):
    with open(filename, "a") as file:
        file.write(f"Prime found: {prime}" + "\n")
        file.write("=================================" + "\n")
        file.write(f"Digits: {count_digits(prime)}" + "\n")
        file.write(f"Timestamp: {datetime.datetime.now()}" + "\n")
        file.write(f"Attempts: {attempts}" + "\n")
        file.write("\n")
 
 
def main(digits=500):
    attempts = 0
    found = 0
 
    print(f"Searching for {digits}-digit primes. Press Ctrl+C to stop.")
    try:
        while True:
            attempts += 1
            candidate = generate_candidate(digits)
 
            if is_prime(candidate):
                found += 1
                save_prime_to_file(candidate, attempts)  # only primes get saved
                print(f"\nFound prime #{found} ({count_digits(candidate)} digits) "
                      f"after {attempts} attempts - saved to found_primes.txt")
                attempts = 0  # start counting again for the next prime
            elif attempts % 100 == 0:
                print(f"Attempt {attempts}: still searching...", end="\r")
    except KeyboardInterrupt:
        print(f"\nStopped. Found {found} prime(s) this run.")
 
 
if __name__ == "__main__":
    # usage: python primehunter.py [digits]
    digits = int(sys.argv[1]) if len(sys.argv) > 1 else 500
    main(digits)
 
