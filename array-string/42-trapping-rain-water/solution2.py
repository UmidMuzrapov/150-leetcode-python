class Solution:
    def trap(self, height: List[int]) -> int:
        max_height = max(height)
        blocks_area = sum(height)

        left = 0
        right = len(height) - 1
        trapped_water = 0

        for val in range(1, max_height + 1):
            
            while height[left] < val:
                left+=1
            
            while height[right] < val:
                right-=1
            
            trapped_water+=(right - left + 1)

        return trapped_water - blocks_area
