def primo(numero):
    if numero == 0 or numero == 1 or numero == 4:
        return False 
    for x in range(2, int(numero/2)):
        return False
    return True
for numero in range(1001):
    if primo(numero):
        print(numero, end=",")
