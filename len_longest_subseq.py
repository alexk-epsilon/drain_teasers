'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_pos = dict()
        n = len(s)
        first = 0
        max_len = 0
        for last in range(n):
            if s[last] in letter_pos:
                first = max(first,letter_pos[s[last]])                

            letter_pos[s[last]] = last +1
            subseq_len = last-first+1
            max_len = max(subseq_len,max_len)
            
        return max_len
    
print(Solution().lengthOfLongestSubstring("abcdae"))
print(Solution().lengthOfLongestSubstring("abcabcbb"))

