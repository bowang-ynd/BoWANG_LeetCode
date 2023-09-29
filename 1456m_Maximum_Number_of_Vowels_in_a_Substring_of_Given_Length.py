"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
"""

def maxVowels(s, k) -> int:
    """
    Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
    @param: s; str, that we need to count the max number of vowel letters
    @param: k; int, that indicates the length of the subarray
    @return: int
    """
    # define a vowels str for reference    
    vowels = "aeiou"

    # setup the count variable as 0
    count = 0

    # for the first subarray of length k, count the vowels 
    for i in range(k):
        # if current character is a vowel, count increment by 1
        if s[i] in vowels:
            count += 1
        
    # set current max_count as current count
    max_count = count

    # note: if the current max_count is already the length k, then we have a maximum of k that cannot be bigger
    # then, return current max_count or k in this case.
    if max_count == k:
        return k
    
    # iterate over the remaining str, starting at index k
    for i in range(k, len(s)):
        # check if the new char is a vowel
        # if so, count increment by 1
        if s[i] in vowels:
            count += 1
        
        # check if the previous character is a vowel
        # if so, count - 1
        if s[i-k] in vowels:
            count -= 1
        
        # update the max_count with the bigger value 
        max_count = max(count, max_count)
        
        # check if current max_count is equal to length k
        # if so, return the current max_count or k
        if max_count == k:
            return k
        
    return max_count
