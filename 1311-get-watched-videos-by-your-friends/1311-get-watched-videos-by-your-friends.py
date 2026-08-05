class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue=deque([id])

        visited={id}
        for i in range(level):
            for _ in range(len(queue)):
                x=queue.popleft()
                for nei in friends[x]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
        d={}
        for p in queue:
            for videos in watchedVideos[p]:
                d[videos]=d.get(videos,0)+1
        return sorted(d.keys(),key=lambda x:(d[x],x))