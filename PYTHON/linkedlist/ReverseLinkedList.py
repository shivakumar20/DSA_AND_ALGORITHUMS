# Leet Code: https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize the previous pointer to None (this will be the new tail of the reversed list)
        prev = None

        # Start with the head of the original list
        current = head

        # Traverse the list until we reach the end
        while current:
            # Store the next node before changing the link
            Next = current.next

            # Reverse the current node's pointer to point to the previous node
            current.next = prev

            # Move previous to the current node (new previous for the next iteration)
            prev = current

            # Move to the next node in the original list
            current = Next

        # At the end, prev will be the new head of the reversed list
        return prev
