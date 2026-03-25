#include <iostream>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        /*
         * Find the starting node of the linked list cycle.
         * Approach: Floyd's Tortoise and Hare (Two Pointers)
         * Time Complexity: O(n)
         * Space Complexity: O(1)
         */
        ListNode* slow = head;
        ListNode* fast = head;

        // Step 1: Find meeting point if cycle exists
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;

            // Cycle detected
            if (slow == fast) {
                // Reset slow to head
                slow = head;
                // Find cycle entrance
                while (slow != fast) {
                    slow = slow->next;
                    fast = fast->next;
                }
                return slow;
            }
        }

        // No cycle
        return nullptr;
    }
};
