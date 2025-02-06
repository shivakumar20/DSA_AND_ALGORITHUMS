# Leet code Link : https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create a dummy node to act as the starting point of the merged list
        d = ListNode()

        # Pointer 'cur' will be used to build the merged list
        cur = d

        # Iterate through both lists until one of them becomes empty
        while list1 and list2:
            # If list1's current node has a smaller value, append it to the merged list
            if list1.val < list2.val:
                cur.next = list1  # Link the smaller node
                cur = list1  # Move cur to the newly added node
                list1 = list1.next  # Move list1 pointer forward
            else:
                # If list2's current node is smaller or equal, append it to the merged list
                cur.next = list2  # Link the smaller node
                cur = list2  # Move cur to the newly added node
                list2 = list2.next  # Move list2 pointer forward

        # If one of the lists is not fully traversed, append the remaining nodes
        cur.next = list1 if list1 else list2

        # Return the merged list starting from the first real node (ignoring the dummy node)
        return d.next
        
    


                                

        
