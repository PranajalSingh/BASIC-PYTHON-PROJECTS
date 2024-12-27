class Solution:
    def __init__(self):
        self.longest_palindrome = None
        self.current_longest_palindrome = None

    def longestPalindrome(self, string: str) -> str:
        self.longest_palindrome = string[0]
        for i in range(1, len(string)):
            for j in range(0, len(string) - i):
                self.current_longest_palindrome = string[j:i+1+j]
                if self.current_longest_palindrome == self.current_longest_palindrome[::-1]:
                    self.longest_palindrome = self.current_longest_palindrome
        return self.longest_palindrome

word = input()
a = Solution()
print(a.longestPalindrome(word))