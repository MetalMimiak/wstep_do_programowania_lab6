import random

liczby = list(range(1, 50))
ilosc_kul_wylosowanych = 6
wylosowane_liczby = random.sample(liczby, ilosc_kul_wylosowanych)
wylosowane_liczby.sort()

print(f"Wylosowane liczby: {wylosowane_liczby}")