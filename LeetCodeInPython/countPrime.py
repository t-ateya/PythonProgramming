"""
#204
    Count the number of prime numbers less than a given number N
"""

def count_number_prime(n):
    """Returns the number of primes less than n"""
    if n in range(0,3):
        return 0
    if n == 3:
        return 1
    count = 0
    for num in range(2, n):
        if num == 2:
            count +=1
        if num == 3:
            count +=1

        if (num % 2 !=0 and num%3 != 0):
            count +=1
    return count

print(count_number_prime(12))