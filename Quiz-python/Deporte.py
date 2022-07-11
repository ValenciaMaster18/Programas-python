from Archivo import archivo

def deporte():
    print("""
Quiz de Deportes
  _____  ______ _____   ____  _____ _______ ______ 
 |  __ \|  ____|  __ \ / __ \|  __ \__   __|  ____|
 | |  | | |__  | |__) | |  | | |__) | | |  | |__   
 | |  | |  __| |  ___/| |  | |  _  /  | |  |  __|  
 | |__| | |____| |    | |__| | | \ \  | |  | |____ 
 |_____/|______|_|     \____/|_|  \_\ |_|  |______|
                                                             
Buena suerte          """)
    
    puntaje = 0
    pregunta = input("""
1)¿Cuàl es el jugador con mas titulos en la historia del futbol?
    A) Leonel Messi
    B) Dani Alvez
    C) Cristiano Ronaldo
Respuesta: """).upper()
    if pregunta == "B":
        puntaje += 20
        print("Respuesta correcta 'Dani alvez'  es el maximo ganador con '42 titulos'")
    else:
        print("La respuesta era la B")

    pregunta = input("""
2)¿Cuàl es el tenista con mas titulos de Grand Slam?
    A) Rafael Nadal
    B) Novak Djokovic
    C) Roger Federer
Respuesta: """).upper()
    if pregunta == "A":
        puntaje += 20
        print("Respuesta correcta 'Rafael nadal' es el maximo ganador con '22 Grand Slam'")
    else:
        print("La respuesta era la A")

    pregunta = input("""
3)¿Què selecciòn a ganado mas mundiales?
    A) Italia
    B) Alemania
    C) Brazil      
Respuesta: """).upper()
    if pregunta == "C":
        puntaje += 20
        print("Respuesta correcta 'Brazil' es el maximo ganador con '5 Copas del Mundo'")
    else:
        print("La respuesta era la C")
        
    pregunta = input("""
4)¿Cuàl es el equipo de NBA con mas titulos?
    A) Boston Celtic
    B) Golden Warrior
    C) Chicago Bulls
Respuesta: """).upper()
    if pregunta == "A":
        puntaje += 20
        print("Respuesta correcta 'Boston Celtic' actualmente es maximo ganador al igual que Los angeles lakers con '17 titulos'")
    else:
        print("La respuesta era la A")
        
    pregunta = input("""
5)¿Cual es el maximo goleador del futbol?
    A) Pele
    B) Cristiano Ronaldo
    C) Josef Bican
Respuesta: """).upper()
    if pregunta == "B":
        puntaje += 20
        print("Respuesta correcta 'Cristiano Ronaldo' actualmente cuenta con '815 Goles'")
    else:
        print("La respuesta era la B")
    
    
    base = archivo("Deporte",puntaje)
    
    return base, pregunta, print(f"Tu puntaje fue de {puntaje} puntos") 


if __name__ == "__main__":
    deporte()