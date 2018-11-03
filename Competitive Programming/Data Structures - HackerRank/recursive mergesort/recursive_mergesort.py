def recMergeSort(array):
	if len(array) is 1 or 0:
		return array
	try:
		midpt = array[len(array)//2]
		leftArray = recMergeSort([i for i in array if i<midpt])
		rightArray = recMergeSort([i for i in array if i>midpt])
		return recMergeSort(leftArray) + recMergeSort([midpt]) + recMergeSort(rightArray)
	except IndexError:
		return array

print(recMergeSort([6,9,8,1,5]))
print(recMergeSort([19,11,12,1,2,20,22,24,25]))