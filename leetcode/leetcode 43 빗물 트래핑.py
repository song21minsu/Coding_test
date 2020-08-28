# 투 포인터 사용
# def trap(height):
#     if not height:
#         return 0
#
#     answer=0
#     left=0
#     right=len(height)-1
#     left_max=height[left]
#     right_max=height[right]
#
#     while left<right:
#         left_max=max(height[left],left_max)
#         right_max=max(height[right],right_max)
#
#         if left_max<=right_max:
#             answer+=(left_max-height[left])
#             left+=1
#         else:
#             answer+=(right_max-height[right])
#             right-=1
#     return answer
#
# print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))


#스택사용
def trap(height):
    stack=[]
    volume=0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top=stack.pop()

            if not len(stack):
                break

            distance=i-stack[-1]-1
            waters=min(height[i],height[stack[-1]],height[top])

            volume+=distance*waters

        stack.append(i)
    return volume

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
