def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

# def get_primes(n):
   # primes = []
  #  for i in range(2, n+1):
      #  if is_prime(i):
       #     primes.append(i)
 #   return primes

def get_primes(start, end):
    primes = []
    for i in range(start, end+1):
        if is_prime(i):
            primes.append(i)
    return primes


def sort_descending(primes):
    return sorted(primes, reverse=True)

def find_largest_prime(n):
    if not isinstance(n, int) or n < 1:   # Checking object using instance built in method
        raise TypeError("Input Must be a positive Integer")
    try:
        primes = sort_descending(get_primes(n))
        for prime in primes:
            if prime <= n:
                return prime

    except:
        pass
    return None

print(find_largest_prime(20))
print(get_primes(12,22))
