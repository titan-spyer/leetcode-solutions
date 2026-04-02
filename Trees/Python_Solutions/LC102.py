from collections import deque

root = root = [3,9,20,'null','null',15,7]

def levelOrder(root):
    if root is None:
        return []
    queue = deque([root])
    answer = []

    while queue:
        level_size = len(queue)
        level = []

        for i in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        answer.append(level)
    return 0

print(levelOrder(root))