import random
import time

def get_words(nivel):
    facil = [
        "instituto", "salchicha", "guanabana", 
        "caracol", "ortopeda", "institucion"
    ]
    medio = [
        "circustancia", "anfitrion", "teatral", 
        "romanticismo", "carambola", "diferenciacion"
    ]
    dificil = [
        "Idiosincrasia", "Otorrinolaringólogo", 
        "Psicopedagogía", "Transterritorialidad"
    ]
    
    if nivel == "facil": 
        return facil
    elif nivel == "medio":
        return medio
    else:
        return dificil

def typing_game():
    nivel = input("Elige nivel (facil/medio/dificil): ")
    words = get_words(nivel)
    random.shuffle(words)
    total_words = len(words)
    mistakes = 0
    
    print("\nJuego de rapidez en escritura")
    print("Escribe rápidamente la palabra que aparece abajo")
    for i, word in enumerate(words, start=1):
        print("Palabra {}/{}: {}".format(i, total_words, word))
        user_input = input("Escribe la palabra: ") 
        if user_input.strip().lower() == word.lower():
            print("Correcto\n")
        else:
            print("Incorrecto\n")
            mistakes += 1
        time.sleep(1)

    correct = total_words - mistakes
    accuracy = (correct / total_words) * 100

    print("\nFin del juego")
    print("Nivel jugado:", nivel.capitalize())
    print("Palabras totales:", total_words)
    print("Errores cometidos:", mistakes)
    print("Palabras correctas:", correct)
    print("Tu precisión fue de: {:.2f}%".format(accuracy))

    if accuracy == 100: 
        print("No cometiste ningún error")
    elif accuracy >= 70: 
        print("¡Bien! Sigue practicando para mejorar aún más")
    else: 
        print("Ay, qué vergüenza")

if __name__ == "__main__": 
    typing_game()
