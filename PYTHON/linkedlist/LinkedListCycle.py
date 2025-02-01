# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # If the linked list is empty, there is no cycle
        if head is None:
            return False

        # Initialize two pointers: slow moves one step, fast moves two steps
        slow = head
        fast = head.next

        # Traverse the linked list
        while slow is not None and fast is not None:
            # If fast reaches the end (i.e., no cycle exists)
            if fast is None or fast.next is None:
                return False

            # If slow and fast meet, a cycle is detected
            if slow == fast:
                return True

            # Move slow one step and fast two steps
            slow = slow.next
            fast = fast.next.next

        # If the loop exits, no cycle was found
        return False
