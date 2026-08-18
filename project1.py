X = int(input())
S = input().split()
N = int(input())
price = 0
for i in range(N):
    size_money = input().split()
    for j in range (len(S)):
        if size_money[0] == S[j]:
            S.remove(size_money[0])
            price += int(size_money[1])
            break
print(price)
