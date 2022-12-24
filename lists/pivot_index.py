'''Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11'''

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_left = [x for x in nums]
        nums_right = [x for x in nums]
        
        for i in range(0,len(nums)):
            j = len(nums)-i-1

            if i!=0:
                nums_left[i]+=nums_left[i-1]
            if j!=len(nums)-1:
                nums_right[j]+=nums_right[j+1]
            
        for i in range(0, len(nums)):
            sum_left = nums_left[i]-nums[i] if i!=0 else 0
            sum_right = nums_right[i]-nums[i] if i!=len(nums)-1 else 0
            if sum_left == sum_right:
                return i
        
        return -1

            