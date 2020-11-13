def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        tmp=str(bin(i|j))[2:]
        tmp = '0' * (n - len(tmp)) + tmp
        tmp=tmp.replace('1','#')
        tmp=tmp.replace('0',' ')
        answer.append(tmp)
    return answer


print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))