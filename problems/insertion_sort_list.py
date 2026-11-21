# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:

        dummy = ListNode()
        curr = head
        while curr:
            prev = dummy
            next_node = curr.next

            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            curr.next = prev.next
            prev.next = curr
            curr = next_node

        return dummy.next


s = Solution()
print(s.insertionSortList(ListNode[4, 2, 1, 3]))
