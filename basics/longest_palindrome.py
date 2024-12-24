class Solution:
    def __init__(self):
        self.lp = None
        self.t = None

    def longestPalindrome(self, s: str) -> str:
        self.lp = s[0]
        for i in range(1, len(s)):
            for j in range(0, len(s) - i):
                self.t = s[j:i+1+j]
                if self.t == self.t[::-1]:
                    self.lp = self.t
        return self.lp

string = input()
a = Solution()
print(a.longestPalindrome(string))