def height(root):
    if root is None:
        return -1
    else:
        return max(height(root.left),height(root.right))+1
