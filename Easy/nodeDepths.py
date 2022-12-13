def nodeDepths(root):
    # Write your code here.
    sum_depths = 0
    total_depth = nodeDepthsHelper(root, sum_depths)
    return total_depth


# O(n) time O(h) Space: h(height of BT) function calls
def nodeDepthsHelper(node, depth):
    if node is None:
        return 0
    return depth + nodeDepthsHelper(node.left, depth + 1) + nodeDepthsHelper(node.right, depth + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
