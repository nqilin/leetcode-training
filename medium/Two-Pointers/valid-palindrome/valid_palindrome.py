class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if the string is a valid palindrome.
        Approach: Two Pointers
        Time: O(n)
        Space: O(1)
        """
        # Initialize left and right pointers
        left = 0
        right = len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters on left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric characters on right
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters in lowercase
            if s[left].lower() != s[right].lower():
                return False
            
            # Move pointers towards center
            left += 1
            right -= 1
        
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
