is_birthday = bool(input("É seu aniversário?: "))
speed = int(input("Velocidade máxima: "))

if is_birthday == True:
    if speed <= 65:
        print("Sem multa") 
    elif speed <= 85:
        print("Multa leve") 
    else:
        print("Multa grande")
else:
    if speed <= 60:
        print("Sem multa") 
    elif speed <= 80:
        print("Multa leve") 
    else:
        print("Multa grande")