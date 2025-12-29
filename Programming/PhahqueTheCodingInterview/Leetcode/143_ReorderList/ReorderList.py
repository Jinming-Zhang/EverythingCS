
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        str(self.val)

    def __str__(self) -> str:
        str(self.val)

    def fromList(lst):
        if len(lst) == 0:
            return None
        head = ListNode(lst[0])
        cur = head
        for i in range(1, len(lst)):
            newNode = ListNode(lst[i])
            cur.next = newNode
            cur = newNode
        return head

    def toList(self):
        res = [self.val]
        cur = self.next
        while (cur != None):
            res.append(cur.val)
            cur = cur.next
        return res


class Solution(object):
    def reorderList(self, head: ListNode):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head == None:
            return None
        if head.next == None:
            return head
        if head.next.next == None:
            return head

        curHead = head
        curTail = curHead
        preTail = curTail
        while (curTail.next != None):
            preTail = curTail
            curTail = curTail.next

        nextHead = head.next
        head.next = curTail
        preTail.next = None
        curTail.next = nextHead
        self.reorderList(nextHead)


# lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
lst = [1, 2, 3, 4]
lstHead = ListNode.fromList(lst)
Solution().reorderList(lstHead)
print(lstHead.toList())
