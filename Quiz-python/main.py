from Deporte import deporte
from Ciencia import ciencia
from Cultura import cultura
from Colombia import colombia

 
def Categoria():    
    categoria = input("""
Seleccione una categoria
          
    1) Deporte
    2) Cultura General
    3) Ciencia
    4) Colombia
""")
    return categoria


def run():
    print("""
  ____ _____ ______ _   ___      ________ _   _ _____ _____   ____  
 |  _ \_   _|  ____| \ | \ \    / /  ____| \ | |_   _|  __ \ / __ \ 
 | |_) || | | |__  |  \| |\ \  / /| |__  |  \| | | | | |  | | |  | |
 |  _ < | | |  __| | . ` | \ \/ / |  __| | . ` | | | | |  | | |  | |
 | |_) || |_| |____| |\  |  \  /  | |____| |\  |_| |_| |__| | |__| |
 |____/_____|______|_| \_|   \/   |______|_| \_|_____|_____/ \____/ 
                                                                                                                            
        """)
    pregunta = input("Presione 'X' y en 'ENTER' para empezar: ").upper()
    if pregunta == "X":
        categoria = Categoria()
        if categoria == "1":
            deporte()
        elif categoria == "2":
            cultura()
        elif categoria == "3":
            ciencia()
        elif categoria == "4":
            colombia()
        else: 
            print("Esta opcion no exite en el menù de categorias")
    else:
        print("Salistes del Quiz")
    
    print()
    print("Programa desarrollado: Luis Valencia")
    
    
if __name__ == "__main__":
    run()
