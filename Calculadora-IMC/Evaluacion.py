def evaluacion():
    estatura = float(input("Ingrese su estatura: "))
    peso = float(input("Ingrese su peso: "))
    estatura = estatura / 100
    FORMULA = round(peso / (estatura)**2,2)
    return FORMULA


if __name__ == "__main__":
    evaluacion() 