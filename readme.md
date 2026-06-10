# PrimeHunter

A Python tool that hunts for large non-Mersenne prime numbers 
using random candidate generation and Miller-Rabin primality testing.

## What it does
- Generates random large numbers (default 500 digits)
- Filters out even numbers immediately
- Tests primality using the Miller-Rabin algorithm
- Skips Mersenne primes (2^n - 1) — these are well searched already
- Saves discovered primes to found_primes.txt with timestamp

## Why non-Mersenne primes?
Most large prime searches focus on Mersenne primes because they are 
easier to test. This project targets the wider, less explored space 
of non-Mersenne primes.

## How to run
pip install -r requirements.txt
python primehunter.py

## Example output
Found a prime number after 69 attempts
Digits: 500
Saved to found_primes.txt

## What I'd add next
- Multiprocessing to use all CPU cores simultaneously
- A Flask dashboard showing live search progress
- Distributed search so multiple users cover different ranges
- Automatic submission of finds to a prime database

## Built with
- Python 3.13
- sympy (for verification)