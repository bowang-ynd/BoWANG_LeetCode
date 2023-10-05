"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""
from collections import Counter


def uniqueOccurrences(arr) -> bool:
    # set up count dictionary
    count = {}

    # iterate over the arr
    for num in arr:
        # increment current count value in the dict
        # if None, then set default to 0
        count[num] = count.get(num, 0) + 1
    
    # if the length of count dict is the same as length of the set of count dict's values
    # which means, no values are repeated
    # return True
    if len(count) == len(set(count.values())):
        return True
    
    # otherwise return False
    return False

def uniqueOccurrences2(arr) -> bool:

    # use the Counter class from Collections 
    return sum(set(Counter(arr).values())) == len(arr)