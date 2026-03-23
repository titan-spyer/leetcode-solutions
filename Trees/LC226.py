# LC 226 Invert Binary Tree 
def invertTree(root):
    if root == None:
        return None
    invertTree(root.left)
    invertTree(root.right)
    root.left, root.right = root.right, root.left
    return root