num = 0 
while True:
    num += 20
    num_mult = 0
    for i in range(20,10,-1):
        if num % i == 0:
            num_mult += 1
        else:
            break
    if num_mult == 10:
        break
    if num % 1000000 == 0:
        print(num / 1000000)
print(num)
