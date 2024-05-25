class Node:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2
        self.next = None

    def __str__(self):
        return f"({self.data1}, {self.data2})"

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data1, data2):
        new_node = Node(data1, data2)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current))
            current = current.next
        return " -> ".join(nodes)

def merge_linked_lists(list1, list2):
    current1 = list1.head
    while current1:
        current2 = list2.head
        while current2:
            if current1.data1 == current2.data1:
                current1.data2 += current2.data2
                break
            current2 = current2.next
        current1 = current1.next

# Example usage
if __name__ == "__main__":
    list1 = SinglyLinkedList()
    list1.append(1, 100)
    list1.append(2, 200)
    list1.append(3, 300)
    print("List 1:", list1)

    list2 = SinglyLinkedList()
    list2.append(2, 50)
    list2.append(3, 30)
    list2.append(4, 400)
    print("List 2:", list2)

    merge_linked_lists(list1, list2)
    print("Merged List:", list1)

