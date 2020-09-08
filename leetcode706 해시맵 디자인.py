class MyHashMap:

    def __init__(self):
        from collections import defaultdict
        """
        Initialize your data structure here.
        """
        self.size=1000
        self.table= defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index=key%self.size
        # 인덱스에 노드가 없으면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index]=ListNode(key,value)
            return (key,value)
        # 인덱스에 노드가 있으면 노드연결
        p=self.table[index]
        while p:
            if p.key==key:
                p.value=value
                return (key,value)
            if p.next is None:
                break
            p=p.next
        p.next=ListNode(key,value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index=key%self.size
        if self.table[index] is None:
            return -1

        # 노드가 있으면 키 탐색
        p=self.table[index]
        while p:
            if p.key==key:
                return p.value
            p=p.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index=key%self.size
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일 때 삭제
        p=self.table[index]
        if p.key==key:
            if p.next is None:
                self.table[index] = ListNode()
            else :
                self.table[index] = p.next
            return key

        # 연결리스트 노드 삭제
        prev=p
        while p:
            if p.key==key:
                prev.next=p.next
                return
            prev=p
            p=p.next

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value=value
        self.next = None

# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
print(obj.put(1,1))
print(obj.put(2,2))
print(obj.get(1))
print(obj.get(3))
print(obj.put(2,1))
print(obj.remove(2))
print(obj.remove(1))
print(obj.get(2))