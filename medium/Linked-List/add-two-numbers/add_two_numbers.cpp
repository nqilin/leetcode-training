// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

/**
 * Add two numbers represented by linked lists (reverse order)
 * @param l1: ListNode* - First number (each node is a digit, reverse order)
 * @param l2: ListNode* - Second number (each node is a digit, reverse order)
 * @return: ListNode* - Sum of the two numbers (linked list, reverse order)
 * Time Complexity: O(max(m, n)) - m/n are lengths of l1/l2, traverse longer list once
 * Space Complexity: O(max(m, n)) - Result list has at most max(m,n)+1 nodes
 */
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    // Dummy node to simplify result list construction
    ListNode* dummy = new ListNode(0);
    ListNode* current = dummy;
    // Carry for addition (0 or 1)
    int carry = 0;
    
    // Traverse both lists until all nodes and carry are processed
    while (l1 != nullptr || l2 != nullptr || carry != 0) {
        // Get current digit values (0 if node is nullptr)
        int val1 = (l1 != nullptr) ? l1->val : 0;
        int val2 = (l2 != nullptr) ? l2->val : 0;
        
        // Calculate sum of digits + carry
        int total = val1 + val2 + carry;
        // Current digit is total % 10
        int current_digit = total % 10;
        // Update carry (1 if total >= 10, else 0)
        carry = total / 10;
        
        // Create new node for current digit and move pointer
        current->next = new ListNode(current_digit);
        current = current->next;
        
        // Move to next nodes if available
        if (l1 != nullptr) l1 = l1->next;
        if (l2 != nullptr) l2 = l2->next;
    }
    
    // Return result list (skip dummy node)
    ListNode* result = dummy->next;
    delete dummy; // Free dummy node memory
    return result;
}

// Helper function to create linked list from array
ListNode* create_linked_list(int nums[], int n) {
    ListNode* dummy = new ListNode(0);
    ListNode* current = dummy;
    for (int i = 0; i < n; i++) {
        current->next = new ListNode(nums[i]);
        current = current->next;
    }
    return dummy->next;
}

// Helper function to print linked list (for verification)
void print_linked_list(ListNode* head) {
    printf("[");
    ListNode* current = head;
    while (current != nullptr) {
        printf("%d", current->val);
        if (current->next != nullptr) printf(",");
        current = current->next;
    }
    printf("]\n");
}

// Test case for verification
int main() {
    // Example: l1 = [2,4,3], l2 = [5,6,4] → sum = [7,0,8] (342 + 465 = 807)
    int l1_nums[] = {2,4,3};
    int l2_nums[] = {5,6,4};
    ListNode* l1 = create_linked_list(l1_nums, 3);
    ListNode* l2 = create_linked_list(l2_nums, 3);
    ListNode* sum_list = addTwoNumbers(l1, l2);
    // Expected output: [7,0,8]
    printf("Sum result: ");
    print_linked_list(sum_list);
    
    // Free memory (optional but good practice)
    delete l1;
    delete l2;
    delete sum_list;
    return 0;
}
