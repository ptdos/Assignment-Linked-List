class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_nodes(self, values_to_remove):
        values_set = set(values_to_remove)   
        dummy = Node(0)  
        dummy.next = self.head
        prev, current = dummy, self.head
        
        while current:
            if current.value in values_set:
                prev.next = current.next  
            else:
                prev = current  
            current = current.next
        
        self.head = dummy.next  

    def print_list(self):
        current = self.head
        result = []
        while current:
            result.append(current.value)
            current = current.next
        return result


def create_linked_list(values):
    ll = LinkedList()
    for value in values:
        ll.append(value)
    return ll


array1 = [1, 2, 3]
linked_list1 = create_linked_list([1, 2, 3, 4, 5])
linked_list1.delete_nodes(array1)
print("Output:", linked_list1.print_list()) 

array2 = [5]
linked_list2 = create_linked_list([1, 2, 3, 4])
linked_list2.delete_nodes(array2)
print("Output:", linked_list2.print_list()) 
