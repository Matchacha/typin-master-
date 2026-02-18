import random 
import time

def get_words(nivel)
    facil = [
        "instituto", "salchicha", "guanabana", "caracol", "ortopeda", "institucion"
    ]
    medio = [
        "circustancia", "anfitrion", "teatral", "romanticismo", "carambola", "diferenciacion"
    ]
    dificil = [
        "Idiosincrasia", "Otorrinolaringólogo", "Psicopedagogía", "Transterritorialidad", 
    ]

if nivel == "facil": 
    return facil
elif nivel == "medio":
    return medio
else:
    return dificil

def typing_game():
    nivel = input("elige nivel (facil/medio/dificil)")
    words = get_words(nivel)
    random.shuffle(words)
    total_words = len(words)
    mistakes = 0
    
    print("/n Juego de rapidez en escritura lol")
    print("escribe rapidamente la palabra que te aparece abajito ahi")
for i, word in enumerate(words, start=1): ## i es el índice, word es la palabra
    print("Palabra {}/{}: {}".format(i, total_words, word)) # Muestra progreso y palabra actual
