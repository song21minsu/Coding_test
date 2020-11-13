def solution(dartResult):

    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'*': 2, '#': -1}

    score=[0,0,0]   #1~3번째 다트
    flag=-1 #숫자판별

    for i,dart in enumerate(dartResult):
        if dart.isdigit():
            flag+=1 #숫자니까 flag변환
            if dart=='0':
                continue
            elif dartResult[i+1].isdigit(): #뒤에 인덱스까지 숫자면 10이니까
                score[flag]=int(dart)*10
                flag-=1
            else:
                score[flag]=int(dart)

        elif dart in 'SDT':
            score[flag]= score[flag]**bonus[dart]

        else:
            if dart=='*':
                score[flag-1]*=2

            score[flag]*=option[dart]

    return sum(score)

print(solution('1S2D*3T'))
print(solution('1D2S#10S'))


# 깔끔한 풀이

# def solution(dartResult):
#     score = []
#     n = ''
#     for i in dartResult:
#         if i.isnumeric():
#             n += i
#         elif i == 'S':
#             score.append(int(n) ** 1)
#             n = ''
#         elif i == 'D':
#             score.append(int(n) ** 2)
#             n = ''
#         elif i == 'T':
#             score.append(int(n) ** 3)
#             n = ''
#         elif i == '*':
#             if len(score) > 1:
#                 score[-2] *= 2
#             score[-1] *= 2
#         elif i == '#':
#             score[-1] *= -1
#     return sum(score)