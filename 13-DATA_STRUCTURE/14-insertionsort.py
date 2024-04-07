# Python program for implementation of Insertion Sort Function to do insertion sort

def insertionsort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>= 0 and key< arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = key
            # print(arr) it is just for explaination howe it works
arr = [12,11,13,5,6]
insertionsort(arr)
print("array is --> ",arr)