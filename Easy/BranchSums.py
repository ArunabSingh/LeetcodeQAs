# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    current_sum = 0
    branch_sums = []
    branchSumsHelper(root, current_sum, branch_sums)
    return branch_sums


def branchSumsHelper(node, current_sum, branch_sums):
    if node is None:
        return
    new_sum = current_sum + node.value
    if node.left is None and node.right is None:
        branch_sums.append(new_sum)
        return

    branchSumsHelper(node.left, new_sum, branch_sums)
    branchSumsHelper(node.right, new_sum, branch_sums)
