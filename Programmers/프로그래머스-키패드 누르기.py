def solution(numbers, hand):
    answer = ''

    left=[1,4,7]
    right=[3,6,9]
    mid=[2,5,8,0]
    handL='*'
    handR='#'
    dict = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2),
                '*': (3, 0), 0: (3, 1), '#': (3, 2)}

    while numbers:
        tmp=numbers.pop(0)
        dist=0
        if tmp in left:
            answer+='L'
            handL=tmp
        elif tmp in right:
            answer+='R'
            handR=tmp
        else:
            leftdidt=abs(dict[handL][0]-dict[tmp][0])+abs(dict[handL][1]-dict[tmp][1])
            rightdidt=abs(dict[handR][0]-dict[tmp][0])+abs(dict[handR][1]-dict[tmp][1])
            if leftdidt>rightdidt:
                answer+='R'
                handR=tmp
            elif leftdidt<rightdidt:
                answer += 'L'
                handL = tmp
            else:
                if hand=='right':
                    answer += 'R'
                    handR = tmp
                else:
                    answer += 'L'
                    handL = tmp

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))