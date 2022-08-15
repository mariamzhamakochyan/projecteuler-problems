num1 = 0
num2 = 1
sum = 0
while True:
      num1, num2 = num2, num1 + num2
      if num2 >= 4000000:
         break
      if  num2 % 2 == 0:
         sum += num2
print(sum)

