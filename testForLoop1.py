'''while True:
	line = input('>\n')
	if line == 'done':
		break'''
		

while True:
	line = input('>')
	if line[0]=='#':
		continue
	if line == 'stop':
		break
	print(line)
print('Done')

