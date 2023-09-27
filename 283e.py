"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 
"""

def moveZeros(nums) -> None:
    """
    Sort an int list by assigning all 0 in the list to the back, and keep other int in its original order to the front
    @param: nums, an int list which has length between 1 and 104
    @return: None, modify the original int list
    """
    # initialize the idx for which we would assign int that is not 0 to
    change_idx = 0
    
    # iterate through the int list 
    for idx in range(len(nums)):
        # if current entry is not 0, then swap it with the entry at change_idx
        if nums[idx] != 0:
            nums[change_idx], nums[idx] = nums[idx], nums[change_idx]
            # change_idx increment by 1 and point to next position to store non-0 entry
            change_idx += 1
