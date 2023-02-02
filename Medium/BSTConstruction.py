# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        current_node = self
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:
                    current_node = current_node.right

        return self

    def contains(self, value):
        # Write your code here.
        current_node = self

        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True
        return False

    def remove(self, value, parent=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        current_node = self

        while current_node is not None:
            if value < current_node.value:
                parent = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent = current_node
                current_node = current_node.right
            else:
                # Total 4 cases to handle.
                # 1. When the toBeRemovedNode has both child nodes
                if current_node.left is not None and current_node.right is not None:
                    current_node.value = current_node.right.getSmallestValue()
                    current_node.right.remove(current_node.value, current_node)
                elif parent is None:
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                    else:
                        pass
                elif parent.left == current_node:
                    parent.left = current_node.left if current_node.left is not None else current_node.right
                elif parent.right == current_node:
                    parent.right = current_node.left if current_node.left is not None else current_node.right
                break
        return self

    def getSmallestValue(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
