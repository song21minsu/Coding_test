def solution(q,location):
    answer=0
    while q:
        if q[0]==max(q):
            answer+=1
            q.pop(0)
            if location==0:
                return answer
            else:
                location-=1
        else:
            q.append(q.pop(0))
            if location==0:
                location=len(q)-1
            else:
                location-=1
    return answer
print(solution([1, 1, 9, 1, 1, 1],0))
