def findClosestValueInBst(tree, target):
    # Write your code here.
    current_node = tree
    closest_node_value = tree.value

    while current_node is not None:
        if abs(target - current_node.value) < abs(target - closest_node_value):
            closest_node_value = current_node.value
        if target > current_node.value:
            current_node = current_node.right
        elif target < current_node.value:
            current_node = current_node.left
        else:
            break

    return closest_node_value


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
