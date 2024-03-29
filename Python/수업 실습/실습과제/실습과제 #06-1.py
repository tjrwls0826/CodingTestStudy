'''
 2~100에 대해 각각 약수를 구해 리스트를 구성한
후 출력하는 프로그램 작성
 리스트 구성 방법
 리스트의 첫 번째와 두 번째 요소는 None으로 넣을 것
 리스트의 세 번째 요소(인덱스 2)에는 2의 약수를 리스트
로 구성해서 넣을 것
 리스트의 네 번째 요소(인덱스 3)에는 3의 약수를 리스트
로 구성해서 넣을 것
 …
 리스트의 101번째 요소(인덱스 100)에는 100의 약수를 리
스트로 구성해서 넣을 것)
 리스트 구성 예: [None, None, [1, 2], [1, 3], [1, 2, 4], … ]
 2~100사이의 정수 한 개를 입력으로 전달 받고 약
수 리스트를 구성해서 반환하는 함수 구현
 2~100의 약수 리스트를 다시 리스트로 구성해서 반
환하는 함수 구현
 이 함수에서 0과 1번 인덱스 요소에 None을 넣을 것
 2~100의 약수 리스트를 화면에 출력하는 함수 작성
 앞에서 만들어진 함수들을 구현하고 사용하는
main() 함수를 구현하고 이를 이용해서 전체 프로그
램 실행
'''


def getone(B):
    C = [None, None]
    for i in range(1, B + 1):
        if B % i == 0:
            C.append(i)
    return C


def getonetoall():
    A = [None, None]
    for i in range(2, 101):
        B = []
        for y in range(1, i + 1):
            if i % y == 0:
                B.append(y)
        A.append(B)
    return A


def printall(A):
    print(A)


def main():
    a = int(input("약수를 구하고 싶은 정수를 입력하세요: "))
    print(getone(a))
    printall(getonetoall())


main()
