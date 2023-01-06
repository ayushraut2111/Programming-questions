class Solution:
    def countGoodTrips(self, n, k, roads):
        # code here
        good_trips = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                for l in range(1, n+1):
                    if (i != j and i != l and j != l):  # exclude trips that don't involve travel
                        has_highway = False
                        for road in roads:
                            if ((road[0] == i and road[1] == j) or (road[0] == j and road[1] == l) or (road[0] == l and road[1] == i)):  # check if any of the roads in the trip involve a highway
                                has_highway = True
                                break
                        if has_highway:
                            good_trips += 1
        return good_trips