# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Add two numbers represented by linked lists (reverse order)
    Args:
        l1: ListNode - First number (each node is a digit, reverse order)
        l2: ListNode - Second number (each node is a digit, reverse order)
    Returns:
        ListNode - Sum of the two numbers (linked list, reverse order)
    Time Complexity: O(max(m, n)) - m/n are lengths of l1/l2, traverse longer list once
    Space Complexity: O(max(m, n)) - Result list has at most max(m,n)+1 nodes
    """
    # Dummy node to simplify result list construction
    dummy = ListNode(0)
    current = dummy
    # Carry for addition (0 or 1)
    carry = 0
    
    # Traverse both lists until all nodes and carry are processed
    while l1 or l2 or carry:
        # Get current digit values (0 if node is None)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate sum of digits + carry
        total = val1 + val2 + carry
        # Current digit is total % 10
        current_digit = total % 10
        # Update carry (1 if total >= 10, else 0)
        carry = total // 10
        
        # Create new node for current digit and move pointer
        current.next = ListNode(current_digit)
        current = current.next
        
        # Move to next nodes if available
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    # Return result list (skip dummy node)
    return dummy.next

# Helper function to create linked list from list
def create_linked_list(nums):
    dummy = ListNode(0)
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to convert linked list to list (for verification)
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test case for verification
if __name__ == "__main__":
    # Example: l1 = [2,4,3], l2 = [5,6,4] → sum = [7,0,8] (342 + 465 = 807)
    l1 = create_linked_list([2,4,3])
    l2 = create_linked_list([5,6,4])
    sum_list = addTwoNumbers(l1, l2)
    # Expected output: [7,0,8]
    print(f"Sum result: {linked_list_to_list(sum_list)}")
