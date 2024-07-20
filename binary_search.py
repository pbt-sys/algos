def binary_search(test_list, target):
	first = 0
	last = len(test_list) -1

	while first <= last:
		midpoint = (first + last) // 2
		
		if test_list[midpoint] == target:
			return midpoint
		elif test_list[midpoint] < target:
			first = midpoint + 1
		else:
			last = midpoint - 1

	return None

def verify(index):
	if index is not None:
		print("Index of target is: " + str(index))
	else:
		print("Target not in list")

numbers = [1,2,3,4,5,6,7,8]
target = int(input("Target: "))

result = binary_search(numbers, target)
verify(result)

