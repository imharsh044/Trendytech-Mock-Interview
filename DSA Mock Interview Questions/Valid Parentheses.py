"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


# Solution:
def isValid(s: str) -> bool:
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    stack_arr = []

    for char in s:
        if char in bracket_pairs.keys():
            curr_brace = bracket_pairs[char]
            if len(stack_arr) > 0 and curr_brace == stack_arr[-1]:
                stack_arr.pop()
            else:
                return False
        else:
            stack_arr.append(char)

    return len(stack_arr) == 0
