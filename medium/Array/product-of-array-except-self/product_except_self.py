from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    """
    Return an array where each element is the product of all elements except itself.
    Approach: Prefix & Suffix Product
    Time: O(n)
    Space: O(1) (output array does not count)
    """
    n = len(nums)
    res = [1] * n

    # Prefix (left product)
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    # Suffix (right product)
    suffix = 1
    for i in range(n-1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]

    return res

if __name__ == "__main__":
    print(productExceptSelf([1,2,3,4]))  # [24,12,8,6]
