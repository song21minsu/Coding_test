from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def isPalindrome(head: ListNode) -> bool:
    q=deque()

    if not head:        # 빈 연결리스트면 팰린드롬
        return True

    node=head
    while node is not None:
        q.append(node.val)
        node=node.next

    while len(q)>1:
        if q.popleft() != q.pop():
            return False

    #자료를 다 돌렸는데 안걸리면
    return True
