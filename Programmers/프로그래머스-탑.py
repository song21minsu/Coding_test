def solution(h):
    answer=[0]*len(h)    #[0,0,0,0,0]
    for i in range(len(h)-1,-1,-1): #i=4~0
        for j in range(i-1,-1,-1):  #j=3~0
            if h[j]>h[i]:
                answer[i]=j+1
                break
    return answer

# print(solution([3,9,9,3,5,7,2]))
# print(solution([1,5,3,6,7,6,5]))
print(solution([6,9,5,7,4]))
