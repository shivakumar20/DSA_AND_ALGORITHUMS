# Leet Code link : https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the starting point of the result list
        Head = ListNode()
        
        # Pointer to traverse and build the result linked list
        ans = Head
        
        # Variable to store the carry value from summation
        carry = 0

        # Loop through both lists while there are nodes left OR there's a carry
        while l1 or l2 or carry:
            # Get values from the current nodes, defaulting to 0 if the node is None
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Compute sum of both digits along with any existing carry
            sum = x + y + carry

            # Update carry for the next iteration
            carry = sum // 10

            # Create a new node with the last digit of the sum and attach it to result list
            ans.next = ListNode(sum % 10)

            # Move ans pointer forward
            ans = ans.next

            # Move l1 and l2 pointers forward if they exist
            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next

        # Return the actual result list (skipping the dummy node)
        return Head.next
