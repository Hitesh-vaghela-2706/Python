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

	def deleteNode(self, key):
		temp = self.head
		# if key at head position we need to change head 
		# after delete a node so we need to seperate this condition
		if (temp is not None):
			if (temp.data == key):
				self.head = temp.next #new head pointed
				temp = None # unlink or delete privious head node
				return

		# cheking for other nodes after head and matching with key
		while(temp is not None):
			if temp.data == key:
				break
			prev = temp #storing privious node for pointing next node after deletation
			temp = temp.next #checking all elements of linked list

		# chacking if key is not  in linkedlist
		if(temp == None):
			return

		prev.next = temp.next # link privious and next node of deleted node
		temp = None # unlink or delete privious head node

	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data,end='\t')
			temp = temp.next

llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
print("Created Linked List: ")
llist.printList()
llist.deleteNode(1)
print("\nLinked List after Deletion of 1:")
llist.printList()