import decimal 
from decimal import Decimal
decimal.getcontext().prec = 2 #global(default) context now has precision set to 2

a = Decimal('0.12345')
b = Decimal('0.12345')
print(a+b)
