# import numpy as np

# print('enter how many number you want to add  in array1')
# m = int(input("enter a number \n"))
# nums1 = []
# if(m <= 1000):
#     for i in range(0,m):
#         B = int(input("enter a value which you want to insert\n"))
#         nums1.insert(i,B)
#     print("array1 named nums1",np.array(nums1))
# else:
#     print("invalid length of array")

# print('enter how many number you want to add  in array2')
# n = int(input("enter a number \n"))
# nums2 = []
# if(n <= 1000):
#     for i in range(0,n):
#         D = int(input("enter a value which you want to insert\n"))
#         nums2.insert(i,D)
#     print("array1 named nums2",np.array(nums2))
# else:
#     print("invalid length of array")

# concate = np.concatenate((nums1,nums2),axis=0)
# print(concate)
# merged_array = np.sort(concate)
# print(merged_array)

# output = np.median(merged_array)
# print("median is " + output)
import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = np.array(nums1)
        nums2 = np.array(nums2)
        concate = np.concatenate((nums1,nums2),axis=0) 
        merged_array = np.sort(concate) 
        output = np.median(merged_array)     
        return output