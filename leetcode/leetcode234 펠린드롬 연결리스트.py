from collections import deque
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q=deque()

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True


sol=Solution()
test1 = ListNode(1)
test2 = ListNode(2, test1)

head1=test2

print(sol.isPalindrome(head1))

test1 = ListNode(1)
test2 = ListNode(2, test1)
test3 = ListNode(2, test2)
test4 = ListNode(1, test3)

head2=test4

print(sol.isPalindrome(head2))