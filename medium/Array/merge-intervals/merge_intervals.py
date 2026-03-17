from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge all overlapping intervals.
    Approach: Sort + Merge
    Time: O(n log n)
    Space: O(1) / O(n)
    """
    if not intervals:
        return []
    
    # Sort intervals by start time
    intervals.sort()
    res = [intervals[0]]
    
    for i in range(1, len(intervals)):
        last = res[-1]
        curr = intervals[i]
        
        if curr[0] <= last[1]:
            # Overlap: merge
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)
    
    return res

if __name__ == "__main__":
    print(merge([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
