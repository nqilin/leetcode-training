from typing import List

def longestConsecutive(nums: List[int]) -> int:
    """
    Find the length of the longest consecutive elements sequence.
    Approach: Hash Set
    Time: O(n)
    Space: O(n)
    """
    num_set = set(nums)
    max_len = 0

    for num in num_set:
        # Only check starting point (no left neighbor)
        if num - 1 not in num_set:
            curr_num = num
            curr_len = 1

            while curr_num + 1 in num_set:
                curr_num += 1
                curr_len += 1

            max_len = max(max_len, curr_len)

    return max_len

if __name__ == "__main__":
    print(longestConsecutive([100,4,200,1,3,2]))  # 4
