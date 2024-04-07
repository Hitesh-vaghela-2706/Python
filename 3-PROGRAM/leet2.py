# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit.
#  Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

#if list is given then use this code 
# but when linked list is given this code is not valid
A = [0,0,3]
B = [2,3,3]
a = ''
b = ''
for i in A:
    i = str(i)
    a = a + i
for i in B:
    i = str(i)
    b = b + i
a = a[::-1] 
b = b[::-1]
c = int(a) + int(b)
d = str(c)
d = d[::-1]
x = []
for i in d:
    x.append(i)
print(x)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_s = ''
        l2_s = ''
        while l1 is not None:
            l1_s = f'{l1.val}{l1_s}'
            l1 = l1.next
        while l2 is not None:
            l2_s = f'{l2.val}{l2_s}'
            l2 = l2.next
        l3_s = str(int(l1_s) + int(l2_s))
        l3 = None
        for n in l3_s:
            l3 = ListNode(n, l3)
        return l3