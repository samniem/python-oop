class Plane:
    vehicle = 'Plane'

    #self is always called so it does not need to be here by necessity
    #self in essence contains the object memory address
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year

AirbusA320 = Plane('Airbus','A320', 1987)
AirbusA318 = Plane('Airbus','A318', 2002)

print("A320 year", AirbusA320.year)
print("vehicle category", Plane.vehicle)
