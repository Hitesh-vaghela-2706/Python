class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
        
class LinkedList:
	def __init__(self):
		self.head = None

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data) # creating a new node	
		new_node.next = self.head # Make next of new Node as head
		self.head = new_node # Make new Node as new head  

	# Function to Inserts a new node after the given prev_node.
	def insertAfter(self, prev_node, new_data):
		#check if the given prev_node exists
		if prev_node is None:
			print("The given previous node must inLinkedList.")
			return
		new_node = Node(new_data)
		new_node.next = prev_node.next #link new node with privios node's next
		prev_node.next = new_node #link privious node with new node

	#Function to Append a new node at the end.
	def append(self, new_data):
		new_node = Node(new_data)
		# checking if linkedlist is empty set new node as head
		if self.head is None:
			self.head = new_node
			return
		# if linkedlist is not empty traver till 
		temp = self.head
		while (temp.next):
			temp = temp.next
		# after reaching at end link new node with privious
		temp.next = new_node

	
	def printList(self):
		temp = self.head
		while (temp):
			print(temp.data,end=" ")
			temp = temp.next
if __name__=='__main__':
	llist = LinkedList()
	llist.append(6)
	llist.push(7)
	llist.push(1)
	llist.append(4)
	llist.insertAfter(llist.head.next, 8)
	print('Created linked list is: ')
	llist.printList()