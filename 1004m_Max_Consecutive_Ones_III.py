"""
Medium
7.6K
89
company
Amazon
company
tcs
company
Facebook
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""

def longestOnes(nums, k) -> int:
    """
    Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
    @param: nums; binary int list contains 0 and 1
    @param: k; int which indicates how many 0s can be flipped to 1s
    @return: int; the longest ones we can have in nums
    """

    # define the left pointer
    left = 0

    # iterate over the nums list with the right pointer
    for right in range(len(nums)):

        # if right pointer currently points to a 0
        # reduce k by 1 to flip current 0 to 1
        if nums[right] == 0:
            k -= 1

        # if no more k can be used to flip 0 to 1
        if k < 0:
            # if the current left points to a 0, then increment k by 1 because by removing the left 0, we can flip another 0 on the right to 1
            if nums[left] == 0:
                k += 1
            
            # regardless, increment left by 1 because our right pointer keeps moving towards the right to find longest ones
            left += 1

    # return the length between right and left pointers
    return right - left + 1