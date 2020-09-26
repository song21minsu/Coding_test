def combine(n,k):
    from itertools import combinations
    answer=list(combinations(range(1,n+1),k))
    return answer



n,k=4,2
print(combine(n,k))