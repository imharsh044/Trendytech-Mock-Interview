"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix amongst the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

# Solution:
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ''

    shortest_str = min(strs, key=len)
    for idx, curr_char in enumerate(shortest_str):
        for other_str in strs:
            if other_str[idx] != curr_char:
                return shortest_str[:idx]

    return shortest_str
