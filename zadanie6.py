import time

sekundy = int(input("Podaj liczbę sekund: "))

for sekunda in range(sekundy, 0, -1):
    print(f"Pozostało sekund: {sekunda}")
    time.sleep(1)
print("Koniec odliczania")