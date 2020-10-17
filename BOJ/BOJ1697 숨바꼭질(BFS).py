n,k=map(int,input().split())
visit=[0]*100001

from collections import deque

def bfs(v):
    cnt=0
    q=deque([[v,cnt]])
    while q:
        x,cnt=q.popleft()   #위치랑 카운트
        if visit[x]!=1: #방문 하지않았으면
            visit[x]=1
            if x==k:
                return cnt
            cnt+=1
            if (x*2)<=100000:
                q.append([x*2,cnt])
            if (x+1)<=100000:
                q.append([x+1,cnt])
            if (x-1)>=0:
                q.append([x-1,cnt])
    return cnt

print(bfs(n))