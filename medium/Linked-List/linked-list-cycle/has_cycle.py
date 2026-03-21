from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Check if linked list has a cycle.
        Approach: Fast & Slow Pointers (Floyd’s Tortoise and Hare)
        Time: O(n)
        Space: O(1)
        """
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True

if __name__ == "__main__":
    print("Cycle detection test")
