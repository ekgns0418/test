num = int(input("숫자를 입력하세요 : "))
arr = [[0] * num for i in range(num)]

number = 0
one = 1
row = -1
column = 0

def snail(number, one, row, column, num):
    for i in range(0, num):
        number += 1
        row += one
        arr[column][row] = number
    num -= 1
    for i in range(1, num+1):
        number += 1
        column += one
        arr[column][row] = number
    one *= -1
    if num == 0:
        return 0
    
    snail(number, one, row, column, num)

snail(number, one, row, column, num)
for column in range(num):
    print(arr[column])
