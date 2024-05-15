class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = {num:0 for num in nums}

        for num in nums:
            my_dict[num]+=1
        
        for key in my_dict.keys():
            if my_dict[key] > len(nums)//2:
                return key

