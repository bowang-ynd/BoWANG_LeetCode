"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
"""

def equalPairs(grid) -> int:
    
    # initialize a dictionary to store each unique row
    pair_dict = {}

    # set up count as 0
    count = 0

    # count the row in the original grid and store in the dictionary
    for row in grid:
        row_tuple = tuple(row)

        # if current row is not in the dictionary, set default value as 0 and then increment
        pair_dict[row_tuple] = pair_dict.get(row_tuple, 0) + 1

    # rotate the grid 
    new_grid = [[] for _ in range(len(grid))]

    for i in range(len(grid)):
        p_row = 0
        while p_row < len(grid):
            new_grid[i].append(grid[p_row][i])
            p_row += 1

    # check if the row in rotated grid is in our dictionary
    # if so, add the stored value to our count
    for row in new_grid:
        row_tuple = tuple(row)
        if row_tuple in pair_dict.keys():
            count += pair_dict.get(row_tuple)
    
    return count