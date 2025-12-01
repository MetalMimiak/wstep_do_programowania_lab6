import random

print("A.")
liczba_min = 1
liczba_max = 100
szczesliwa_liczba = random.randint(liczba_min, liczba_max)
print(f"Twoja szczęśliwa liczba to: {szczesliwa_liczba}")

print("B.")
roczniki = [1997, 2000, 2001, 2003, 2004, 2005, 2007, 2008]
szczesliwy_rocznik = random.choice(roczniki)
print(f"Szczęśliwy rocznik to: {szczesliwy_rocznik}")