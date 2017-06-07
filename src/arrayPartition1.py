class Solution(object):
    def ArrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        l = len(nums)
        sum = 0

        for i in range(0,l,2):
        	sum = sum + nums[i]

        return sum

