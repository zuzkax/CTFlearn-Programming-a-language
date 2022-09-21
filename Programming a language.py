flag = [0]

n = input()

for i in n:
    if i == '.':
        flag.append(flag[len(flag)-1])
    elif i == '-':
        flag[len(flag)-1] -= 1
    elif i == '+':
        flag[len(flag)-1] += 1
    elif i == '@':
        flag[len(flag)-1], flag[len(flag)-2] = flag[len(flag)-2], flag[len(flag)-1]
    elif i == '>':
        flag.append(flag[0])
        del flag[0]
    elif i == '<':
        ostatni = flag[len(flag)-1]
        flag[len(flag)-1] == 0
        for x in range(len(flag)-1,0,-1):
            flag[x] = flag[x -1]
        flag[0] = ostatni

print(flag)
