import random
import math
import time

take_bits = int(input("How many bits do you want: "))
message = int(input("Enter message: "))

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if num % 2 != 0:
            if is_prime(num):
                return num

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def generate_keys(bits):
    start_time = time.perf_counter() # Start measuring time
    p = generate_prime(bits // 2 + 1)
    q = generate_prime(bits - (bits // 2 + 1))
    
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    _, d, _ = extended_gcd(e, phi)
    d %= phi
    if d < 0:
        d += phi
    end_time = time.perf_counter()
    public_key = (n, e)
    private_key = (n, d)
    return public_key, private_key, end_time - start_time


def factor_modulus(N):
    sqrt_N = int(math.sqrt(N)) + 1
    for i in range (2, sqrt_N):
        if N % i == 0:
            p = i
            q = N // i
            return p, q
    return None, None    
def encrypt(message, public_key):
    n, e = public_key
    encrypted_message = pow(message, e, n)
    return encrypted_message

def decrypt(encrypted_message, private_key):
    n, d = private_key
    decrypted_message = pow(encrypted_message, d, n)
    return decrypted_message          