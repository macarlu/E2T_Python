class Militar:
    empleo= ""
    nombre= ""
    edad = int()

    def __init__(self):
       pass

    def saludo(self):
        print("A sus ordenes Buenos dias!")

    def dalenombre(self,name):
        self.nombre=name

    def dimenombre(self):
        print(f"El militar se llama {self.nombre}")

    def daleempleo(self,rank):
        self.empleo= rank

    def dimeempleo(self):
        print(f"Su militar es {self.empleo}")
    
    def daleedad(self,age):
        self.edad = age

    def cumpleaños(self):
        self.edad += 1
    
    def dimeedad(self):
        print(f"El militar tiene {self.edad} años")
    
   
    

militar1= Militar()
militar1.dalenombre("Maverick")
militar1.daleempleo("Capitan de Corneta")
militar1.daleedad(21)
militar1.dimeedad()
militar1.cumpleaños()
militar1.cumpleaños()
militar1.cumpleaños()
militar1.cumpleaños()
militar1.dimeedad()