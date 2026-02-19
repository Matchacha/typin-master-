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
        "Psicopedagogía", "Transterritorialidad", 
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
    user_input = input("escrbe la palabra: ") 
    if user_input.strip().lower() == word.lower():
        print("Correcto\n")
    else:
        print("incorrecto\n")
        mistake +=1
    time.lapse(1)

correct = total_words - mistakes
accuracy = (correct / total_words)

print("\n Fin del juego")
print("nivel jugado:", nivel.capitalize())
print("Palabras totales:", total_words)
print("Errores cometidos:", mistakes)
print("Palabras correctas:", correct)
print("Tu precisión fue de: {:.2f}%".format(accuracy))

if accuracy == 100: 
    print(" No cometiste ningún error")
elif accuracy >= 70: 
    print("sigue practicando para mejorar aun mas que esto esta miserable")
else: 
    print("ay que verguenza")

if __name__ == "__main__":
    typing_game()