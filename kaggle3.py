def elementwise_greater_than(L, thresh):
	#L = [1, 2, 3, 4]
	#thresh = 3
	#empty list to store the elements in L
	res = []
	for ele in L:
		res.append(ele > thresh)
		# return(ele>thresh for ele in L)
	return res
# Call the function and print the result
result = elementwise_greater_than([1, 2, 3, 4], 3)
print(result)