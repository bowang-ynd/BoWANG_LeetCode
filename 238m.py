"""
238M: Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

def product_of_array_except_self(nums):
    """
    Takes a lift of int, return a list of int for each position is the product of the list except the int at the position itself.
    @param: nums, an int list
    @return: answer, an int list
    """

    # store the list's length to a local variable
    length = len(nums)

    # initialize the answer list
    answer = [0] * length

    # set the left most entry of answer as 1, this is because at index 1, there is no prefix product but 1
    answer[0] = 1

    # iterate through the input int list
    for i in range(1, length):
        # set the left variable with value of the int at previous index
        left = nums[i - 1]
        # update answer at the given index by multiplying the current left with existing prefix
        answer[i] = answer[i - 1] * left
    
    # set the right most entry as 1, this is also because at the last index, there is no suffix product but 1.
    right = 1

    # iterate through the list again, but reversedly
    for i in reversed(range(length)):

        # update the entry for answer at the current index by multipling its current value with the right 
        answer[i] = answer[i] * right

        # update the right as the product of all suffix to the current index
        right *= nums[i]

    return answer


def main():
    print(product_of_array_except_self([1, 2, 3, 4]))
    print([24, 12, 8, 6])

    print()

    print(product_of_array_except_self([-1, 1, 0, -3, 3]))
    print([0, 0, 9, 0, 0])

if __name__ == '__main__':
    main()