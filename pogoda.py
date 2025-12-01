import temperatura

celsius_1 = 21
fahrenheit_wynik = temperatura.c_to_f(celsius_1)
print(f"{celsius_1}°C to {fahrenheit_wynik}°F")

fahrenheit_1 = 89
celsius_wynik = temperatura.f_to_c(fahrenheit_1)
print(f"{fahrenheit_1}°F to {celsius_wynik}°C")

celsius_2 = 35
kelwin_wynik = temperatura.c_to_k(celsius_2)
print(f"{celsius_2}°C to {kelwin_wynik}K")