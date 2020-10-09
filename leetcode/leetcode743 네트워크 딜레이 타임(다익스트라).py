# 노드 개수:n, k:출발정점, u:출발지, v:도착지, w:소요시간

def networkDelayTime(times,n,k):
    from collections import defaultdict
    graph=defaultdict(list)

    for u,v,w in times:
        graph[u].append((v,w))
    #q : (소요시간, 정점)
    q=[(0,k)]
    dist=defaultdict(int)

    #우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while q:
        import heapq
        time,node = heapq.heappop(q)
        if node not in dist:
            dist[node] = time
            for v,w in graph[node]:
                alt = time+w
                heapq.heappush(q,(alt,v))

    #모든 노드의 최단경로가 존재하는지 여부
    if len(dist) == n:
        return max(dist.values())
    return -1


print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))
print(networkDelayTime([[3,1,5],[3,2,2],[2,1,2],[3,4,1],[4,5,1],[5,6,1],[6,7,1],[7,8,1],[8,1,1]],8,3))