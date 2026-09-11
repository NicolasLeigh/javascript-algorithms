class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True

        def is_mirror(left, right):
            if left is None and right is None:
                return True

            if left is None or right is None:
                return False

            if left.val != right.val:
                return False

            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

        return is_mirror(root.left, root.right)