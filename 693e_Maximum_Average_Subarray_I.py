"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""
def findMaxAverage(nums, k) -> float:
    """
    Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
    @param: nums; list, a list of integer 
    @param: k; int, an int indicating the subarray's length
    @return: float
    """

    # setup the current sum 
    curr_sum = sum(nums[:k])
    # setup the current max
    curr_max = curr_sum

    # iterate over the remaining entries in the list, starting at index k
    for i in range(k, len(nums)):
        # add the current entry to the sum
        curr_sum += nums[i]
        # subtract the previous entry, which has index as i-k
        curr_sum -= nums[i - k]

        # update current max
        curr_max = max(curr_sum, curr_max)

    # return the average: dividing curr_max by k
    return curr_max / k