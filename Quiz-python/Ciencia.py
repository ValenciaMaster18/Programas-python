from Archivo import archivo 

def ciencia(): 
    print("""
Quiz de Ciencia        
   _____ _____ ______ _   _  _____ _____          
  / ____|_   _|  ____| \ | |/ ____|_   _|   /\    
 | |      | | | |__  |  \| | |      | |    /  \   
 | |      | | |  __| | . ` | |      | |   / /\ \  
 | |____ _| |_| |____| |\  | |____ _| |_ / ____ \ 
  \_____|_____|______|_| \_|\_____|_____/_/    \_ 
                                                            
Buena suerte          """)
    puntaje = 0
    pregunta = input("""
1)¿Cuàl es la fòrmula molecular del agua?
    A) H2
    B) O2
    C) H2O
Respuesta: """).upper()
    if pregunta == "C":
        puntaje += 20
        print("Respuesta correcta 'H2O'")
    else:
        print("La respuesta era la C")

    pregunta = input("""
2)¿Còmo se llama la capa màs externa de nuestro planeta?
    A) Hidròsfera
    B) Atmòsfera
    C) Litòsfera
Respuesta: """).upper()
    if pregunta == "B":
        puntaje += 20
        print("Respuesta correcta 'Atmòsfera'")
    else:
        print("La respuesta era la B")

    pregunta = input("""
3)¿Cuànto tarda la tierra en dar una vuelta al sol?
    A) 24 horas
    B) 30 dìas
    C) 365 dìas
Respuesta: """).upper()
    if pregunta == "C":
        puntaje += 20
        print("Respuesta correcta '365 dias'")
    else:
        print("La respuesta era la C")
        
    pregunta = input("""
4)¿Cuàntos dientes tiene la dentadura completa de un adulto?
    A) 32
    B) 28
    C) 26
Respuesta: """).upper()
    if pregunta == "A":
        puntaje += 20
        print("Respuesta correcta '32 Dientes'")
    else:
        print("La respuesta era la A")
        
    pregunta = input("""
5)¿Cuàntos corazones tiene un pulpo?
    A) 3
    B) 2
    C) 1
Respuesta: """).upper()
    if pregunta == "A":
        puntaje += 20
        print("Respuesta correcta '3 Corazones'")
    else:
        print("La respuesta era la A")
        
        
    base = archivo("Ciencia",puntaje)
    
    return base, pregunta, print(f"Tu puntaje fue de {puntaje} puntos") 


if __name__ == "__main__":
    ciencia()
    