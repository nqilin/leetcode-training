from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into one sorted linked list.
        Approach: Iterative with dummy node
        Time Complexity: O(n + m)
        Space Complexity: O(1)
        """
        # Create a dummy node to simplify merging
        dummy = ListNode()
        current = dummy

        # Traverse both lists and append smaller node
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Append remaining nodes
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next
