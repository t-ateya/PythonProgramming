def sum_of_digits(n):
    assert n >= 0 and int(n) == n, "The number has to be positive integer"

    if n % 10 == n:
        return n
    else:
        return sum_of_digits(int(n/10)) + (n % 10)


print(sum_of_digits(1234))
