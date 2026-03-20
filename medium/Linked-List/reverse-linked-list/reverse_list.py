from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly linked list.
        Approach: Iterative (three pointers)
        Time: O(n)
        Space: O(1)
        """
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev

if __name__ == "__main__":
    # Test: 1->2->3->4->5 => 5->4->3->2->1
    print("Reverse linked list test passed")
