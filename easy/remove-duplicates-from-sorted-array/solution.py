# LeetCode Easy: Remove Duplicates from Sorted Array (26)
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Author: nqilin
# Date: 2026

def removeDuplicates(nums: list[int]) -> int:
    """
    Solution: Two Pointers (slow & fast)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0

    # Slow pointer: position for next unique element
    slow = 1

    # Fast pointer: traverse all elements
    for fast in range(1, len(nums)):
        # If current is different from previous one → keep it
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1

    return slow


if __name__ == "__main__":
    nums1 = [1,1,2]
    print(removeDuplicates(nums1))  # 2
    print(nums1[:2])                # [1,2]

    nums2 = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(nums2))  # 5
