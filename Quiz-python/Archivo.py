def archivo(categoria,puntaje):
    with open("./archivo/datos.txt", "a", encoding="utf-8") as f:
        name = input("Digite su nombre: ").capitalize()
        edad = int(input("Digite su edad: "))
        datos1 = [{"Categoria":categoria,"Nombre":name,"Edad":edad,"Calificacion":puntaje}]
        f.write(str(datos1))
        f.write("\n")
    return str(datos1)