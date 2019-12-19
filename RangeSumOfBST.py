class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class RangeSumOfBST:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        return self.getRangeSum(root, L, R)

    def getRangeSum(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0
        elif root.val < L:
            result = self.getRangeSum(root.right, L, R)
        elif root.val > R:
            result = self.getRangeSum(root.left, L, R)
        else:
            result = self.getRangeSum(root.left, L, R) + self.getRangeSum(root.right, L, R) + root.val

        return result


if __name__ == "__main__":
    tree = TreeNode(10)
    tree.left = TreeNode(5)
    tree.left.left = TreeNode(2)
    tree.left.right = TreeNode(7)
    tree.right = TreeNode(15)
    assert (RangeSumOfBST().rangeSumBST(tree, 2, 9) == 14)
