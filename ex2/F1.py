Laps = 45
FuelPerLap = 2.25
FuelRequirement = Laps*FuelPerLap
print("minimum fuel requirement is: ",FuelRequirement)
Fuel = FuelRequirement * 1.5
print("Full fuel load: ",Fuel)


QLapTime = 80.45
TLapTime = QLapTime - ((0.35/10) * 5)
NLapTime = TLapTime + ((0.35/10) * Fuel)
print("Theoretical lap time is: ", TLapTime)
print("old lap time is: ", QLapTime)
print("first lap time is: ", NLapTime)

