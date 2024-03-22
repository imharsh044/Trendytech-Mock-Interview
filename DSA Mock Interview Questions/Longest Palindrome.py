"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case-sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:
1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""


# Solution:
def longestPalindrome(s: str) -> int:
    hash_set = set()
    max_len = 0

    for char in s:
        if char in hash_set:
            hash_set.remove(char)
            max_len += 2
        else:
            hash_set.add(char)

    return max_len if len(hash_set) == 0 else max_len + 1
