from linkedlist import LinkedList

# Create a linked list
ll = LinkedList()

# Insert some values
ll.insert(10)
ll.insert(5)
ll.insert(15)
ll.insert(3)
ll.insert(7)

# Search for values
print("Searching for 5:", ll.search(5))  # Should return True
print("Searching for 8:", ll.search(8))  # Should return False

# Delete a value
ll.delete(10)

# Traverse and print the linked list
values = ll.traverse()
print("Values in linked list:", values)
