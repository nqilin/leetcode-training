# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    """
    Remove the nth node from the end of a linked list (one-pass solution)
    Args:
        head: ListNode - Head of the linked list
        n: int - The nth node to remove from the end (1-indexed)
    Returns:
        ListNode - Head of the modified linked list
    Time Complexity: O(L) - L is the length of the linked list (one-pass)
    Space Complexity: O(1) - Constant extra space (no extra list)
    """
    # Dummy node to handle edge case (remove head node)
    dummy = ListNode(0, head)
    # Two pointers: slow starts at dummy, fast starts at head
    slow = dummy
    fast = head
    
    # Move fast pointer n steps ahead (create n-gap between slow and fast)
    for _ in range(n):
        fast = fast.next
    
    # Move both pointers until fast reaches end (slow stops at prev of target node)
    while fast:
        slow = slow.next
        fast = fast.next
    
    # Remove the nth node (skip the target node)
    slow.next = slow.next.next
    
    # Return modified list (skip dummy node)
    return dummy.next

# Helper functions for test
def create_linked_list(nums):
    dummy = ListNode(0)
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test case for verification
if __name__ == "__main__":
    # Example: [1,2,3,4,5], n=2 → [1,2,3,5]
    test_list = create_linked_list([1,2,3,4,5])
    modified_list = removeNthFromEnd(test_list, 2)
    print(f"Modified list: {linked_list_to_list(modified_list)}")
