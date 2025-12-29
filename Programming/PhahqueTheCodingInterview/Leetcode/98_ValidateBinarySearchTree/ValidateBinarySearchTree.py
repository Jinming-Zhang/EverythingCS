from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverseTree(self, root):
        lst = []
        if (root.left != None):
            lst.extend(self.traverseTree(root.left))
        lst.append(root.value)
        if (root.right != None):
            lst.extend(self.traverseTree(root.right))
        return lst

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if (root == None):
            return True
        lst = self.traverseTree(root)
        for i in range(1, len(lst)):
            if (lst[i] <= lst[i-1]):
                return False
        return True
