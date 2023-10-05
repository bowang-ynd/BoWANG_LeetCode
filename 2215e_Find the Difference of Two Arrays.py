"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
Example 2:

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
-1000 <= nums1[i], nums2[i] <= 1000
"""

def findDifference(nums1, nums2) -> list:
    """
    Return a list contains two list. The first list contians unique elements in nums1 but not in nums2, and the second list contains unique elements in nums2 but not in nums1
    @param: nums1; list, a list of int
    @param: nums2; list, a list of int
    @return: list; a list of two unique set that contains elements in one but not in the other
    """

    # initialize two empty list for append and return
    lst1 = []
    lst2 = []
    
    # cast the input nums1 and nums2 list to set to retrive all unique int
    set1 = set(nums1)
    set2 = set(nums2)

    # using set difference to retrive elements in one set but not in the other
    lst1 = set1 - set2
    lst2 = set2 - set1
    
    # return the list result 
    return [lst1, lst2]