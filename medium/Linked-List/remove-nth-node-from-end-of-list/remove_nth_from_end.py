from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the nth node from the end of the list.
        Approach: Two Pointers (Dummy Node)
        Time: O(n)
        Space: O(1)
        """
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        
        # Fast moves n steps first
        for _ in range(n + 1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Remove the node
        slow.next = slow.next.next
        return dummy.next

if __name__ == "__main__":
    print("Remove Nth Node test")
