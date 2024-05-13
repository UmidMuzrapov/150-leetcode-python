class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = 0
        temp = []

        while index < m:
            temp.append(nums1[index])
            index+=1
        
        index = 0
        while temp or nums2:
            num = 0
            if temp and nums2:
                num = nums2.pop(0) if nums2[0] <= temp[0] else temp.pop(0)
            elif not temp:
                num = nums2.pop(0)
            else:
                num = temp.pop(0)
            
            nums1[index] = num
            index+=1

