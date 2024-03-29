'''
파일이 없는
경우와 문자열에서 실수로 변환하면서 오류가 발생
할 수 있는 경우에 대해 예외 처리하는 코드를 추가
'''



def readFile(fileName):
    try:
        with open(fileName) as f:
            strLst = f.readlines()
        floatlist = []
        for s in strLst:
            try:
                floatlist.append(float(s))
            except ValueError:
                continue
        return floatlist
    except FileNotFoundError:
        print(fileName + "을 찾을 수 없습니다.")
        return 0


lst1 = readFile("MP09Data1.txt")
lst2 = readFile("MP09Data2.txt")

if lst1 == 0 or lst2 == 0:
    pass
else:
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
