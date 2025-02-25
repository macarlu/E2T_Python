#tres opciones, una aleatoria gana, jugador elege 1 caja aleatoria, presentador abre 1, no la escogidfa , no la premiada, aleatoriamente jugador cambia o no cambia.Gana o no
#gana con cambio x%, gana sin cambio x%,pierde con cambio x%,pierde sin cambio x%

import random
'''
class Concurso:
    caja1 = 1
    caja2 = 2
    caja3 = 3

    def __init__(self):
        pass

    def repartir(self,reparte):
        self.reparte = reparte
        reparte = random.randint(1,3)
    
    def eligecaja(self,caja):
        self.caja = caja
        caja = random.randint(1,3)
    
    def abrecaja(self,abrir):
        self.abrir = abrir
        abrir = random.randint(1,3)
        if abrir 
'''

class Concurso:
    puertas=[1,2,3]
    gana_sin_ch = 0
    gana_con_ch = 0
    pierde_sin_ch = 0
    pierde_con_ch = 0
    interacciones = 0

    def __init__(self):
        pass
    
    def concursar(self,iteracciones):
        self.iteracciones = iteracciones

        for i in range(0,iteracciones):
            self.puertas = [1,2,3]
            eleccion_jugador = random.choice(self.puertas)
            puerta_premio = random.choice(self.puertas)

            if eleccion_jugador == puerta_premio:
                fase_final = []
                fase_final.append(eleccion_jugador)
                self.puertas.remove(eleccion_jugador)
                fase_final.append(random.choice(self.puertas))
            
            else:
                fase_final = []
                fase_final.append(eleccion_jugador)
                fase_final.append(puerta_premio)

            cambio = random.randint(0,1)

            if cambio == 0:
                if eleccion_jugador == puerta_premio:
                    self.gana_sin_ch += 1
                else:
                    self.pierde_sin_ch += 1

            else:
                if eleccion_jugador != puerta_premio:
                    self.gana_con_ch += 1
                else:
                    self.pierde_con_ch += 1
    
    def imprimir_resultados(self):
        print(f"Cambiando la caja del jugador ha: \n -Ganado el {(self.gana_con_ch/self.interacciones)*100}% de las veces. -Perdido el {(self.pierde_con_ch/self.interacciones)*100}% de las veces.")
        print(f"Manteniendo la caja del jugador ha: \n -Ganado el {(self.gana_sin_ch/self.interacciones)*100}% de las veces. -Perdido el {(self.pierde_sin_ch/self.interacciones)*100}% de las veces.")
        
    
concurso1 = Concurso()
concurso1.concursar(100)
concurso1.imprimir_resultados()


        