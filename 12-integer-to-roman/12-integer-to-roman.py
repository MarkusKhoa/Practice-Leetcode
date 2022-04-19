class Solution(object):
    def intToRoman(self, num):
        roman_digits = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_num = ""
        i = 0
        while num != 0:
            for _ in range(int(num/ints[i])):
                roman_num += roman_digits[i]
                num -= ints[i]
            i += 1
        return roman_num