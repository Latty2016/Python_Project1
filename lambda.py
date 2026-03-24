
# difference between normal function and lambda function
# normal function has a name and uses return
# lambada has no name and no return --- it return automatically

 # def name(arguments): return expression  VS   lambada arguments: expression    
   
	
	
def double(x):
	return x * 2
		
print(double(5))

print('******************************************')
number = lambda x: x * 2
print(number(3))

print('******************************************')
def is_even(x):
	return x % 2 == 0
	
print(is_even(6))

print('******************************************')
even = lambda x: x % 2 == 0
print(even(7))