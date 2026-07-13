class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0  # Store the length of the last word.
        i = len(s) - 1  # Start from the end of the string.

        while i >= 0 and s[i] == ' ':  # Skip trailing spaces.
            i -= 1

        while i >= 0 and s[i] != ' ':  # Count characters of the last word.
            length += 1
            i -= 1

        return length  # Return the length of the last word.