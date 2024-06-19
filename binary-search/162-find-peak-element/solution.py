class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left!=right:
            mid = (right+left)//2
            if nums[mid+1] > nums[mid]:
                left = mid + 1
            elif nums[mid-1] > nums[mid]:
                right = mid
            else:
                return mid
        
        return left
            
