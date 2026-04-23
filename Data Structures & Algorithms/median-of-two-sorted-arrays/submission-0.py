class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
                
        total = len(nums1) + len(nums2)
        half = total // 2

        low, high = 0, len(nums1) - 1
        while True:
            mid1 = (low + high) // 2
            mid2 = half - mid1 - 2
            
            # [1, 2, 3]

            """
            1 | 2
              | 3
            """
            l1 = nums1[mid1] if mid1 >= 0 else float('-inf')
            r1 = nums1[mid1+1] if mid1+1 < len(nums1) else float('inf')
            l2 = nums2[mid2] if mid2 >= 0 else float('-inf')
            r2 = nums2[mid2+1] if mid2+1 < len(nums2) else float('inf')

            print(l1, l2, r1, r2)

            if l1 <= r2 and l2 <= r1:
                if total % 2 == 1:
                    return min(r1, r2)
                else: 
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                # element too large in search array, elminate larger half
                high = mid1 - 1
            else:
                low = mid1 + 1
        
        return 0.0