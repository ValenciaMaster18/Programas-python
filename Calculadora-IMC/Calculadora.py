from Clasificacion import clasificacion
from Evaluacion import evaluacion



def main():
    
    IMC = evaluacion()
    print(IMC)
    clasificacion(IMC)


    
if __name__ == "__main__":
    main() 
    