T = int(input())
l = []
for i in range(T):
    t = input()
    l.append(t.split())
for i in l:
    if int(i[0])%int(i[1])==1:
        print("YES")
    elif int(i[0])%int(i[1])==int(i[1])-1:
        print("YES")
    else:
        print("NO")