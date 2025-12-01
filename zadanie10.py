import random
import math

granica_dolna = int(input("Podaj dolną granicę przedziału: "))
granica_gorna = int(input("Podaj górną granicę przedziału: "))

krotka = tuple(random.randint(granica_dolna, granica_gorna) for _ in range(10))
print(f"Krotka: {krotka}")
iloczyn = math.prod(krotka)
sr_geometryczna = iloczyn ** (1 / 10)
print(f"Iloczyn: {iloczyn}")
print(f"Średnia geometryczna [jako pierwiastek 10 stopnia]: {sr_geometryczna:.4f}")