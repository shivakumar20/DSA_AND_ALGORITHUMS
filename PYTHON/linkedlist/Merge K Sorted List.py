import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min-heap to keep track of the smallest node from each list
        heap = []

        # Push the head of each linked list into the heap
        for i, node in enumerate(lists):
            if node:
                # Push a tuple (node value, index, node) to maintain order in case of duplicate values
                heapq.heappush(heap, (node.val, i, node))
        
        # Dummy node to start the merged linked list
        D = ListNode()
        cur = D  # Pointer to build the result linked list

        # Process the heap until it is empty
        while heap:
            # Extract the smallest element from the heap
            val, i, node = heapq.heappop(heap)

            # Link the extracted node to the result list
            cur.next = node
            cur = node  # Move the pointer forward

            # Move to the next node in the linked list from which the extracted node came
            node = node.next

            # If there is another node in the same list, push it to the heap
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        # Return the merged sorted linked list
        return D.next
