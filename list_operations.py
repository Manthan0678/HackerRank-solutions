if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        A = input().split()
        if A[0] == "insert":
            l.insert(int(A[1]),int(A[2]))
        elif A[0] == "print":
            print(l)
        elif A[0] == "remove":
            l.remove(int(A[1]))
        elif A[0] == "append":
            l.append(int(A[1]))
        elif A[0] == "sort":
            l.sort()
        elif A[0] == "pop":
            l.pop()
        elif A[0] == "reverse":
            l.reverse()