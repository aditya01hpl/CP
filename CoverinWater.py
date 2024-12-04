def solve(arr):
    for i in range(len(arr)-2):
        n, nn, nnn = i, i+1, i+2
        if (arr[n] == '.' and arr[nn] == '.' and arr[nnn] == '.'):
            return 2
        
    return arr.count('.')


t = int(input())
while t:
    n = int(input())
    arr = list(input())
    print(solve(arr))
    t -= 1
