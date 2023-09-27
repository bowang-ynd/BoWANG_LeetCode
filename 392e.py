"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
"""

def isSubsequence(s, t) -> bool:
    """
    Check if the string t contains string s in s's orginal order. 
    e.g. "abc" is in "ahbhc" but not in "acb"
    @param: s; string s is the subsequence that should exist in t
    @param: t; string t is the target string within which we need to find string s 
    @return: bool; True for s in t, False for s not in t
    """
    # if string s is an empty string, then it is a subsequence for any string t
    # so return True when s is empty
    if len(s) == 0:
        return True
    # then for s is not an empty string
    else:
        # initialize two pointers p1, p2
        p1, p2 = 0, 0
        # while loop for p1 and p2 both have not reached the end of string s or string t
        while (p1 < len(s)) and (p2 < len(t)):
            # compare current char at p1 in s and at p2 in t
            # if the char at p1 in s is in t, move on to next char in s by increment p1
            if s[p1] == t[p2]:
                p1 += 1
            
            # regardless we have found the char in s at p1 or not, increment p2 to move on and compare next char in t
            p2 += 1
        
        # if all chars in s have been found in t, p1 should be equal to its length
        # return (p1 == len(s)) will return True then. Otherwise, return False, meaning that not all chars in s are found in t
        return p1 == len(s)


#Example 1:
#Input: s = "abc", t = "ahbgdc"
#Output: true
print("The result should be True: ", isSubsequence("abc", "ahbgdc"))

#Example 2:
#Input: s = "axc", t = "ahbgdc"
#Output: false
print("The result should be False: ", isSubsequence("axc", "ahbgdc"))

#Example 3:
#Input: s = "", t = "ahbgdc"
#Output: true
print("The result should be True: ", isSubsequence("", "ahbgdc"))
