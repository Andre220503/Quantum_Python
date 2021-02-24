class coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x) ** 2
        y_diff = (self.y - otra_coordenada.y) ** 2

        distancia = (x_diff + y_diff) ** 0.5
        return distancia

coord_1 = coordenada(3, 30)
coord_2 = coordenada(4, 8)

print(coord_1.distancia(coord_2))
print(coord_2.distancia(coord_1))

