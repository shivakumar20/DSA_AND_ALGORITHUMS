#Leet code Link https://leetcode.com/problems/reorder-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Step 1: Find the middle of the linked list using slow and fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the linked list
        second = slow.next  # Start of the second half
        slow.next = None  # Break the list into two halves
        
        prev = None  # Previous pointer for reversal
        while second:
            Next = second.next  # Store next node
            second.next = prev  # Reverse the link
            prev = second  # Move prev to current node
            second = Next  # Move to next node
        
        # Step 3: Merge the two halves
        first, second = head, prev  # First half and reversed second half

        while second:
            temp1, temp2 = first.next, second.next  # Store next nodes

            first.next = second  # Link first half node to second half node
            second.next = temp1  # Link second half node to next first half node

            first = temp1  # Move to next node in first half
            second = temp2  # Move to next node in second half
