# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.new_tree = TreeNode(0)
        self.temp = self.new_tree
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if root is not None:
                self.increasingBST(root.left)
                self.temp.right = TreeNode(root.val)
                self.temp = self.temp.right
                self.increasingBST(root.right)
        
        inorder(root)
        
        return self.new_tree.right