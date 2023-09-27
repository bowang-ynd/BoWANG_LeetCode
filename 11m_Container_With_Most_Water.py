"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

def maxArea(height) -> int:
    """
    return the max area with list of height; the area is calculated by the x-axis and height
    @param: height; a list of height
    @return: max_water; the max area to contain the most water
    """

    # initialize max_water variable 
    max_water = 0

    # initialize two pointers, idx_left and idx_right pointing to the most left and most right entry of the height list
    idx_left, idx_right = 0, len(height) - 1

    # while loop: left index is still at the left of right index
    # that is x-axis distance is greater than 0
    while (idx_left < idx_right):
        # calculate the current area
        curr_area = (idx_right - idx_left) * (min(height[idx_left], height[idx_right]))
        # max_water should be the higher value between previous max area and current area
        max_water = max(max_water, curr_area)

        # check which side has a shorter height, the idx from the shorter side should move towards the center by 1
        # that is left++ or right--
        if height[idx_left] < height[idx_right]:
            idx_left += 1
        else:
            idx_right -= 1

    # after going through the entire height list, return max_water
    return max_water