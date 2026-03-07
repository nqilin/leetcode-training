from typing import List

def sortColors(nums: List[int]) -> None:
    """
    Sort an array with 0, 1, 2 in-place (Dutch National Flag Problem)
    Args:
        nums: List[int] - Input array containing only 0, 1, 2
    Returns:
        None - Modify nums in-place instead of returning
    Time Complexity: O(n) - Traverse the array once (one-pass solution)
    Space Complexity: O(1) - Constant extra space (in-place sorting)
    """
    # Three pointers:
    # left: right boundary of 0s (all elements before left are 0)
    # current: current element to check
    # right: left boundary of 2s (all elements after right are 2)
    left = 0
    current = 0
    right = len(nums) - 1
    
    while current <= right:
        if nums[current] == 0:
            # Swap current with left (put 0 to 0s region)
            nums[left], nums[current] = nums[current], nums[left]
            # Move left forward (expand 0s region)
            left += 1
            # Move current forward (processed current element)
            current += 1
        elif nums[current] == 1:
            # 1 is in correct position, move current forward
            current += 1
        else: # nums[current] == 2
            # Swap current with right (put 2 to 2s region)
            nums[current], nums[right] = nums[right], nums[current]
            # Move right backward (expand 2s region)
            right -= 1
            # Do NOT move current (swapped element needs to be checked)

# Test case for verification
if __name__ == "__main__":
    test_cases = [
        [2,0,2,1,1,0],  # Expected: [0,0,1,1,2,2]
        [2,0,1],         # Expected: [0,1,2]
        [0]              # Expected: [0]
    ]
    for case in test_cases:
        sortColors(case)
        print(f"Sorted array: {case}")
