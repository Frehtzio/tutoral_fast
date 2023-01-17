from collections import deque
a = deque()

a.append(3)

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        l = r = 0
        q = deque()
        res = []
        
        while r < len(nums):
            print(q)
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if l > q[0]:
                q.popleft()
                
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r +=1 
        return res
                

        
            



s = Solution()                
ss = s.maxSlidingWindow(nums = [7,2,4], k = 2)
print(ss)