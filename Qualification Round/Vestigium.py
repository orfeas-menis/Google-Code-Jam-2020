import sys

T = int(sys.stdin.readline())

for x in range(1,T+1):
    k = 0 
    r = 0
    c = 0 
    N = int(sys.stdin.readline())
    rowSum = 0
    A = [[0 for x in range(N)] for y in range(N)] 
    for i in range(N): 
        sum = 0
        line = sys.stdin.readline()
        temp = (line.split(" ", N))
        temp[N-1] = temp[N-1][0:-1]
        for j in range(0,N):
            A[i][j] = int(temp[j])
            if (i==j):
                k = k + A[i][j]
    for i in range(N):
        if len(A[i]) != len(set(A[i])):
            r = r + 1 
        temp = []
        for j in range(N):
            temp.append(A[j][i])
        if (len(temp)) != len(set(temp)):
            c = c + 1
        
    print("Case #" + str(x) + ": " + str(k) + " " + str(r) + " " + str(c))
