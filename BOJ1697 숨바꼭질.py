from collections import deque

n,k = map(int,input().split())
arr=[0]*100001
def bfs(n,k):
    q=deque()
    q.append(n)

    while q:
        v=q.popleft()
        if v==k:
            return arr[v]
        for d in (v-1,v+1,v*2):
            if 0<=d<100001 and arr[d]==0:
                arr[d]=arr[v]+1
                q.append(d)
print(bfs(n,k))

