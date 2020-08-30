#데크 이용
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def isPalindrome(head):
    from collections import deque
    q=deque()

    if not head:
        return True

    node=head
    while node is not None:
        q.append(node.val)
        node=node.next

    while len(q)>1:
        if q.popleft()!=q.pop():
            return False

    return True
