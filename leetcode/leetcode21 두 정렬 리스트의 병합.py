class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self,l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val>l2.val):
        l1,l2=l2,l1
    if l1:
        l1.next=self.mergeTwoLists(l1.next,l2)
    return l1

l1=ListNode([1,2,4])
l2=ListNode([1,3,4])
# print(mergeTwoLists(self,l1,l2))
