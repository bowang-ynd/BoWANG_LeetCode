"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""

def decodeString(s):
        
    # initialize an empty stack
    stack = []

    # iterate over the input encoded string
    for chr in s:

        # append the current character to stack if current char is not ']'
        if chr != ']':
            stack.append(chr)
            
        # otherwise, we have a closed [] section and we can decode 
        else: 
            # define a sub string to store decoded string 
            subStr = ""

            # while current char on top of the stack is not '['
            # add it to the sub string 
            while stack[-1] != '[':
                subStr += stack.pop()
                
            # otherwise, the top of the stack is '['
            # then, pop it 
            stack.pop()

            # then define a number string to store decoded digit(s)
            numStr = ""

            # while current stack has value, and the top of stack is a digit
            # add current digit to numStr
            while stack and stack[-1].isdigit():
                numStr += stack.pop()
                
            # otherwise, the current decoded string should be the decoded sub string repeating for decoded num times
            # reverse the order of numStr
            stack.append(int(numStr[::-1]) * subStr)
        
    # after all characters have been resolved in the for loop, return a string of current stack
    return "".join([section[::-1] for section in stack])    