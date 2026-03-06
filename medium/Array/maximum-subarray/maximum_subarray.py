from typing import List

def maxSubArray(nums: List[int]) -> int:
    """
    Find the contiguous subarray with the largest sum (Kadane's Algorithm)
    Args:
        nums: List[int] - Input integer array (can contain negative numbers)
    Returns:
        int - Maximum sum of contiguous subarray
    Time Complexity: O(n) - Traverse the array once
    Space Complexity: O(1) - Constant extra space (optimized Kadane's Algorithm)
    """
    # Current maximum sum of subarray ending at current position
    current_max = nums[0]
    # Global maximum sum of all subarrays
    global_max = nums[0]
    
    # Traverse from the second element
    for num in nums[1:]:
        # Key logic: either start new subarray with current num, or extend previous subarray
        current_max = max(num, current_max + num)
        # Update global max if current max is larger
        global_max = max(global_max, current_max)
    
    return global_max

# Test case for verification
if __name__ == "__main__":
    test_cases = [
        [-2,1,-3,4,-1,2,1,-5,4],  # Expected: 6 (subarray [4,-1,2,1])
        [1],                        # Expected: 1
        [5,4,-1,7,8]               # Expected: 23
    ]
    for case in test_cases:
        print(f"Input: {case} → Max subarray sum: {maxSubArray(case)}")
