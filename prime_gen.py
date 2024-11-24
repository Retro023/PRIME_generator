import signal
import sys
from sympy import isprime

primes = []

n = 2

paused = False

def pause_handler(signum, frame):
    global paused
    paused = True
    print("\nPaused. Press 'v' to view primes, 'c' to continue, 'q' to quit.")

signal.signal(signal.SIGINT, pause_handler)

def display_menu():
    global paused
    while paused:
        choice = input("\nEnter option ('v' to view primes, 'c' to continue, 'q' to quit): ").lower()
        if choice == 'v':
            print("\nHere is the list of primes found so far:")
            print(primes)
        elif choice == 'c':
            paused = False 
        elif choice == 'q':
            print("Goodbye")
            sys.exit(0)  
        else:
            print("Invalid option. Please enter 'v', 'c', or 'q'.")


while True:
    if not paused:
                    # the formula 2^(2n - 1) - 1
        candidate = 2 ** (2 * n - 1) - 1
        if isprime(candidate):
            print(f"Found prime: {candidate}")
            primes.append(candidate)  
        n += 1
    else:
        display_menu()  




