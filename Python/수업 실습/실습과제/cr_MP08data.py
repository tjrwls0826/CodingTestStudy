import os

print(os.getcwd())

filename = input("input file name: ")  # �ּ� 1��
try:
    with open(filename, encoding="utf-8") as f:  # �ּ� 2��
        lst = f.readlines()

except FileNotFoundError:
    filename = input("Couldn't find the file, input again")  # �ּ� 3��
