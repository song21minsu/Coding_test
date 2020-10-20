from itertools import combinations
def solution(numbers):
    answer = []

    for i in combinations(numbers,2):
        num=sum(i)
        if num in answer:
            continue
        else:
            answer.append(num)

    return sorted(answer)


print(solution([2,1,3,4,1]))