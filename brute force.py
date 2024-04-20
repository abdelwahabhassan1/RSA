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

 #Function to test brute force attack
def test_brute_force_attack(N, e):
    print("Original private exponent (d):", e)
    found_d = brute_force_private_exponent(N, e)
    if found_d is not None:
        print("Brute force found private exponent (d):", found_d)
    else:
        print("Brute force attack failed. Unable to find private exponent (d).")

# Example usage
bit_size_8 = 8
bit_size_16 = 16

print("Testing RSA with 8-bit key size:")
public_key, private_key = generate_rsa_keys(bit_size_8)
print("Public Key (N, e):", public_key)
print("Private Key (N, d):", private_key)
test_brute_force_attack(*private_key)

print("Testing RSA with 16-bit key size:")
public_key, private_key = generate_rsa_keys(bit_size_16)
print("Public Key (N, e):", public_key)
print("Private Key (N, d):", private_key)
test_brute_force_attack(*private_key)