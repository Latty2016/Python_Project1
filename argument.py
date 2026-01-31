# playing with parameters

'''def adding(a,b,c):
	addition = a+b+c
	return addition
	
x = adding(5,6,4)
print(x)'''

def computePay(hours, rate):

	if hours > 40:
		pay = (hours-40)*(rate*0.5)+ (hours * rate)
	else:
		pay = hours*rate	
	return pay
	
stringHour = input("Enter the total hours you worked: " )
stringRate = input("Enter the rate: ")	
floatHours = float(stringHour)
floatRate = float(stringRate)

print("Pay", computePay(floatHours,floatRate))