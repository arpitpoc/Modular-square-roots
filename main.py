import random


from prime_generator import generate_prime
from brute_force import brute_force
from euler_criterion import euler_criterion
from tonelli_shanks import tonelli_shanks
from tonelli_shanks import tonelli_shanks, find_non_residue

# Task A: Brute Force

print("\n----- TASK A: BRUTE FORCE -----")

p1 = int(input("Enter small prime p: "))
a1 = int(input("Enter value of a: "))

roots1 = brute_force(a1, p1)

print("Quadratic Roots:", roots1)

# Task B: Euler's Criterion

print("\n----- TASK B: EULER'S CRITERION -----")

p2 = int(input("Enter small prime p: "))
a2 = int(input("Enter value of a: "))

result2 = euler_criterion(a2, p2)

print("Euler's Criterion Result:", result2)

# Task C: Tonelli-Shanks

print("\n----- TASK C: TONELLI-SHANKS -----")

p3 = generate_prime()

x3 = random.randint(1, p3-1)

a3 = pow(x3, 2, p3)

roots3 = tonelli_shanks(a3, p3)

print("Generated Prime p:", p3)
print("Original x:", x3)
print("Calculated a:", a3)
print("Square Roots:", roots3)
print("Original x found:", x3 in roots3)

# Task D: Quadratic Non-Residue

print("\n----- TASK D: QUADRATIC NON-RESIDUE -----")

p4 = generate_prime()

a4 = find_non_residue(p4)

result4 = euler_criterion(a4, p4)

roots4 = tonelli_shanks(a4, p4)

print("Generated Prime p:", p4)
print("Quadratic Non-Residue a:", a4)
print("Euler Criterion Result:", result4)
print("Square Roots:", roots4)