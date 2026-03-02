

def fashionable_late(arrivals, name):
	order = arrivals.index(name)
	return order>=len(arrivals)/2 and order !=len(arrivals)-1
	
	
arrivals = ['Paul', 'John', 'Ringo', 'George', 'Jen', 'Jamie']
#print(arrivals[3])
#print(len(arrivals))

print(f"Total guests      :{len(arrivals)}")
print(f"Midpoint          :{len(arrivals)/2}")
print(f"Last position     :{len(arrivals)-1}")
print('-'*40)

for name in arrivals:
	order = arrivals.index(name)
	result = fashionable_late(arrivals,name)
	if result:
		status = 'Fashionably Late!'
	elif len(arrivals)/2:
		status = 'Too Early'
	else:
		status = 'Too Late'
	print(f"{name:<10}	position {order}	>>>	{status}")