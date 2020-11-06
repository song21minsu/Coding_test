def solution(n):
    answer = 0
    tmp=''

    if n==1:
        return 1
    else:
        while n//3>=1:
            nam=n%3
            n=n//3
            tmp=str(nam)+tmp
            if n<3:
                tmp=str(n)+tmp

        revere_tmp=tmp[::-1]

        for index,i in enumerate(revere_tmp):
            answer+=int(i)*pow(3,len(revere_tmp)-index-1)

        return answer

print(solution(45))