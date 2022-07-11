class Persona:
    
    def __init__(self,nombre, apellido, dni, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.dni= dni
        self.telefono = telefono
        
        
    def __str__(self):
        return self.nombre +" "+ str(self.dni) +" "+ str(self.telefono)


if __name__ == "__main__":
    persona = Persona("Miguel","Melendez",6845,311548941)
    print(persona)