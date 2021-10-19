def DFS(sum, alist):
    if sum == m:
        print(sum)
        return
    else:
        for i, a in enumerate(alist):
            if ch[a[1]] == 0:
                ch[a[1]] = 1
                DFS(sum+a[0], a[i:])
                ch[a[1]] = 0

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    alist = [list(map(int,input().split())) for _ in range(n)]
    
    res = [0]*len(alist)
    ch = {}
    
    for a in alist:
        ch[a[1]] = 0
    
    DFS(0, alist)
