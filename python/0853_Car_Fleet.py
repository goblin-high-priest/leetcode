class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        fleet_time = 0

        for pos, velocity in cars:
            time = (target - pos) / velocity

            if time > fleet_time:
                fleets += 1
                fleet_time = time
            
        return fleets
