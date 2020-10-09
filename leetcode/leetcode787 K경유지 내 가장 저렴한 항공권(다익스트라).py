#시작점:src, 도착점:dst, 경유지 제한:k, 노드수:n
def findCheapestPrice(n,flights,src,dst,k):
    from collections import defaultdict
    graph = defaultdict(list)

    for u, v, w in flights:
        graph[u].append((v, w))
    # q : (소요값, 시작점), cnt : 경유횟수
    cnt=0
    q = [(0,src,cnt)]

    while q:
        import heapq
        price, node, cnt = heapq.heappop(q)

        if node==dst:
            return price

        # 경유횟수 제한인것만 우선순위큐에 추가
        if cnt<=k:
            cnt+=1
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(q, (alt, v, cnt))
    return -1

print(findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1))
print(findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0))