def solution(n):
    answer = 0
    tmp=''

    if n==1:
        return 1
    else:
        while n > 0:
            tmp += str(n % 3)
            n = n // 3

        revere_tmp=tmp[::-1]

        for i in range(len(revere_tmp)):
            answer += (int(revere_tmp[i]) * pow(3,i))
        return answer

print(solution(45))
