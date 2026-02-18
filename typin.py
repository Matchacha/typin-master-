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
    