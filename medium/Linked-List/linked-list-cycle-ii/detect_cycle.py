from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Find the starting node of the linked list cycle.
        Approach: Floyd's Tortoise and Hare (Two Pointers)
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        slow = head
        fast = head

        # Step 1: Move pointers to find the meeting point if cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # Found cycle, now find the entrance
            if slow == fast:
                # Move slow pointer back to head
                slow = head
                # Both pointers move one step at a time until they meet
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                # Meeting point is the cycle start
                return slow
        
        # No cycle exists
        return None
