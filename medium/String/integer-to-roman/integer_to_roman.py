def intToRoman(num: int) -> str:
    """
    Convert an integer to a Roman numeral (1 <= num <= 3999)
    Args:
        num: int - Input integer (1-3999)
    Returns:
        str - Corresponding Roman numeral string
    Time Complexity: O(1) - Fixed number of iterations (max 13 steps)
    Space Complexity: O(1) - Fixed size of value-symbol pairs
    """
    # Define value-symbol pairs in descending order (include special cases like 4, 9, 40...)
    value_symbols = [
        (1000, "M"),
        (900,  "CM"),
        (500,  "D"),
        (400,  "CD"),
        (100,  "C"),
        (90,   "XC"),
        (50,   "L"),
        (40,   "XL"),
        (10,   "X"),
        (9,    "IX"),
        (5,    "V"),
        (4,    "IV"),
        (1,    "I")
    ]
    
    roman = []
    # Iterate through value-symbol pairs
    for value, symbol in value_symbols:
        # If num >= current value, append symbol and subtract value
        while num >= value:
            roman.append(symbol)
            num -= value
        # Early exit if num becomes 0
        if num == 0:
            break
    
    # Join list to string
    return ''.join(roman)

# Test case for verification
if __name__ == "__main__":
    test_cases = [3, 58, 1994]
    # Expected outputs: "III", "LVIII", "MCMXCIV"
    for case in test_cases:
        print(f"Integer {case} → Roman: {intToRoman(case)}")
