def reverseWords(s: str) -> str:
    """
    Reverse the words in a string, remove extra spaces.
    Time: O(n)
    Space: O(n)
    """
    words = s.strip().split()
    words.reverse()
    return " ".join(words)

if __name__ == "__main__":
    print(reverseWords("the sky is blue"))  # "blue is sky the"
