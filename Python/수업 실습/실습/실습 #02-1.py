'''
자동차의 연비는 10km/liter(리터) 라고 가정
 평균 가솔린 값은 1900원/liter으로 가정
 자동차로 이동할 때 평균 속도는 40km/hour로 가정
 2022년 시간당 최저 임금은 9160원
'''

oilprice1km = 190
# 키로미터당 60/40 분
carkmtime = 60/40
print("키로미터당 분",carkmtime)
workprice = 9160 / 60
print("분당 임금",workprice)
ofAdistnce = int(input("A의 거리"))
ofAprice = int(input("A의 가격"))
A = ofAprice + (ofAdistnce * oilprice1km + ofAdistnce * carkmtime * workprice)*2
print(f"A의 가격은{A}")

ofBdistnce = int(input("B의 거리"))
ofBprice = int(input("B의 가격"))
B = ofBprice + (ofBdistnce * oilprice1km + ofBdistnce * carkmtime * workprice)*2
print(f"B의 가격은{B}")

onprice = int(input())
ondelivery = int(input())


