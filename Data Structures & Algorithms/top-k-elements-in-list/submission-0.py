class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        max_heap = []
        for num, freq in count.items():
            heapq.heappush(max_heap, (-1*freq, num))        
        
        ans = []
        for _ in range(k):
            freq, num = heapq.heappop(max_heap)
            ans.append(num)

        return ans
