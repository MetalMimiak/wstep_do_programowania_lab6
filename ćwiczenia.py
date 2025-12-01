import f_mat

print("A.")

wynik_kwadrat_a = f_mat.kwadrat(10)
print(f"Kwadrat liczby 10: {wynik_kwadrat_a}")

wynik_szescian_a = f_mat.szescian(3)
print(f"Sześcian liczby 3: {wynik_szescian_a}")

wynik_dodaj_a = f_mat.dodaj(10, 5)
print(f"Suma liczb 10 i 5: {wynik_dodaj_a}")

print("B.")

from f_mat import kwadrat
wynik_kwadrat_b = kwadrat(10)
print(f"Kwadrat liczby 10: {wynik_kwadrat_b}")

from f_mat import szescian
wynik_szescian_b = szescian(3)
print(f"Sześcian liczby 3: {wynik_szescian_b}")

from f_mat import dodaj
wynik_dodaj_b = dodaj(10, 5)
print(f"Suma liczb 10 i 5: {wynik_dodaj_b}")