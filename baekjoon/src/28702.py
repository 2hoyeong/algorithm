n = 0
for i in range(3, 0, -1):
    num = input()
    if num.isdigit():
        n = int(num) + i

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
