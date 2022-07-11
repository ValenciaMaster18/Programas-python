from Figura import Figura

class Cuadrado(Figura):
    
    def __init__(self, area, perimetro):
        self.lados = 0
        super().__init__(area, perimetro)
        
     
    def __str__(self):
        return str(self.calcularArea()) +" "+ str(self.calcularPerimetro())     
        
        
    def calcularArea(self):
        return "Area: " + str(self.area**2) + "cm²"
    
    
    def calcularPerimetro(self):
        return "Perimetro: " + str(self.perimetro * 4) + "cm"
    
if __name__ == "__main__":
    cuadrado = Cuadrado(2,6)
    print(cuadrado)
    print(cuadrado.calcularArea())
    print(cuadrado.calcularPerimetro())