# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        length = 1
        last = head

        while last.next:
            last = last.next
            length += 1

        k = k % length

        if k == 0:
            return head

        last.next = head

        steps_to_new_tail = length - k - 1
        curr = head

        for _ in range(steps_to_new_tail):
            curr = curr.next

        new_head = curr.next
        curr.next = None

        return new_head