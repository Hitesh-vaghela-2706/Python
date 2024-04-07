# You are assigned to put some amount of boxes onto one truck. You are given
#  a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
# numberOfBoxesi is the number of boxes of type i.
# numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize, which is the maximum number of 
# boxes that can be put on the truck. You can choose any boxes to put on the 
# truck as long as the number of boxes does not exceed truckSize.
# Return the maximum total number of units that can be put on the truck.
# Example 1:
# Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
# Output: 8

boxTypes = [[3,1],[1,3],[2,2]] #[box,unit]
truckSize = 4
boxTypes.sort(reverse=True,key = lambda x:x[1])
print(boxTypes) #converts into sorted[unit,box]
ans = 0
for i in boxTypes:
    if truckSize>=i[0]:
        truckSize-=i[0]
        ans +=(i[0]*i[1])
        continue
    if truckSize<i[0] and truckSize!=0:
        ans += (truckSize*i[1])
        break
print(ans)