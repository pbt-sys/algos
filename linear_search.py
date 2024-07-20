def linear_search(test_list, target):
	"""
	returns the position of the target value if found. 
	else returns None
	"""
	
	for i in range(len(test_list)):
		if test_list[i] == target:
			return i

def verify(index):
	if index is not None:
		print("Target found at index " + str(index))
	else:
		print("Target not in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 6)
verify(result)

