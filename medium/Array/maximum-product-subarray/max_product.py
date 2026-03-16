from typing import List

def maxProduct(nums: List[int]) -> int:
    """
    Find the contiguous subarray with the largest product.
    Approach: Dynamic Programming (track max & min)
    Time: O(n)
    Space: O(1)
    """
    if not nums:
        return 0

    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        temp = max_prod
        max_prod = max(nums[i], max_prod * nums[i], min_prod * nums[i])
        min_prod = min(nums[i], temp * nums[i], min_prod * nums[i])
        result = max(result, max_prod)

    return result

if __name__ == "__main__":
    print(maxProduct([2,3,-2,4]))  # 6
    print(maxProduct([-2,0,-1]))  # 0
