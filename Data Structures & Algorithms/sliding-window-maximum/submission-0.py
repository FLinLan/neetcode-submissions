class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        brute force, have a fixed window, recompute the maximum
        each time, give O(nk)
        
        to avoid this recomputation, we can remove all the elements
        that are smaller than the maximum, ensure that the maximum
        only ever exist in the same position inside our window,
        we can then retrieve it in O(1) time.

        ensure that the deque is in a monotonic decreasing order

        [1,2,1,0,4,2,6]  

        """
        dq = deque()
        ans = []

        for i in range(len(nums)):
            # remove elements out of the window
            if dq and dq[0] <= i-k: dq.popleft()
            
            # remove all smaller elements, ensure the dq[0] is always maximum
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i) 
            if dq[-1] >= k-1:
                ans.append(nums[dq[0]])
        
        return ans
            