from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets in the array which gives the sum of zero
    Args:
        nums: List[int] - Input integer array
    Returns:
        List[List[int]] - List of unique triplets [a,b,c] where a+b+c=0
    Time Complexity: O(n²) - Sort O(n log n) + two pointers traverse O(n²)
    Space Complexity: O(log n) ~ O(n) - Depends on sorting algorithm space
    """
    # Result list to store unique triplets
    result = []
    # Sort the array (key for two pointers and duplicate removal)
    nums.sort()
    n = len(nums)
    
    # Iterate through each element as the first number of triplet
    for i in range(n):
        # Skip duplicate first element to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # Target sum for the other two numbers
        target = -nums[i]
        # Two pointers: left starts after i, right at the end
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                # Found valid triplet, add to result
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicate left element
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                # Skip duplicate right element
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                
                # Move both pointers to find new combinations
                left += 1
                right -= 1
            
            elif current_sum < target:
                # Need larger sum, move left pointer right
                left += 1
            else:
                # Need smaller sum, move right pointer left
                right -= 1
    
    return result

# Test case for verification
if __name__ == "__main__":
    test_nums = [-1,0,1,2,-1,-4]
    # Expected output: [[-1,-1,2],[-1,0,1]]
    print(f"3Sum result: {threeSum(test_nums)}")
