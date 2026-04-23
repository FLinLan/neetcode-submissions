class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1

        while L <= R:
            combine = numbers[L] + numbers[R]
            if combine == target:
                return [L+1, R+1]
            elif combine < target:
                L += 1
            else:
                R -= 1
        
        return [-1, -1]
        