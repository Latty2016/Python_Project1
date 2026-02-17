#slicing
string = 'monthly plan'
print(string[0:5])
print(string[8:25])
#concatination
a = 'latif'
b = 'altay'
print(a + ' ' + b)

# in logical operator
fruit = 'apple'
if 'a' in fruit:
	print('found it')
# lower(), upper()

greeting = 'how are you?'
print(greeting.upper())
# find()

fd = string.find('n')
print(fd)

# replace()
rp = string.replace('monthly','anual')
print(rp)
#lstrip() and rstrip() remove whitespace at the left or right
# strip() removes all spaces
#startwith()
line = 'i have a book'
line.startswith('p')
#
data = 'From stephen.marquard@uct.ac.za Sat Jan'
update = data.find('@')
print(update)