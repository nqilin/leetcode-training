# LeetCode Easy: Remove Element (27)
# https://leetcode.com/problems/remove-element/
# Author: nqilin
# Date: 2026

def removeElement(nums: list[int], val: int) -> int:
    """
    Optimal Solution: Two Pointers (slow & fast)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Slow pointer: position to place the next valid number
    slow = 0

    # Fast pointer: traverse all elements
    for fast in range(len(nums)):
        # Keep elements that are NOT equal to val
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1

    # Slow pointer index = new length
    return slow


if __name__ == "__main__":
    # Test case 1
    nums1 = [3,2,2,3]
    val1 = 3
    print(removeElement(nums1, val1))  # 2
    print(nums1[:2])                   # [2,2]

    # Test case 2
    nums2 = [0,1,2,2,3,0,4,2]
    val2 = 2
    print(removeElement(nums2, val2))  # 5
