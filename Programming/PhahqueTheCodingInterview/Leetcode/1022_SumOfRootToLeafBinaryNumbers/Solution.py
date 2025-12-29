# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# store the path to the nodes using a dictionary
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        pathToNode = {}
        pathToNode[root] = str(root.val)
        frontier = []
        frontier.append(root)
        sum = 0
        while (len(frontier) > 0):
            expand = frontier.pop()
            pathToCur = pathToNode[expand]
            if expand.left is None and expand.right is None:
                sum += int("0b"+pathToCur, 2)
            if expand.left is not None:
                pathToNode[expand.left] = pathToCur+str(expand.left.val)
                frontier.append(expand.left)
            if expand.right is not None:
                pathToNode[expand.right] = pathToCur+str(expand.right.val)
                frontier.append(expand.right)
        return sum
