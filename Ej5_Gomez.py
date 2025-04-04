import random
'''Escribe 5 strings con frases que describan su experiencia durante el desarrollo de la asignatura.

Incluye estas frases en una lista.

Genera el código necesario, para que cada vez que se ejecute el código, muestre una frase aleatoria de esa lista.'''

def generador_frases():
    
    frases = ["Me ha parecido muy entretenido", "Veo mucho potencial de uso con este lenguaje", "Tengo que replicar el Rally-x con Pygame","La asignatura debería durar todo el curso", "Me cuesta pensar en Python sin música"]
    frase_elegida = random.choice(frases)
    print(f"La frase elegida es '{frase_elegida}'")
    
generador_frases()