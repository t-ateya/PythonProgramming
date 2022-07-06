import math

def paint_cal(height, width, cover):
	area = height*width
	num_of_cans = area/cover
	return math.ceil(num_of_cans)

#print(paint_cal(5,1,2))

def prime_num(number):
	count = 0
	divide_by = 1
	while divide_by < number:
		if number % divide_by ==0:
			count +=1
		divide_by +=1
	if count == 1:
		print(f"{number} is prime")
	else:
		print(f"{number} is not prime")
		
prime_num(5)
