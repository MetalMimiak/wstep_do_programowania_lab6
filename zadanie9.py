import math
import keyword

print("Funkcje w module 'math':")
print([item for item in dir(math) if not item.startswith("_")])

print("\nFunkcje w module 'keyword'")
print([item for item in dir(keyword) if not item.startswith("_")])

print("\nFunkcje dostępne dla typu 'tuple':")
print([item for item in dir(tuple) if not item.startswith("_")])