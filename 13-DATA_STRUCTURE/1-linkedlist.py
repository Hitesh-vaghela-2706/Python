# creating a class for nodes
class Node:
	def __init__(self, data):# Function to initialise the node object
		self.data = data # assign A data 
		self.next = None # assign a next pointer none bcz created empty linkedlist

# Linked List class contains a Node object	
class LinkedList:
	def __init__(self): 
		self.head = None #assign a head none bcz created a empty linkedlist
		
	# function for printing elements of linkedlist
	def printList(self):
		print("linkedlist is ",end=' ')
		temp = self.head
		while (temp):
			print (temp.data,end=',')
			temp = temp.next
			
if __name__=='__main__':
	#creating Nodes
	llist = LinkedList()
	llist.head = Node(12)
	second = Node(32)
	third = Node(37)
	fourth = Node(24)
	fifth = Node(59)
	# linking Nodes
	llist.head.next = second
	second.next = third
	third.next = fourth
	fourth.next = fifth
	llist.printList()
