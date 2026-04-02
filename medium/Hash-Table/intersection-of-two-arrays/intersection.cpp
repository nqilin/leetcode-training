#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        /*
         * Get unique intersection of two arrays.
         * Approach: Hash Set lookup
         * Time: O(m + n)
         * Space: O(m)
         */
        unordered_set<int> st(nums1.begin(), nums1.end());
        vector<int> res;
        
        for(int x : nums2){
            if(st.count(x)){
                res.push_back(x);
                st.erase(x);
            }
        }
        return res;
    }
};
