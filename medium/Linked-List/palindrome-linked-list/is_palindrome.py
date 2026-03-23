from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Check if a linked list is a palindrome.
        Approach: Fast & Slow Pointers + Reverse Half List
        Time: O(n)
        Space: O(1)
        """
        # Find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # Compare
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True

if __name__ == "__main__":
    print("Palindrome linked list test")
