num = int(input("escolha um numero: "))

if num >= 1 and num <= 12:
    if num == 1:
        print("janeiro")
    elif num == 2:
        print("fevereiro")
    elif num == 3:
        print("março")
    elif num == 4:
        print("abriu")
    elif num == 5:
        print("maio")
    elif num == 6:
        print("junho")
    elif num == 7:
        print("julho")
    elif num == 8:
        print("agosto")
    elif num == 9:
        print("setembro")
    elif num == 10:
        print("outubro")
    elif num == 11:
        print("novembro")
    elif num == 12:
        print("dezembro")
else:
    print("valor invalido")