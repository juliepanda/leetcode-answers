# PASSED

# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.

# M = 1000
# D = 500
# C = 100
# L = 50
# X = 10
# V = 5
# I = 1

# ex// DCXXI: 621

class Solution:
# @param {string} s
# @return {integer}
  def romanToInt(self, s):
    sum = 0
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    i = 0
    while i < len(s):
      firstChar = s[i]
      secondChar = s[i+1] if i < len(s) - 1 else None
      # case if 4 or 9
      if secondChar != None and roman[firstChar] < roman[secondChar]:
        sum = sum + roman[secondChar] - roman[firstChar]
        i = i + 2
      else:
      # normal case
        sum = sum + roman[firstChar]
        i = i + 1
    return sum
