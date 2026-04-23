class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine position and speed into a list of tuples and sort by position in descending order
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []  # Stack to store the time it takes each car/fleet to reach the target
        
        for p, s in cars:
            time = (target - p) / s  # Time for the car to reach the target
            
            # If the current car takes LESS time than the fleet in front,
            # it will catch up and join that fleet
            if not stack or time > stack[-1]:
                stack.append(time)
            
        return len(stack)