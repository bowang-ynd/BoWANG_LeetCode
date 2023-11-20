"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""

def asteroidCollision(asteroids):
    # initialize an empty stack
    stack = []

    # declare a flag for existence of asteroid
    flag = False

    # iterate over the list of asteroid
    for num in asteroids:
        # first update the existence flag as True
        flag = True

        # if the stack is not empty, 
        # and the top value is greater than 0
        # and current asteroid is in opposite direction
        while stack and stack[-1] > 0 and num < 0:
            # if the top value of stack is less than asteroid value
            # then we continue to pop the stack and check next top value
            if stack[-1] < abs(num):
                stack.pop()
                continue
            # else if top value equals asteroid value
            # we pop the stack and break the loop
            elif stack[-1] == abs(num):
                stack.pop()
                
            # whether the top value equals to asteroid value or top value is greater
            # it means the current asteroid is demolished 
            # so we set the existence flag as False and break from while loop
            flag = False
            break

        # after breaking from while loop
        # checks flag 
        if flag:
            stack.append(num)
        
    return stack   