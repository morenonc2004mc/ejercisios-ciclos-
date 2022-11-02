def numeroperfecto(num):
    suma = 0
    for i in range(1,num):
        if (num % (i) == 0  ):
            suma += (i)
    if num == suma:
        return True
    else:
        return False
num = int(input("Introduzca un numero: "))
if numeroperfecto(num):
    print("%s es un numero perfecto" % num)
else:
    print("%s No es un numero perfecto" % num)         