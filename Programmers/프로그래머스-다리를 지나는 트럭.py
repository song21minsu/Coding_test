def solution(b_length, b_weight, t_weight):
    answer=0
    q=[0]*b_length
    while q:
        answer+=1
        q.pop(0)
        if t_weight:
            if sum(q)+t_weight[0]<=b_weight:
                q.append(t_weight.pop(0))
                print(q)
            else:
                q.append(0)
                print(q)
    return answer


print(solution(2,10,[7,4,5,6]))
