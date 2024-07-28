class Solution:
    """
        points[i] ->  x start and x end -> horizontal diameter
        a baloon is burst by an arros shot at x if x start < x < x end
    """
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda lst: lst[0])
        reduced_intervals = [points[0]]

        for [x_start, x_end] in points[1:]:
            [prev_start, prev_end] = reduced_intervals.pop()
            if x_start > prev_end:
                reduced_intervals.append([prev_start, prev_end])
                reduced_intervals.append([x_start, x_end])
            else:
                x_end = min(x_end, prev_end)
                reduced_intervals.append([x_start, x_end])
        
        return len(reduced_intervals)
