# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:

        if head is None:
            return None

        current = head
        prev = None

        while current:
            if current.val == val:
                temp = current.next
                if prev is None:
                    head = temp
                else:
                    prev.next = temp
                current = temp
            else:
                prev = current
                current = current.next
        return head
