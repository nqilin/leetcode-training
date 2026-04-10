# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        Find the node where cycle begins in linked list.
        Approach: Fast & Slow Two Pointers (Floyd's Algorithm)
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        slow = head
        fast = head
        
        # first meet: detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # find cycle entrance
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
