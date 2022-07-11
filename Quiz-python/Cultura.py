from Archivo import archivo

def cultura():
    print("""
Quiz de Cultura General        
   _____ _    _ _   _______ _    _ _____               _____ ______ _   _ ______ _____            _      
  / ____| |  | | | |__   __| |  | |  __ \     /\      / ____|  ____| \ | |  ____|  __ \     /\   | |     
 | |    | |  | | |    | |  | |  | | |__) |   /  \    | |  __| |__  |  \| | |__  | |__) |   /  \  | |     
 | |    | |  | | |    | |  | |  | |  _  /   / /\ \   | | |_ |  __| | . ` |  __| |  _  /   / /\ \ | |     
 | |____| |__| | |____| |  | |__| | | \ \  / ____ \  | |__| | |____| |\  | |____| | \ \  / ____ \| |____ 
  \_____|\____/|______|_|   \____/|_|  \_\/_/    \_\  \_____|______|_| \_|______|_|  \_\/_/    \_\______|
                                                                                                                   
Buena suerte          """)
    puntaje = 0
    pregunta = input("""
1)¿Cuàl es el paìs màs grande del mundo?
    A) EEUU
    B) China
    C) Rusia
Respuesta: """).upper()
    if pregunta == "C":
        puntaje += 20
        print("Respuesta correcta 'Rusia' con '17 Kilometros cuadrados'")
    else:
        print("La respuesta era la C")

    pregunta = input("""
2)¿Entre què años se desarrollò la segunda guerra mundial?
    A) 1914 - 1919
    B) 1929 - 1935
    C) 1939 - 1945
Respuesta: """).upper()
    if pregunta == "C":
        puntaje += 20
        print("Respuesta correcta '1939-1945' aproximadamente duro '5 Años'")
    else:
        print("La respuesta era la C")

    pregunta = input("""
3)¿Cuàndo llegò Cristòbal Colòn por primera vez Amèrica?
    A) 09 de agosto de 1925
    B) 12 de octubre de 1492
    C) 15 de octubre de 1542
Respuesta: """).upper()
    if pregunta == "B":
        puntaje += 20
        print("Respuesta correcta '12 de octubre de 1492'")
    else:
        print("La respuesta era la B")
        
    pregunta = input("""
4)¿Cuàl es el metal mas caro del mundo?
    A) Oro
    B) Platino
    C) Rodio
Respuesta: """).upper()
    if pregunta == "C":
        puntaje += 20
        print("Respuesta correcta 'Rodio' Actualmente tiene un valor de 28.250 dolares por 'onza'")
    else:
        print("La respuesta era la C")
        
    pregunta = input("""
5)¿En què año llego el ser humano a la luna?
    A) 1969
    B) 1999
    C) 1934
Respuesta: """).upper()
    if pregunta == "A":
        puntaje += 20
        print("Respuesta correcta '1969' en la Mision del 'Apolo 11 de la NASA'")
    else:
        print("La respuesta era la A")
        
        
    base = archivo("Cultura",puntaje)
    
    return base, pregunta, print(f"Tu puntaje fue de {puntaje} puntos") 


if __name__ == "__main__":
    cultura()