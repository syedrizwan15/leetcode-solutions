class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Check if string is empty
        if i == n:
            return 0

        # Check sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        # Convert digits
        num = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # Overflow check
            if num > (2**31 - 1 - digit) // 10:
                return -2**31 if sign == -1 else 2**31 - 1

            num = num * 10 + digit
            i += 1

        return sign * num