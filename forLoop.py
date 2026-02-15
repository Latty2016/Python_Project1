'''for i in [5,2,3,7,5,6,'latif','altay','Ali']:
	print(i)
print('Loop is done...')'''


'''friends = ['Ali','Kasim','Tom']
for fried in friends:
	print('Hello',fried)
print('Loop is done...')'''


'''largestsofar=0
print('Before the loop, the largest so far is: ',largestsofar)
numbers=[9, 41, 12, 3, 74, 15,100]
for num in numbers:
	if num > largestsofar:
		largestsofar=num
print('Afer the loop, the largets number is:',largestsofar)'''

'''count = 0
for numbers in [9, 41, 12, 3, 74, 15]:
	count = count + 1
	print(numbers)
print('The total loop through is: ',count)'''

'''sum = 0
for numbers in [9, 41, 12, 3, 74, 15]:
	sum = numbers + sum
print('The total addition of all the loop is: ',sum)'''

'''count = 0
sum = 0
for numbers in [9, 41, 12, 3, 74, 15]:
	count = count + 1
	sum = numbers + sum
print('The average of the loop is:',sum/count)'''

found = False
print('no value to find')
for numbers in [9, 41, 12, 3, 74, 15]:
	if numbers==41:
		found=True
print('I found the value',found)


