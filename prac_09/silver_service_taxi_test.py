

from silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi("Hummer", 200, 4)
print(hummer)

audi = SilverServiceTaxi("Audi", 100, 2)
audi.drive(18)
assert audi.get_fare() == 48.8
