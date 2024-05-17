class Solution:
    """
        3 2 1 0 4
        2 3 1 1 1
        for my current max jum
            if (currentindex + max_jum >= length) return True
            explore in that range if there is a jump that could increase the range
            choose that one 

        

    """
    def canJump(self, nums: List[int]) -> bool:
        index = 0
        length = len(nums)
        local_max = 0
        prev = index

        while index < length:
            if index + nums[index] >= length - 1:
                return True

            prev = index 
            index = localMaxJump(nums, index)
            if (index == prev and index + nums[index] < length - 1):
                return False

        return True
            
def localMaxJump(nums, start):
    max_jump = nums[start]
    max_index = start
    end = start + max_jump + 1

    for index in range(start+1, end):
        jump = index + nums[index]
        if jump > max_jump:
            max_jump = jump
            max_index = index

    return max_index
        


