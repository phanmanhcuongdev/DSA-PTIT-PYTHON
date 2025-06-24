class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    seen=set()
    cur=head
    prev=None

    while cur:
        if cur.data in seen:
            prev.next=cur.next
        else:
            seen.add(cur.data)
            prev=cur
        cur = cur.next

def print_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Đọc dữ liệu
n = int(input())
value = list(map(int, input().split()))

# Tạo danh sách liên kết
g = list(map(Node, value))
for i in range(len(g) - 1):
    g[i].next = g[i + 1]

head = g[0]

# Xoá phần tử trùng
remove_duplicates(head)

# In kết quả
print_list(head)
