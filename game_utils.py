 # Präsentiert ein Rätsel und prüft die Eingabe des Spielers
def solve_riddle(riddle):
    print(riddle['question'])
    answer = input("Deine Antwort: ").lower().strip()

    if answer == riddle['answer'].lower().strip():
        print("Rätsel gelöst. Gut gemacht!")
        return True
    else:
        print("Falsche Antwort. Probier es nochmal!")
        return False


# Verabschiedet sich und endet das Spiel
def end_game():
    print("The end. Danke fürs Spielen!")