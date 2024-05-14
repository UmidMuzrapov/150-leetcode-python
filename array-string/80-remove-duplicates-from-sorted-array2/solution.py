class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        prev_count = 1
        elements_to_examine = len(nums) - 1
        index = 1
        count = 1

        for _ in range(elements_to_examine):
            current = nums[index]

            if current == prev:
                
                if (prev_count == 2):
                    nums.pop(index)
                else:
                    prev_count+=1
                    index+=1
                    count+=1
            else:
                prev = current
                prev_count=1
                index+=1
                count+=1
        
        return count



