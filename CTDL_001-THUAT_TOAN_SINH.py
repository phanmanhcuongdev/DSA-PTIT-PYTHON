n=int(input())
a=[0]*(n)
def generation(i):
    if i==n:
        reserve_a=a[::-1]
        if a==reserve_a:
            print(*a)
        return
    a[i]=0;
    generation(i+1)
    a[i]=1
    generation(i+1)

generation(0);
