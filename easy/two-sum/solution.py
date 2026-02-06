# LeetCode Easy: Two Sum (https://leetcode.com/problems/two-sum/)
# Two solutions: Brute Force / Hash Table (dictionary)
# Author: nqilin
# Date: 2026

# Problem Statement:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input has exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def two_sum_brute_force(nums: list[int], target: int) -> list[int]:
    """
    Solution 1: Brute Force (simple, low efficiency)
    Time Complexity: O(n²) - double for loop
    Space Complexity: O(1) - no extra space
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # No solution (per problem statement, this line is unreachable)

def two_sum_hash_table(nums: list[int], target: int) -> list[int]:
    """
    Solution 2: Hash Table (dictionary, optimal)
    Time Complexity: O(n) - single for loop
    Space Complexity: O(n) - store elements in dict
    Core Idea: Use dict to map value -> index, find complement in O(1)
    """
    num_map = {}  # key: number value, value: number index
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], idx]
        num_map[num] = idx
    return []  # No solution (per problem statement, this line is unreachable)

# Test cases (verify solution correctness)
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(two_sum_brute_force(nums1, target1))  # Output: [0, 1]
    print(two_sum_hash_table(nums1, target1))   # Output: [0, 1]

    # Test Case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(two_sum_hash_table(nums2, target2))   # Output: [1, 2]

    # Test Case 3
    nums3 = [3, 3]
    target3 = 6
    print(two_sum_hash_table(nums3, target3))   # Output: [0, 1]
