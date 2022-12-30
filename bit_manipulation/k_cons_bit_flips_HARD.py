'''
You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].
'''


class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        
        flips = 0


        # global pointer, that is updated to track only flips due to past i-k or curr-window number of element flips
        num_flips_i_by_prev_windows = 0
        # has_flipped_i will help updated above variable correctly
        has_flipped_i = [False]*len(nums)

        for i in range(0, len(nums)):
            
            # after the first window
            if i>=k:
                # for ith index, the num_flips_i_by_prev_windows doesnt get affected by
                # windows that start on or before i-k, so we decrement the increased num_flips_i_by_prev_windows due to them
                # to keep a only valid flip count due to previous window range.
                if has_flipped_i[i-k]:
                    num_flips_i_by_prev_windows-=1
            
            # if nums[i] is 1 and previous window flips are odd, then 1 became 0 and 1 has to be made 1 again
            # similarly if nums[i] is 0 and prev window flips are even, then 0 became 0 and has to be made 1 again
            if num_flips_i_by_prev_windows % 2 == nums[i]:
                # as we need to flip and ran out of window space at end
                if i>len(nums)-k:
                    return -1
                flips+=1
                num_flips_i_by_prev_windows+=1
                has_flipped_i[i] = True
        
        return flips