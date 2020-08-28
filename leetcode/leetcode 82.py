import collections
def deleteDuplicates(head):
    dic=collections.Counter(head)
    ans=[]
    for k,v in dic.items():
        if v==1:
            ans.append(k)
    return ans

print(deleteDuplicates([1,2,3,3,4,4,5]))
