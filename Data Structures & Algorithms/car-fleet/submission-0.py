class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_speed = [(a,b) for a,b in zip(position, speed)]
        car_speed_sorted = sorted(car_speed, reverse=True)
        time = []
        for cs in car_speed_sorted:
            t = (target - cs[0]) / cs[1]
            time.append(t)
            if len(time) >= 2 and t <= time[-2]:
                time.pop()

        return len(time)


