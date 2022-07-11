def datos(salud):
    with open("./Calculadora-IMC/archivo/dato.txt", "a") as f:
        nombre = input("Nombre del usuario: ").capitalize()
        edad = int(input("Edad del usuario: "))
        base = [{"Nombre":nombre,"Edad":edad,"estado":salud}]
        f.write(str(base))
        f.write("\n")
    return print(str(base))





