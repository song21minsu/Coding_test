def findItinerary(tickets):

    from collections import defaultdict
    graph=defaultdict(list)
    # 그래프를 역순으로 구성해서 pop사용
    for a,b in sorted(tickets,reverse=True):
        graph[a].append(b)

    visit=[]
    def dfs(a):
        # 마지막값(역순으로해서 pop)을 어휘 순으로 방문
        while graph[a]:
            dfs(graph[a].pop())
        visit.append(a)
    dfs('JFK')
    # 역순으로 그래프를 구성했으니 뒤집어서 리턴
    return visit[::-1]

print(findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print(findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))