from collections import defaultdict
from collections import deque


n=int(input())  #전체 사람의 수
man1,man2=map(int,input().split())   # 계산해야하는 두 사람
m=int(input())
arr=[list(map(int,input().split())) for _ in range(m)] # (x,y) : x는 y의 부모

dic=defaultdict(list)
for x,y in arr:
    dic[x].append(y)
    dic[y].append(x)
# print(dic)

def bfs(start,dic,end):
    visit=set()
    q=deque()
    q.append((0,start))
    while q:
        cnt,v=q.popleft()
        visit.add(v)
        if v==end:
            return cnt
        for i in dic[v]:
            if i not in visit:
                visit.add(i)
                q.append((cnt+1,i))
    return -1


print(bfs(man1,dic,man2))