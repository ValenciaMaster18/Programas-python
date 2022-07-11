

from random import triangular


class Triangulo():
    def __init__(self):
        pass
        
    
    def calcularArea(self,base,altura):
        self.base = base
        self.altura = altura 
        self.area = (self.base * self.altura) / 2
        
        return "Area: " + str(self.area)
    
    
    def calcularPerimetro(self,lados):
        self.lados = lados
        self.perimetro =  self.lados * 3
        return "Perimetro: " + str(self.perimetro)
    
    
    
if __name__ == "__main__":
    triangulo = Triangulo()
    print(triangulo.calcularArea(5,10))
    print(triangulo .calcularPerimetro(5))