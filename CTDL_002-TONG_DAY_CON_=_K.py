m=list(map(int,input().split()))
b=list(map(int,input().split()))
n=m[0]
sum=m[1]
cnt=0
a = [0]*n;

def inra():
    for i in range(n):
        if a[i]==1:
            print(b[i],end=" ")
    print()

def check():
    x=0
    for i in range(n):
       if a[i]==1:
           x+=b[i]
    if x==sum:
        return True
    else:
        return False

def generation(i):
    global cnt
    if i==n:
        if check():
            inra()
            cnt+=1
        return
    a[i]=0
    generation(i+1)
    a[i]=1
    generation(i+1)

generation(0)
print(cnt)
