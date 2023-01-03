'''Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.'''

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # idea:
        # 1. stack storing index, height of that index, pair
        # 2. at any point in time, we want to store all rectangles that starts from some point and can extend to end of the array
        # 3. if it cant extend, we pop the latest ones till, we find one that can be extended through current elemnt
        # 4. current elements index is moved to the last popped one, as current element can be extended backwards till that
        # 5. this idea can be derived by taking all cases.. 
        # 6. case 1: bar1 is taller than bar 2. then bar 1 cant be extended through bar 2 but bar 2 can be extended back
        # 7. case 2: bar1 is shorter than bar 2. then bar 2 cant be extended back but a new rectangel can start from here that can potentially extend  till end
        # while popping update max area with a max area global variable
    
        stack = []
        ans = 0
        for i in range(len(heights)):

            ind = i
            # check if element smaller than latest one
            while stack and stack[-1][1]>heights[i]:
                ind, height = stack.pop()
                ans = max(ans, height*(i-ind)) # max height of extending till ith index
                # pop stack till condition false            

            stack.append((ind, heights[i]))
            # print(stack)
        
        # from remaining stack elements all are potential rectangles that can stretch till end, so compute max among their areas
        while stack:
            ind, height = stack.pop()
            area = (len(heights)-ind)*height
            ans =  max(area, ans)
            
        return ans


                    