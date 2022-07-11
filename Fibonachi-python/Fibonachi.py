def fibonachi():
    pares = []
    impares = []
    
    a = 0
    b = 1
    contenedor = 0
    for _ in range(10):
        print(contenedor,end=" ")
        contenedor = a + b
        b = a
        a = contenedor      
        if contenedor%2 != 0:
            impares.append(contenedor)
        else:
            pares.append(contenedor)
    print()
    lista = [{"Pares":pares,"Impares":impares}]
            
    return print(lista)    


def run():
    fibonachi()


if __name__ == "__main__":
    run()