# Python program for implementation of Selection Sort
A = [64, 25, 12, 22, 11]
for i in range(len(A)):
	min_idx = i # consider i as min and Find the minimum element in remaining unsorted array
	for j in range(i+1, len(A)):
		if A[min_idx] > A[j]:
			min_idx = j		
	# Swap the found minimum element with the first element	
	A[i], A[min_idx] = A[min_idx], A[i]
print ("Sorted array",A)
