from collections import deque

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    q = deque(map(int,input().split()))
    cnt=0
    while q:
        top=max(q)
        m-=1
        pop=q.popleft()
        if top!=pop:
            q.append(pop)
            if m<0:
                m=len(q)-1
        else:
            cnt+=1
            if m==-1:
                print(cnt)
                break
