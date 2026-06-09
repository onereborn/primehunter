import random
import math

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
    candidate = generate_candidate(100)
    print(f"Generated candidate: {candidate}")
    print(f"Number of digits: {count_digits(candidate)}")

if __name__ == "__main__":
    main()