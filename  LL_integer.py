class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def print_list(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.value))
            current = current.next
        return " <-> ".join(result)

def integer_to_linked_list(n):
    dll = DoublyLinkedList()
    num_str = str(n)
    
    if num_str[0] == '-':  # If number is negative
        dll.append('-')
        num_str = num_str[1:]  # Remove the negative sign for processing

    for digit in num_str:
        dll.append(int(digit))  # Append each digit as an integer

    return dll

def linked_list_to_integer(dll):
    if not dll.head:
        return 0

    num_str = ""
    current = dll.head
    while current:
        num_str += str(current.value)
        current = current.next

    return int(num_str)  # Convert string back to integer

n1 = 25
dll1 = integer_to_linked_list(n1)
print("Linked List Representation:", dll1.print_list())

n2 = -4
dll2 = integer_to_linked_list(n2)
print("Linked List Representation:", dll2.print_list())

print("Extracted Integer:", linked_list_to_integer(dll1)) 
print("Extracted Integer:", linked_list_to_integer(dll2)) 
