import sys

n,start,end=map(int,input().split())
q=[]

inf=sys.maxsize

tree=[[] for _ in range(n+1)]
