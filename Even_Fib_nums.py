def fib(num):
    num1 = 0
    num2 = 1
    res = num1 + num2
    while res < num:
      num1 = num2 
      num2 = res
      res = num1 + num2
    if res == num:
      return True
    else:
      return False
    
def evalFibsum(n):
  sum = 0
  for num in range(n):
    if fib(num) and (num % 2 == 0):
      sum += num
  return sum

print(evalFibsum(50))
