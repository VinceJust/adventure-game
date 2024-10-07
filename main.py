# Importierung von Variablen von game_utils.py
from game_utils import solve_riddle, end_game

# Begrüßt den Spieler und erklärt die Spielregeln
def greeting():
    print("Willkommen bei der verlorenen Schatzsuche!")
    print("Dein Ziel ist es, den Schatz zu finden, indem du durch verschiedene Räume navigierst und Rätsel löst.")
    print("Du kannst dich bewegen, indem du 'north', 'south', 'east' oder 'west' eingibst.")
    print("Viel Glück!")

# Beschreibt den aktuellen Raum und die verfügbaren Aktionen
def enter_room(room):
    print(f"\nDu betrittst den Raum: {room['name']}.")
    print(room['description'])

# main Funktion
def main():
    greeting()

    # Räume und Rätsel definieren
    rooms = {
        'entrance': {  # Der erste Raum. Der Spieler startet hier.
            'name': 'Eingangshalle',
            'description': 'Eine große Halle mit einer Tür im Norden.',
            'riddle': {
                'question': 'Welche Zutat ist umstritten für eine Pizza?',
                'answer': 'Ananas'
            },
            'north': 'library'
        },
        'library': {  # Raum, wenn der Spieler nach Norden geht.
            'name': 'Bibliothek',
            'description': 'Ein Raum voller alter Bücher. Es gibt eine Tür im Osten.',
            'riddle': {
                'question': 'Was ist ein Krabbelvieh aber kein Insekt?',
                'answer': 'Spinne'
            },
            'east': 'treasure_room'
        },
        'treasure_room': {  # Raum, wenn der Spieler nach Osten geht. Dies kann er erst tun, wenn er in der library ist.
            'name': 'Schatzkammer',
            'description': 'Du siehst eine Schatztruhe, die in der Mitte des Raumes glitzert.',
            'riddle': {
                'question': 'Was ist sowohl überflüssig als auch lebensnotwendig?.',
                'answer': 'Wasser'
            }
        }
    }

    current_room = 'entrance'

    while True:
        room = rooms[current_room]
        enter_room(room)

        if solve_riddle(room['riddle']):
            if current_room == 'treasure_room':
                print("Herzlichen Glückwunsch! Du hast den Schatz gefunden!")
                break

            # Verarbeitung der Richtungseingabe
            direction = input("In welche Richtung möchtest du gehen? (north, east, south, west): ").lower().strip()
            if direction in room:
                next_room = room[direction]
                if next_room:
                    current_room = next_room
                else:
                    print("Du kannst in diese Richtung nicht weitergehen.")
            else:
                print("Ungültige Richtung.")
        else:
            print("Du musst das Rätsel lösen, um weiterzukommen.")

    end_game()

if __name__ == "__main__":
    main()















