def readFile(fileName):
    with open(fileName) as f:
        strLst = f.readlines()
    floatlist = []
    for s in strLst:
        floatlist.append(float(s))
    return floatlist


lst1 = readFile("MP09Data1.txt")
lst2 = readFile("MP09Data2.txt")

idx1, idx2 = 0, 0

while idx1 < len(lst1) and idx2 < len(lst2):
    if lst1[idx1] >= lst2[idx2]:
        print(lst1[idx1])
        idx1 += 1
    else:
        print(lst2[idx2])
        idx2 += 1

# 윗 단계에서 어느부분에서 멈췄는지 알수 없기에
while idx1 < len(lst1):
    print(lst1[idx1])
    idx1 += 1
while idx2 < len(lst2):
    print(lst2[idx2])
    idx2 += 1

# elif lst1[idx1] < lst2[idx2]

# print(lst1, lst2)
