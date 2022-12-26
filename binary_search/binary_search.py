'''Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==1:
            if target==nums[0]:
                return 0
            else:
                return -1


        start = 0
        end = len(nums)-1

        while start<=end:
            mid = (start+end)//2
            if nums[mid]>target:
                end = mid-1
            elif nums[mid]<target:
                start = mid+1
            else:
                return mid
        return -1