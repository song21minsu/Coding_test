from collections import Counter
def removeDuplicateLetters(s):
    stack=[]
    counter=Counter(s)

    for char in s:
        counter[char]-=1
        if char in stack:
            continue
        while stack and char<stack[-1] and counter[stack[-1]]>0:
            stack.pop()
        stack.append(char)

    return ''.join(stack)

# s="bcabc"
s="cbacdcbc"
print(removeDuplicateLetters(s))