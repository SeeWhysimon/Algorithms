from TreeAlgorithms import Solution, TreeNode

solution = Solution()

root1 = TreeNode(val=1)
root11 = TreeNode(val=2)
root12 = TreeNode(val=2)
root21 = TreeNode(val=3)
root22 = TreeNode(val=4)
root23 = TreeNode(val=4)
root24 = TreeNode(val=3)

root1.left = root11
root1.right = root12
root11.left = root21
root11.right = root22
root12.left = root23
root12.right = root24

print(solution.inorderTraversal(root=root1))