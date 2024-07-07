class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        mini_heap = [[nums2[0] + u, i, 0] for i, u in enumerate(nums1[:k])]
        heapq.heapify(mini_heap)
        length_nums2 = len(nums2)
        answer = [ ]

        while k and mini_heap:
            min_elem = heapq.heappop(mini_heap)
            num1_index = min_elem[1]
            num2_index = min_elem[2]
            answer.append([nums1[num1_index], nums2[num2_index]])
            k -= 1

            if num2_index + 1 < length_nums2:
                my_sum = nums1[num1_index] + nums2[num2_index+1]
                next_elem = [my_sum, num1_index, num2_index+1]
                heapq.heappush(mini_heap, next_elem)
            
        return answer
        
     
        
