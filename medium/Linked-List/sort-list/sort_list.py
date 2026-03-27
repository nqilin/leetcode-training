from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Sort a linked list in O(n log n) time using constant space.
        Approach: Merge Sort (Top Down)
        Time Complexity: O(n log n)
        Space Complexity: O(log n)
        """
        # Base case: empty or single node
        if not head or not head.next:
            return head
        
        # Step 1: Find middle to split list
        mid = self.find_mid(head)
        left = head
        right = mid.next
        mid.next = None
        
        # Step 2: Recursively sort both halves
        left = self.sortList(left)
        right = self.sortList(right)
        
        # Step 3: Merge sorted halves
        return self.merge(left, right)
    
    def find_mid(self, head):
        # Find middle using slow & fast pointers
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, l1, l2):
        # Merge two sorted lists
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next
