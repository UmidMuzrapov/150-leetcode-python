class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        my_list = []
        count = 0

        for num in nums:
            if num != val:
                my_list.append(num)
                count += 1
        
        for i in range(count):
            nums[i] = my_list[i]

        return count
