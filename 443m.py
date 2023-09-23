"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

"""

def compress(chars) -> int:
    """
    Takes a list of characters or symbols, return a compressed list which counts the occurances of each character or symbols. E.g. [a, b, b, b, c] will return 4 and the list will be modified as [a, b, 3, c]
    @param: chars, a list of characters and symbols
    @return: int, the length of the newly modifed list
    """
    # initialize variables
    compressed_lst = []

    # set count as 1 and the first previous character as the fitst entry in the input list
    count = 1
    prev_char = chars[0]

    # iterate through the chars list 
    for i in range(1, len(chars)):
        # if the current char is the same as previous char, count increment 
        if chars[i] == prev_char:
            count += 1
        # if the curr_char is not the same as prev_char
        # append the previous char to the compressed list 
        else:
            compressed_lst.append(prev_char)
            # if count is 1, then skip the process
            # if count is greater than 1, then append each digit of count as a str to the compressed list
            if count > 1:
                for num in str(count):
                    compressed_lst.append(num)
            # after appending the count, set the prev_char as current_char
            # and update count back to 1
            prev_char = chars[i]
            count = 1
    
    # after the iteration, append the last prev_char and its count to the compressed list 
    compressed_lst.append(prev_char)
    if count > 1:
        for num in str(count):
            compressed_lst.append(num)
    
    # update the input chars as the compressed list
    chars[:] = compressed_lst

    # return the length of the compressed list
    return len(compressed_lst)