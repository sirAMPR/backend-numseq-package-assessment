def primes(n):
    """Returns a list of prime nubmers less than n"""
    return [i for i in range(n) if is_prime(i)]


def is_prime(m):
    """Returns a boolean indication weather m is a prime number"""
    if m < 2:
        return False
    elif m == 2:
        return True
    for n in range(2, m):
        if m % n == 0:
            return False
    return True
