#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

/**
 * Group anagrams together from a list of strings
 * @param strs: vector<string> - Input list of strings
 * @return: vector<vector<string>> - Groups of anagrams
 * Time Complexity: O(n * k log k) - n = number of strings, k = max length of a string
 * Space Complexity: O(n * k) - Store all strings in the hash map
 */
vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> anagram_map;

    for (string& s : strs) {
        string key = s;
        sort(key.begin(), key.end());
        anagram_map[key].push_back(s);
    }

    vector<vector<string>> result;
    for (auto& pair : anagram_map) {
        result.push_back(pair.second);
    }

    return result;
}

// Test
#include <iostream>
int main() {
    vector<string> test = {"eat","tea","tan","ate","nat","bat"};
    auto res = groupAnagrams(test);
    for (auto& g : res) {
        for (string& s : g) cout << s << " ";
        cout << endl;
    }
    return 0;
}
