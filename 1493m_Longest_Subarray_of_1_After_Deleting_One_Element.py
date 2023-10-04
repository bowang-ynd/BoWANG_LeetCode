"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

def longestSubarray(nums) -> int:
    """
    Return the size of the longest non-empty subarray containing only 1's in the resulting array. Reutn 0 if no such subarray
    @param: nums: list; contains a list of binary int
    @return: int; length of the longest subarray specified
    """

    # set left pointer as 0
    left = 0

    # set a variable to indicate how many zeros we can delete
    zero_count = 1

    # iterate through the nums list with right pointer
    for right in range(len(nums)):
        # if right pointer points to 0
        # decrement the zero_count
        if nums[right] == 0:
            zero_count -= 1

        # if we have counted two zeros
        if zero_count < 0:

            # check current left pointer entry
            # if left points to a zero, increment the zero_count
            if nums[left] == 0:
                zero_count += 1
            
            # regardless, increment left pointer
            left += 1
    
    return right - left


example1 = [0,1,1,1,0,1,1,0,1]
print("Expected: 5 and Output: ", longestSubarray(example1))
example2 = [1,1,0,1]
print("Expected: 3 and Output: ", longestSubarray(example2))