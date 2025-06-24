class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n=input()
value=list(map(int,input().split()))
m=int(input())
g=list(map(Node,value))
for i in range(len(g)-1):
    g[i].next=g[i+1]
x=g[0]
while(True):
    if m!=x.data:
        print(x.data,end=" ")
    if x.next!=None:
        x=x.next
    else:
        break;
