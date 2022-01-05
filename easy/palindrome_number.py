
# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

# For example, 121 is a palindrome while 123 is not.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Constraints:

# -231 <= x <= 231 - 1

# Follow up: Could you solve it without converting the integer to a string?

class Solution:
    # time complexity: runtime is gonna be O(log_10 N) where N is the length of digit x 
    # space complexity: O(1) since we do not store an array of numbers or characters to represent x  
    # converting digit x to a string (str x) would require O(N) alone 
    # my solution will not work if reversed number is larger than int.max 
    # better solution would be to only revert half of the number 
    # edge case: negativ number is never palindrome 
    # optimization: halt when original number x < reverse (means half of numbers have been processed)
    def isPalindrome(self, x: int) -> bool: 
        # Improved solution
        reverse = 0
        while(x > reverse):
            reverse = (reverse * 10) + x % 10 
            x = x // 10 # floor division  
        print(reverse)
        print(x)
        return True if reverse == x or reverse / 10 == x else False # get rid of last digtig in check by dividing reverse by 10 (eg x = 12, rev = 121, rev/10 = 12) 
    
    def simpleIsPalindrome(self, x: int) -> bool: # fails if reverse > int.max  
        reverse = 0
        remainder = x 
        while(remainder > 0):
            last = remainder % 10 
            reverse = (reverse * 10) + last 
            remainder = remainder // 10 # floor 
        return True if reverse == x else False

assert(Solution().simpleIsPalindrome(121))
assert(not Solution().simpleIsPalindrome(-121))
assert(not Solution().simpleIsPalindrome(10))
print("All tests passed")