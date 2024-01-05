class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_int_mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        prev_value = 0
        for char in reversed(s):
            current_value = roman_to_int_mapping[char]
            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value
            prev_value = current_value
        return result


roman_numeral = input("s = ")
sol = Solution()
result = sol.romanToInt(roman_numeral)
print(f"{result}")
