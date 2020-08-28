# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
        # head=[1,2,3,4,5], n=2 뒤에서 n번째 삭제
        tmp=[]
        while head:
            tmp.append(head.val)
            head=head.next
        # print(tmp)
        new_tmp=[]
        for i in tmp:
            for j in i:
                new_tmp.append(j)
        # print(new_tmp)
        cnt=len(new_tmp)
        ans=[]
        for i in range(len(new_tmp)):
            if (cnt-i)==n:
                continue
            else:
                ans.append(new_tmp[i])
        print(ans)
        head=ListNode(0)
        cur=head
        for i in ans:
            cur.next=ListNode(i)
            cur=cur.next
        return head.next
        # pass
head=ListNode([1,2,3,4,5])
print(Solution.removeNthFromEnd(head,2))
