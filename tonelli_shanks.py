
# Step 1: Decompose p-1 into Q * 2^S

def decompose(p):
    q = p - 1
    s = 0

    while q % 2 == 0:
        q = q // 2
        s = s + 1

    return q, s


# Step 2: Find Quadratic Non-Residue

def find_non_residue(p):
    z = 2

    while pow(z, (p - 1) // 2, p) != p - 1:
        z = z + 1

    return z


# Step 3: Initialize Variables

def initialize(a, p, q, s, z):
    m = s
    c = pow(z, q, p)
    t = pow(a, q, p)
    r = pow(a, (q + 1) // 2, p)

    return m, c, t, r


# Step 4: Perform One Tonelli-Shanks Iteration

def tonelli_iteration(p, m, c, t, r):

    i = 0

    while i < m and pow(t, 2**i, p) != 1:
        i = i + 1

    if i == m:
        raise ValueError("No valid i found")

    b = pow(c, 2**(m - i - 1), p)

    r = (r * b) % p
    t = (t * b * b) % p
    c = (b * b) % p
    m = i

    return m, c, t, r


# Step 5: Complete Tonelli-Shanks Algorithm

def tonelli_shanks(a, p):

    a = a % p

    # Handle zero
    if a == 0:
        return [0]

    # Check Euler's Criterion
    if pow(a, (p - 1) // 2, p) != 1:
        return None

    # Decompose p-1
    q, s = decompose(p)

    # Find non-residue
    z = find_non_residue(p)

    # Initialize
    m, c, t, r = initialize(a, p, q, s, z)

    # Repeat iterations until t becomes 1
    while t != 1:
        m, c, t, r = tonelli_iteration(p, m, c, t, r)

    # Return both roots
    root1 = r
    root2 = (p - r) % p

    if root1 == root2:
        return [root1]

    return sorted([root1, root2])


