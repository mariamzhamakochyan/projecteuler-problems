squares_sum = 0
sum_of_nums = 0
for i in range(1, 101):
    sum_of_nums += i
    squares_sum += i ** 2
sum_of_nums **= 2
print(sum_of_nums - squares_sum)

 
