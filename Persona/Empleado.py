from Persona import Persona

class Empleado(Persona):
    def __init__(self,nombre, apellido, dni, telefono,salario):
        super().__init__(nombre, apellido, dni, telefono)
        self.salario = salario
        
        
if __name__ == "__main__":
    empleado = Empleado("Luis","Valencia",12345,3226480213,5000000)
    print(empleado)