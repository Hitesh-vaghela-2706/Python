def search(arr, n, x):

	for i in range(0, n):
		if (arr[i] == x):
			return i
	return -1

# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10
n = len(arr)

# Function call
result = search(arr, n, x)
if(result == -1):
	print("Element is not present in array")
else:
	print("Element is present at index", result)


# if duplicate elements are presernt...
def search1(array,n,key):
	f = []
	if key not in array:
		return -1
	for i in range(0,n):
		if(array[i] == key):
			f.append(i)
	return f
	
array = [1,2,3,4,5,3,4,3,2]
n = len(array)
key = 3
res = search1(array,n,key)
if(res == -1):
	print("Element is not present in array")
else:
	print(f"Element {key} is present at index")
	for i in res:
		print(i,end=" ")
