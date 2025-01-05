import math

while True:
    num = input()
    if num == '0':
        break
    nl = len(num)
    if nl == 1:
        print('yes')
    else:
        front, back = num[:nl // 2], num[math.ceil(nl / 2):]
        reverse_back = ''.join(list(reversed(back)))

        if front == reverse_back:
            print('yes')
        else:
            print('no')
