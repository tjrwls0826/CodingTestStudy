pop = {"종로구": 156567, "중구": 133708, "용산구": 112881, "성동구": 135}

a = input("구 이름을 입력 ")

if a in pop:
    print(pop[a])
else:
    print("해당 구 정보가 없습니다.")
