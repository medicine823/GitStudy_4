import re

file = open("./IDcode_unmasked.txt", 'w')
print("ex. 김원호 990624-1234567")
print("성함과 주민등록번호를 입력하세요: ")

while True:
    string = input()
    if string.lower() == 'mask':
        break
    file.write(string + '\n')

file = open("./IDcode_unmasked.txt", 'r')
data = file.read()
pattern = re.compile("([0-9]{6})-[0-9]{7}")
data1 = (pattern.sub("\g<1>-*******", data))
print(data1)

file = open("./IDcode_masked.txt", 'w')
file.write(data1)

file.close()