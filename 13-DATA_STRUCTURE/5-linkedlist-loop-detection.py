class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
class LinkedList:
	def __init__(self):
		self.head = None
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data, end=" ")
			temp = temp.next
	# Function for detect loop in linkedlist
	def detectLoop(self):
		s = set() #create a empty set
		temp = self.head
		while (temp):
			if (temp in s):
				return True
			s.add(temp) #adding each new element in set
			print("set is " , s) # printing set
			temp = temp.next
		return False


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
llist.head.next.next.next.next = llist.head
if(llist.detectLoop()):
	print("Loop found")
else:
	print("No Loop ")