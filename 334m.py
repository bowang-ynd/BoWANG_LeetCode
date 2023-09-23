"""
334. Increasing Triplet Subsequence

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""

def increasingTriplet(nums) -> bool:
    # initiate the first_sum and second_sum variables to positive infinity for later comparison        
    first_num = float("inf")
    second_num = float("inf")

    # iterate through the list 
    for num in nums:
        # if the current num is smaller than the first_num, set first_num as current num
        if num <= first_num:
            first_num = num
        # if the current num is greater than the first_num and smaller than the second_num, then we have found the second num in the ijk sequence
        # so, set the second_num as the current num
        # the reason why we can reset the first_num without concerning whether affecting the sequence is because the second_num also represent a sequence of i and j regardless of later first_num
        # only if we have found a i and j sequence prior, we can set the second_num
        # so with the second_num, we simply need to find the third num, that is any num greater than the second_num
        elif first_num < num <= second_num:
            second_num = num
        # if the current num is also greater than the second_num, then we have found the third num in the ijk sequence
        # so we can return True
        else: 
            return True

    return False

def main():
    print(increasingTriplet([1,2,3,4,5]))
    print(increasingTriplet([5,4,3,2,1]))
    print(increasingTriplet([2,1,5,0,7,4,6]))

if __name__ == '__main__':
    main()