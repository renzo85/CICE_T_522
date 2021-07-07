class Mun:
    def __init__(self, ine_code, sup_km2, den_km2): #self hace referencia a la instancia o ejemplo que estamos refiriendonos
        self.ine_code = ine_code #clave valor
        self.sup_km2 = sup_km2
        self.den_km2 = den_km2

    def population(self):
        return self.sup_km2 * self.den_km2


municipio_1 = {
  "codigo_ine": "280006",
  "sup_km2": 5,
  "den_km2": 3.72
}

municipio_2 = {
  "codigo_ine": "280007",
  "sup_km2": 3,
  "den_km2": 5.72
}

obj_municipio_1 = Mun("28006", 5 , 3.72) #una instancia perfecta
obj_municipio_2 = Mun("28006", 4 , 10)
print(obj_municipio_1.population())
print(obj_municipio_2.population())
print(obj_municipio_1.den_km2, obj_municipio_1.sup_km2)


