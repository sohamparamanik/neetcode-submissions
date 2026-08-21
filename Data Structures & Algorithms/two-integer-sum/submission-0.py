class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        ha={}
        for i in range (0,n):
            remainder = target - nums[i]
            if remainder in ha:
                return[ha[remainder],i]
            ha[nums[i]]=i    

        