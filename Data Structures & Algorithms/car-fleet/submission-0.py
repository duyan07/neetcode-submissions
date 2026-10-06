class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = []

        for pos, spd in cars:
            t = (target - pos) / spd
            if not fleets or t > fleets[-1]:
                fleets.append(t)
        
        return len(fleets)