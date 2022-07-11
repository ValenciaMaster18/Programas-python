class Figura:
    
    def __init__(self,area,perimetro):
        self.area = area
        self.perimetro = perimetro
        
    
    # def __str__(self):
    #     return "Area: " + str(self.area) + "cm²" + "  " + "Perimetro: " + str(self.perimetro) + "cm"

    

if __name__ == "__main__":
    figura = Figura(25.5,6)
    print(figura)