class Cell():
    def __init__(self, coorinateX, coorinateY):
        self._CoorinateX = coorinateX
        self._CoorinateY = coorinateY
        self._value = "_"

    def getCoorinateX(self):
        return self._CoorinateX

    def getCoorinateY(self):
        return self._CoorinateY

    def getValue(self):
        return self._value

    def setCoorinateX(self, newCoordinateX):
        self._CoorinateX = newCoordinateX

    def setCoorinateY(self, newCoordinateY):
        self._CoorinateY = newCoordinateY