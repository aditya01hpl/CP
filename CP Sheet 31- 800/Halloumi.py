
def solve(arr, k):
    newarr=sorted(arr)
    if k <= 1 and arr != newarr:
        
        return False
    else:
        return True


t = int(input())
while t:
    n,k = list(map(int,input().split()))
    
    arr = list(map(int, input().split()))
    
    if(solve(arr, k)):
        print("Yes")
    else:
        print("No")
    t-=1
