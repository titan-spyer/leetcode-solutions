# LC 104 MAXIMUM DEPTH OF BINARY TREE

root = [3,9,20,'null','null',15,7]
def maxDepth(root):
    if root.val is None:
        return 0
    
    left_depth = self.maxDepth(root.left)
    right_depth = self.maxDepth(root.right)
    return 1 + max(left_depth, right_depth)

print(maxDepth(root))