class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        original = [x for x in nums]
        index = 0
        length = len(nums)
        split = length - (k%length)

        for original_i in range(split, length):
            nums[index] = original[original_i]
            index+=1
        
        for original_i in range(0, split):
            nums[index] = original[original_i]
            index+=1
    
