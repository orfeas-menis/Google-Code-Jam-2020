import sys

T = int(sys.stdin.readline())

for x in range(1,T+1):
    occupied = [-1,-1]  #occupied[0] => C, occupied[1] => J
    N = int(sys.stdin.readline())
    A = [] 
    result = [" " for x in range(N)]
    response = ""
    for i in range(N): 
        line = sys.stdin.readline()
        line = line[0:-1]
        times = line.split()
        A.append((int(times[0]),int(times[1]),i))

    A.sort(key=lambda tup: tup[0])
        
    for (start,end,position) in A:
        if occupied[0] <= start:
            result[position] = "C"
            occupied[0] = end
        elif occupied[1] <= start:
            result[position] = "J"
            occupied[1] = end
        else:
            response = "IMPOSSIBLE"
            break
    if response == "":
        for i in result:
            response = response + i
    print("Case #" + str(x) + ": " + response)
