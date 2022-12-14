# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    current_node = linkedList
    while current_node is not None:
        while current_node.next is not None and current_node.value == current_node.next.value:
            if current_node.next.next is None:
                current_node.next = None
            else:
                current_node.next = current_node.next.next
        current_node = current_node.next
    return linkedList
