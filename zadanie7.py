import datetime

kolokwium = datetime.date(2025, 12, 18)
ile_zostalo_czasu = kolokwium - datetime.date.today()
ile_zostalo_dni = ile_zostalo_czasu.days
print(f"Do kolokwium pozostało {ile_zostalo_dni} dni")

laboratorium = datetime.date(2025, 11, 25)
ile_minelo_czasu = datetime.date.today() - laboratorium
ile_minelo_dni = ile_minelo_czasu.days
print(f"Od ostatniego laboratorium minęło {ile_minelo_dni} dni")