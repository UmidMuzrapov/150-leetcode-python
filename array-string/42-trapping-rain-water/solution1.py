class Solution:
    def trap(self, height: List[int]) -> int:
        left = self._precalculate_left(height)
        right = self._precalculate_right(height)
        area = 0

        for i, val in enumerate(height):
            local_area = min(left[i], right[i]) - val
            area += local_area if local_area > 0 else 0
        
        return area


    def _precalculate_left(self, height):
        prev = -1
        left = []

        for i, val in enumerate(height):
            left.append(prev)
            prev = max(prev, height[i])
        
        return left
    
    def _precalculate_right(self, height):
        prev = -1
        right = [0 for _ in range(len(height))]

        for i in range(len(height)-1, -1, -1):
            right[i] = prev
            prev = max(prev, height[i])

        return right
