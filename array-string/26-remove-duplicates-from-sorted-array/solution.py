class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        unique = [prev]
        unique_count = 1

        for index in range(1, len(nums)):
            current = nums[index]
            if current != prev:
                unique.append(current)
                prev = current
                unique_count+=1
        
        for index in range(len(unique)):
            nums[index] = unique[index]

        return unique_count

