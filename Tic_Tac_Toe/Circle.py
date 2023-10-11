from Tic_Tac_Toe.Cell import *

class Сircle(Cell):
    def __init__(self, coorinateX, coorinateY):
        super().__init__(coorinateX, coorinateY)
        self._value = "O"