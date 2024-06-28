class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.sumNumbersHelper(root, 0)

    def sumNumbersHelper(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0
        sum = sum * 10 + root.val
        if root.left is None and root.right is None:
            return sum
        return self.sumNumbersHelper(root.left, sum) + self.sumNumbersHelper(root.right, sum)