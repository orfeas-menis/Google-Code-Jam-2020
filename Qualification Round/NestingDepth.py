import sys

T = int(sys.stdin.readline())

for x in range(1,T+1):
    line = sys.stdin.readline()
    line = line[0:-1]
    myList = [num for num in line]
    openParentheses = 0
    result = ""
    for i in myList:
        if int(i) == openParentheses:
            result = result + i
        elif int(i) < openParentheses:
            while int(i) < openParentheses:
                openParentheses = openParentheses - 1
                result = result + ")"
            result = result + i
        else:
            while int(i) > openParentheses:
                openParentheses = openParentheses + 1
                result = result + "("
            result = result + i
    for i in range(openParentheses):
        result = result + ")"

    print("Case #" + str(x) + ": " + result)
