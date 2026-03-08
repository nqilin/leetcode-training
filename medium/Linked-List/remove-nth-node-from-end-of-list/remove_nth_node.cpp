// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

/**
 * Remove the nth node from the end of a linked list (one-pass solution)
 * @param head: ListNode* - Head of the linked list
 * @param n: int - The nth node to remove from the end (1-indexed)
 * @return: ListNode* - Head of the modified linked list
 * Time Complexity: O(L) - L is the length of the linked list (one-pass)
 * Space Complexity: O(1) - Constant extra space (no extra list)
 */
ListNode* removeNthFromEnd(ListNode* head, int n) {
    // Dummy node to handle edge case (remove head node)
    ListNode* dummy = new ListNode(0, head);
    // Two pointers: slow starts at dummy, fast starts at head
    ListNode* slow = dummy;
    ListNode* fast = head;
    
    // Move fast pointer n steps ahead (create n-gap between slow and fast)
    for (int i = 0; i < n; i++) {
        fast = fast->next;
    }
    
    // Move both pointers until fast reaches end (slow stops at prev of target node)
    while (fast != nullptr) {
        slow = slow->next;
        fast = fast->next;
    }
    
    // Remove the nth node (skip the target node)
    ListNode* temp = slow->next; // Save target node for memory release
    slow->next = slow->next->next;
    delete temp; // Free memory (good practice)
    
    // Return modified list (skip dummy node)
    ListNode* result = dummy->next;
    delete dummy; // Free dummy node memory
    return result;
}

// Helper functions for test
ListNode* create_linked_list(int nums[], int n) {
    ListNode* dummy = new ListNode(0);
    ListNode* current = dummy;
    for (int i = 0; i < n; i++) {
        current->next = new ListNode(nums[i]);
        current = current->next;
    }
    return dummy->next;
}

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
    // Example: [1,2,3,4,5], n=2 → [1,2,3,5]
    int test_nums[] = {1,2,3,4,5};
    ListNode* test_list = create_linked_list(test_nums, 5);
    ListNode* modified_list = removeNthFromEnd(test_list, 2);
    printf("Modified list: ");
    print_linked_list(modified_list);
    
    // Free memory
    delete test_list;
    delete modified_list;
    return 0;
}
