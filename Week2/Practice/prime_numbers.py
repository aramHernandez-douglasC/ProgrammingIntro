import math

# def prime_num(n: int):
#     # 0 is not
#     # 1 is not
#     # 2 is prime
#     def is_prime(x: int):
#         if x < 2:
#             return False
#         for index in range(2, int(math.sqrt(x)) + 1):
#             if x % index == 0:
#                 return False
#         return True
#
#     prime_numbers = []
#    for i in range(2, n + 1):
#         if(is_prime(i)):
#             prime_numbers.append(i)
#
#     return prime_numbers
#
# print(prime_num(100000000000))

# Mcp Model context procol
# langchain

def prime_nums(n):
    try:
        if n < 2:
            return []

        sieve = [True] * (n + 1)
        sieve[0:2] = [False, False]

        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False

        primes = []

        for i in range(2, n+1):
            if sieve[i]:
                primes.append(i)

        return primes
    except Exception as e:
        print(f"Something happened {e}")


print(prime_nums("A"))


