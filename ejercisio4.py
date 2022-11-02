#Hay solo 3 numeros perfectos inferiores a 1000
for i in range(1,1001):
    sum = 0
    for j in range(1,i):
        if i%j == 0:
            sum += j
        if sum == i:
            print(i)