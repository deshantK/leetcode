import heapq
def solve(target, startFuel, stations):
    cnt = 0
    index = 0
    heap = []
    if len(stations) ==0:
        if target > startFuel:
            return -1
        else:
            return 0
    sofar = 0

    while target > startFuel:
        if index < len(stations):
            fuel = stations[index][0]

            if startFuel < fuel:
                while heap and startFuel < fuel:
                    startFuel -= heapq.heappop(heap)
                    cnt +=1
                if startFuel < fuel:
                    return -1
            heapq.heappush(heap, -stations[index][1])
            index +=1
        else:
            while heap and startFuel < target:
                startFuel -= heapq.heappop(heap)
                cnt +=1
            if startFuel < target:
                return -1
    return cnt

target = 100
startFuel = 50
stations = [[25,25],[50,50]]
print (solve(target, startFuel, stations))
