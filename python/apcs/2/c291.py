n = int(input())
fl = [int(x) for x in input().split()]
visited = [False] * n
cnt = 0
for i in range(n):
    if not visited[i]:
        cnt += 1
        curr = i
        while not visited[curr]:
            visited[curr] = True
            curr = fl[curr]
print(cnt)