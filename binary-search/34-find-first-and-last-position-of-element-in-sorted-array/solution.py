class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
            
        left, right = 0, len(nums) - 1
        mid = 0
        found = False

        while left != right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                found = True
                break
        
        if not found and nums[left] != target:
            return [-1, -1]
  
        end_l = mid
        mid_l = 0
        while end_l > left:
            mid_l = (left+end_l)//2
            if nums[mid_l] == target:
                end_l = mid_l
            else:
                left = mid_l + 1
        end_l = left if nums[left] == target else end_l

        end_r = right 
        start_r = mid
        mid_r = 0
        while start_r < end_r:
            mid_r = (start_r+end_r)//2
            if nums[mid_r] == target:
                start_r = mid_r + 1
            else:
                end_r = mid_r

        end_r = end_r if nums[end_r] ==target else end_r - 1   
        return [end_l, max(end_l, end_r)]
