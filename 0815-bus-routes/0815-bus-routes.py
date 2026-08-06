from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0

        stop_to_buses = defaultdict(list)

        for bus_id, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus_id)

        if source not in stop_to_buses or target not in stop_to_buses:
            return -1

        queue = deque([source])
        stops_visited = {source}
        buses_taken = set()

        buses = 0

        while queue:
            buses += 1

            for _ in range(len(queue)):
                stop = queue.popleft()

                for bus in stop_to_buses[stop]:

                    if bus in buses_taken:
                        continue

                    buses_taken.add(bus)

                    for nxt in routes[bus]:

                        if nxt == target:
                            return buses

                        if nxt not in stops_visited:
                            stops_visited.add(nxt)
                            queue.append(nxt)

        return -1