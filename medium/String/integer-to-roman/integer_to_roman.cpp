#include <string>
#include <vector>
using namespace std;

/**
 * Convert an integer to a Roman numeral (1 <= num <= 3999)
 * @param num: int - Input integer (1-3999)
 * @return: string - Corresponding Roman numeral string
 * Time Complexity: O(1) - Fixed number of iterations (max 13 steps)
 * Space Complexity: O(1) - Fixed size of value-symbol pairs
 */
string intToRoman(int num) {
    // Define value-symbol pairs in descending order (include special cases like 4, 9, 40...)
    vector<pair<int, string>> value_symbols = {
        {1000, "M"},
        {900,  "CM"},
        {500,  "D"},
        {400,  "CD"},
        {100,  "C"},
        {90,   "XC"},
        {50,   "L"},
        {40,   "XL"},
        {10,   "X"},
        {9,    "IX"},
        {5,    "V"},
        {4,    "IV"},
        {1,    "I"}
    };
    
    string roman;
    // Iterate through value-symbol pairs
    for (auto& pair : value_symbols) {
        int value = pair.first;
        string symbol = pair.second;
        // If num >= current value, append symbol and subtract value
        while (num >= value) {
            roman += symbol;
            num -= value;
        }
        // Early exit if num becomes 0
        if (num == 0) {
            break;
        }
    }
    
    return roman;
}

// Test case for verification
#include <iostream>
int main() {
    int test_cases[] = {3, 58, 1994};
    // Expected outputs: "III", "LVIII", "MCMXCIV"
    for (int case_num : test_cases) {
        cout << "Integer " << case_num << " → Roman: " << intToRoman(case_num) << endl;
    }
    return 0;
}
