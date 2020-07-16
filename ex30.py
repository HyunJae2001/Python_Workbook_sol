PoundsPerSquareInch = 6895
MillimetersOfMercury = 133
Atmospheres = 101325

pressure = float(input('Enter the pressure in kilo-pascals: '))

poundspersquareinch = pressure / PoundsPerSquareInch
millimetersofmecury = pressure / MillimetersOfMercury
atmospheres = pressure / Atmospheres

print(f'The {pressure} kilo-pascals is {poundspersquareinch} pounds per square inch and {millimetersofmecury} millimeters of mercury and {atmospheres} atmospheres')