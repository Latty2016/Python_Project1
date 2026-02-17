fruit = 'bananas'
print(fruit)
letter = fruit[3]
print(letter)

x = 3
print(fruit[x-3])
print('******************************************')

# len() gives the length of the a string
print(len(fruit))
print('******************************************')

for letter in fruit:
	print(letter)

print('******************************************')
count = 0
for letter in fruit:
	if letter == 'a':
		count = count + 1
print(count)

