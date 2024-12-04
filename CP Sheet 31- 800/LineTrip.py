def solve(arr ,k):
    arr1=[0]
    arrf=arr1+arr
    num=2*(k-arrf[-1])
    arrf.append(num+arrf[-1])
    maxgap=0
    for i in range(len(arrf)-1):
        currgap=arrf[i+1]-arrf[i]
        if currgap>maxgap:
            maxgap=currgap
        currgap=0
    return maxgap




t = int(input())
while t:
    n,k = list(map(int,input().split()))
    
    arr = list(map(int, input().split()))
    
    print(solve(arr,k))
    t-=1