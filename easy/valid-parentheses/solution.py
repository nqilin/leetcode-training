# LeetCode Easy: Valid Parentheses (20)
# https://leetcode.com/problems/valid-parentheses/
# Author: nqilin
# Date: 2026

# Problem: Check if the input parentheses string is valid.
# Rules:
# 1. Open brackets must be closed by the same type.
# 2. Open brackets must be closed in the correct order.

def isValid(s: str) -> bool:
    """
    Standard solution: Stack (list) + Mapping
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Map closing bracket to corresponding opening bracket
    bracket_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    stack = []  # Use list as stack (append = push, pop = pop from end)

    for char in s:
        # If it's closing bracket
        if char in bracket_map:
            # Get top element of stack (or dummy value if empty)
            top_element = stack.pop() if stack else '#'

            # Not matching → invalid
            if bracket_map[char] != top_element:
                return False
        else:
            # It's opening bracket → push to stack
            stack.append(char)

    # Valid only if stack is empty (all opened are closed)
    return len(stack) == 0


if __name__ == "__main__":
    print(isValid("()"))          # True
    print(isValid("()[]{}"))      # True
    print(isValid("(]"))          # False
    print(isValid("([)]"))        # False
    print(isValid("{[]}"))        # True
