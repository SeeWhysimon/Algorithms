from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def predorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root:
            result.append(root.val)
            result.extend(self.predorderTraversal(root.left))
            result.extend(self.predorderTraversal(root.right))
        return result
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root:
            result.extend(self.postorderTraversal(root.left))
            result.extend(self.postorderTraversal(root.right))
            result.append(root.val)
        return result
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root:
            result.extend(self.inorderTraversal(root.left))
            result.append(root.val)
            result.extend(self.inorderTraversal(root.right))
        return result
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root:
            queue = deque([root]) # enabling efficient breadth-first traversal of the tree
            while queue:
                level_size = len(queue)
                curr_level = []
                for _ in range(level_size):
                    node = queue.popleft()
                    curr_level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                result.append(curr_level)
        return result
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = root.right, root.left
            root.left = self.invertTree(root.left)
            root.right = self.invertTree(root.right)
        return root
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root:
            queue = deque([root])
            while queue:
                level_size = len(queue)
                curr_level = []
                for _ in range(level_size):
                    node = queue.popleft()
                    curr_level.append(node.val) if node else None
                    queue.append(node.left) if node else None
                    queue.append(node.right) if node else None
                if len(curr_level) >= 2:
                    left = 0
                    right = len(curr_level) - 1
                    while left < right:
                        if curr_level[left] != curr_level[right]:
                            return False
                        left += 1
                        right -= 1
        return True
        