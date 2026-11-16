from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Stage 1: Search for the node
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Stage 2: Node found, handle the 3 deletion cases
            
            # Case 1 & 2: Node has 0 or 1 child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # Case 3: Node has 2 children
            # Find the inorder successor (smallest value in the right subtree)
            successor = self.findMin(root.right)
            # Copy the successor's value to the current node
            root.val = successor.val
            # Delete the duplicate successor node from the right subtree
            root.right = self.deleteNode(root.right, successor.val)
            
        return root

    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node
