
import math


def is_palindrome_num(n:int)->bool:
    if n <=0:
        return n == 0
    
    n_length = math.floor(math.log10(n)) + 1
    x = 10**(n_length-1)

    for i in range(n_length // 2):
        if n // x != n%10:
            return False
        n %= x #remove the msb
        n //= 10 #remvoe the lsb
        x //=100
    return True 

ans = is_palindrome_num(157751)
print(ans)

``