
# open('filename','mode') mode == 'r'/'w'

''' mfile = open('mbox.txt')
count = 0
for line in mfile:
	count = count + 1
print('Total line in the file is: ', count)'''

# reaing the file
''' mfile = open('mbox.txt')
rfile = mfile.read()
print(len(rfile))
print(rfile[:50])'''
# searching a file
''' mfile = open('mbox.txt')
for line in mfile:
	line = line.rstrip() # new line is considered as white spacea and it is stripped
	if line.startswith('From'):
		print(line)'''
# using in to select lines
''' mfile = open('mbox.txt')
for line in mfile:
	line = line.rstrip()
	if not '@uct.ac.za' in line:
		continue
	print(line)'''
# opening file and operate on it
fileName = input('Enter the file name: ')
try:
	openFile = open(fileName)
except:
	print('File cannot be found...',fileName)
	
count = 0
for line in openFile:
	if line.startswith('from'):
		count = count + 1
print('There were ', count, 'subject lines in', fileName)
	