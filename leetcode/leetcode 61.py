class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def rotateRight(head,k):
    if not head or not head.next or not k:
        return head
    cur = head
    len = 1
    while cur.next:
        len+=1
        cur=cur.next
    cur.next=head
    cur=head
    mod=len-k%len
    while mod-1>0:
        cur=cur.next
        mod-=1
    new_head=cur.next
    cur.next=None
    return new_head

head=ListNode([1,2,3,4,5])

if __name__ =="__main__":
    print(rotateRight(head,2))
