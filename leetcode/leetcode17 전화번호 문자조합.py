def letterCombinations(digits):
    # 예외처리
    if not digits:
        return []
    
    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl","6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result=[]

    def dfs(index,visit):
        # 다 돌면 백트래킹
        if len(visit)==len(digits):
            result.append(visit)
            return
        # 입력digits 하나씩 돌리며
        for i in range(index,len(digits)):
            # 숫자에 있는 문자 하나씩 반복
            for j in dic[digits[i]]:
                dfs(i+1,visit+j)

    dfs(0,"")
    return result


digits="23"
print(letterCombinations(digits))
