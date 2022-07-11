from Archivo import archivo

def colombia(): 
    print("""
Quiz de colombia  
   _____ ____  _      ____  __  __ ____ _____          
  / ____/ __ \| |    / __ \|  \/  |  _ \_   _|   /\    
 | |   | |  | | |   | |  | | \  / | |_) || |    /  \   
 | |   | |  | | |   | |  | | |\/| |  _ < | |   / /\ \  
 | |___| |__| | |___| |__| | |  | | |_) || |_ / ____ \ 
  \_____\____/|______\____/|_|  |_|____/_____/_/    \_ 
                                                          
Buena suerte        """)
    puntaje = 0
    pregunta = input("""
1)¿Colombia se encuentra en?
    A) Centro America
    B) Amèrica del Sur
    C) Amèrica del Norte
Respuesta: """).upper()
    if pregunta == "B":
        puntaje += 20
        print("Respuesta correcta 'America del sur' es el unico pais que tiene costa con el oceano Atlantio, Pacifico")
    else:
        print("La respuesta era la B")

    pregunta = input("""
2)¿La flor emblematica de colombia es?
    A) Heliconia
    B) Orquidea
    C) Rosa
Respuesta: """).upper()
    if pregunta == "B":
        puntaje += 20
        print("Respuesta correcta 'Orquidea' Se encuentra en el 'Alto magdalena y huila'")
    else:
        print("La respuesta era la B")

    pregunta = input("""
3)¿Què cordillera atraviesa colombia?
    A) El Himaya
    B) Los Alpes
    C) Los Andes
Respuesta: """).upper()
    if pregunta == "C":
        puntaje += 20
        print("Respuesta correcta 'Los andes'")
    else:
        print("La respuesta era la C")
        
    pregunta = input("""
4)¿En què hemisferio està situado Colombia?
    A) Hemisferio norte
    B) En los 2 Hemisferios
    C) Hemisferio Sur
Respuesta: """).upper()
    if pregunta == "B":
        puntaje += 20
        print("Respuesta correcta 'En los 2 hemisferios sur y norte'")
    else:
        print("La respuesta era la B")
        
    pregunta = input("""
5)¿La moneda de colombia es?
    A) Peso Colombiano
    B) Real Colombiano
    C) Dolar
Respuesta: """).upper()
    if pregunta == "A":
        puntaje += 20
        print("Respuesta correcta 'Peso Colombiano'")
    else:
        print("La respuesta era la A")
        
        
    base = archivo("Colombia",puntaje)
    
    return base, pregunta, print(f"Tu puntaje fue de {puntaje} puntos") 


if __name__ == "__main__":
    colombia()