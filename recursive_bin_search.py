def recursive_bin_search(test_list, target):
	if not test_list:
		return False
	else:
		midpoint = (len(test_list)) // 2
		
		if test_list[midpoint] == target:
			return True
		else:
			if test_list[midpoint] < target:
				return recursive_bin_search(test_list[midpoint+1:], target)
			else:
				return recursive_bin_search(test_list[:midpoint], target)

def verify(result):
	print("Target found: " + str(result))

numbers = [1,2,3,4,5,6,7,8]
result = recursive_bin_search(numbers, 4)
verify(result)

