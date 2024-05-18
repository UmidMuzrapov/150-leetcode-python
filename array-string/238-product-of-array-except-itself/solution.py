class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = [1]
        n = len(nums)

        for i in range(1, n):
            pre.append(nums[i-1]*pre[i-1])
            post.append(post[i-1]*nums[n-i])
            
        return [pre[i]*post[n-i-1] for i in range(n)]
