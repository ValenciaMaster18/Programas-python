from Datos import datos

def clasificacion(salud):
    if salud < 16.00:
        print("Delgadez severa")
    elif salud >= 16.00  and salud <= 16.99: 
        estado = "Delgadez moderada"
    elif salud >= 17.00 and salud <=18.49:
        estado = "Delgadez aceptable"
    elif salud >= 18.50 and salud <= 24.99:
        estado = "Normal"
    elif salud >= 25.00 and salud <= 29.99:
        estado ="Pre-obeso(riesgo)"
    elif salud >= 30.00 and salud <= 34.99:
        estado = "Obeso tipo | (riesgo moderado)"
    elif salud >= 35.00 and salud <= 39.99:
        estado ="Obeso tipo || (riesgo severo)"
    elif salud >= 40.00:
        estado ="Obeso tipo ||| (riesgo muy severo)"
    else:
        print("!!!")
    
    return datos(estado)

if __name__ == "__main__":
    clasificacion() 