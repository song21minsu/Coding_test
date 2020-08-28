# class Solution:
def evalRPN(tokens):
    num=[]
    cal=['-','+','*','/']
    for i in tokens:
        if i not in cal:
            num.append(int(i))
        else:
            num1=num.pop()
            num2=num.pop()
            print(num2,num1,i)
            if i=='+':
                num.append(num2+num1)
            elif i=='-':
                num.append(num2-num1)
            elif i=='*':
                num.append(num2*num1)
            elif i=='/':
                num.append(int(num2/num1))
    return num[0]
tokens=["4","-2","/","2","-3","-","-"]
# tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# tokens=["2", "1", "+", "3", "*"]
# tokens=["4", "13", "5", "/", "+"]
print(evalRPN(tokens))
