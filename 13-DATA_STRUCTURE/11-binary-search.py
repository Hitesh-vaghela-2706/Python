# for binary search array must be sorted if not then 
# first we need to sort array and then apply binary search
def binarySearch (arr, l, r, key):
	if r >= l:
		mid = l + (r - l) // 2
		if arr[mid] == key:
			return mid
		elif arr[mid] > key:
			return binarySearch(arr, l, mid-1, key)
		else:
			return binarySearch(arr, mid + 1, r, key)
	else:
		return -1

arr = [ 2, 3, 4, 10, 40 ]
key = 10
start_index = 0
end_index = len(arr) - 1
result = binarySearch(arr, start_index, end_index, key)

if result != -1:
	print ("Element is present at index % d" % result)
else:
	print ("Element is not present in array")