# [LeetCode 49 - Group Anagrams](https://leetcode.com/problems/group-anagrams/)
> Difficulty: Medium | Tags: Hash Table, String, Sorting

## 🎯 Problem Description
Given an array of strings `strs`, group the anagrams together.  
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

## 💡 Solution Ideas
1. Core Idea:  
   Anagrams have the **same sorted character sequence**.  
   Use this sorted string as a **hash map key**.
2. Step-by-Step:
   - Iterate each string.
   - Sort the string to get a unique key for all its anagrams.
   - Use a hash map to group all strings with the same key.
   - Collect all groups from the map as the final result.
3. Edge Cases:
   - Empty string list
   - Single string
   - All strings are anagrams
   - All strings are unique

## 📁 Code Files
- [Python Solution](group_anagrams.py)
- [C++ Solution](group_anagrams.cpp)

## ⚡ Complexity Analysis
- **Time Complexity (TC): O(n * k log k)**
  - n: number of strings
  - k: maximum length of a string
  - Sorting each string takes O(k log k)
- **Space Complexity (SC): O(n * k)**
  - Store all strings in the hash map

## 📌 Problem-Solving Tips
1. Sorting is the simplest way to generate a key for anagrams.
2. Hash map enables O(1) average insertion and lookup.
3. This pattern is widely used in anagram-related problems.

## 📝 Training Log
- Completed Time: 2026-03-04
- Difficulty Evaluation: ⭐⭐ (1-5 stars)
- Notes: Learned how to use hash map + sorting to group anagrams.
