# # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1=[]
list2=[]
for i in range(len(list1)):
    list1.append(list1[i]*pow(10,(len(list1)-(i+1))))
for i in range(len(list2)):
    list2.append(list2[i]*pow(10,(len(list2)-(i+1))))
tot_list1=sum(list1)
tot_list2=sum(list2)
answer=list(map(int,str(tot_list1+tot_list2)))
ans=[]
for i in range(len(answer)-1,-1,-1):
    ans.append(answer[i])


head=ListNode(0)
cur=head
for i in ans:
    cur.next=ListNode(i)
    cur=cur.next
print(cur)
