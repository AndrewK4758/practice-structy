class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(self, root) -> list[int]:
    res = []
    def inorder(root):
        if not root:
            return
        
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)
    inorder(root)
    return res

print(inorderTraversal([1,2,3]))