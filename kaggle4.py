

def menu_is_boring(meals):
    # Iterate over all indices of the list, except the last one
	for i in range(len(meals)-1):
		if meals[i] == meals[i+1]:
			return True
	return False
	# Call the function and print the result
first_food = ["Pizza","Burger","Sushi","Pasta","Fried Rice"]
second_food = ["Pizza","Burger","Burger","Pasta","Burger","Fried Rice"]
print('Latif`s Food -'*5)
result1 = menu_is_boring(first_food)
print(result1)
print('Yusuf`s Food -'*5)
result2 = menu_is_boring(second_food)
print(result2)