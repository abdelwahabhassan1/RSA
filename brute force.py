import random
take_bits = int(input("How many bits do you want: "))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):         #calculates the modular inverse of a modulo m.
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def brute_force_private_exponent(N, e):              # assume the private exponent d is smaller than N
    for d in range(2, N):
        if (e * d) % N == 1:
            return d
    return None

def generate_rsa_keys(bit_size):      # Generate two random prime numbers p and q
    p = random.randrange(2**(bit_size//2 - 1), 2**(bit_size//2))
    q = random.randrange(2**(bit_size//2 - 1), 2**(bit_size//2))
    N = p * q            # Calculate modulus N
    phi = (p - 1) * (q - 1)       
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    d = mod_inverse(e, phi)         # Calculate private exponent d using the modular inverse of e mod phi
    return (N, e), (N, d)              # Return public and private keys
