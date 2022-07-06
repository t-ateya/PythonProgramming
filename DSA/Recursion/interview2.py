def power(base, exp):
    """Returns the base to the power exp of any given two numbers"""
    assert exp >= 0 and int(
        exp) == exp, "Sorry! The pow must be positive integer"
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    return base*power(base, exp-1)


print(power(-2.5, 5))
