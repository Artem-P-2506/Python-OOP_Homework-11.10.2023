import os
from datetime import datetime
from Tic_Tac_Toe.Cross import *
from Tic_Tac_Toe.Circle import *

class Game():
    def __init__(self):
        self.__arrayTicTacToe = []
        self.__firstPlayerName = "NONE"
        self.__secondPlayerName = "NONE"

    def getFirstPlayerName(self):
        return self.__firstPlayerName

    def getSecondPlayerName(self):
        return self.__secondPlayerName

    def setFirstPlayerName(self, newName):
        self.__firstPlayerName = newName

    def setSecondPlayerName(self, newName):
        self.__secondPlayerName = newName

    def getLogsOfLastGame(self):
        if os.path.exists("gameLOGS.txt"):
            with open("gameLOGS.txt", 'r') as file:
                return file.readlines()
        else:
            return []

    def __makeArray(self, rows, colums):
        for i in range(rows):
            self.__arrayTicTacToe.append([])
            for j in range(colums):
                self.__arrayTicTacToe[i].append(Cell(i, j))

    def __changeCell(self, playerName):
        if playerName == self.__firstPlayerName:
            value = 1
            symbol = "X"
        elif playerName == self.__secondPlayerName:
            value = 2
            symbol = "O"
        else: #Передано несуществующее имя игрока
            value = 0
            symbol = "NONE"

        while(True):
            print(f"\tСейчас ходит игрок '{playerName}' ({symbol})!")
            coorinateX = int(input("Введите X-координату ячейки для хода: "))
            coorinateY = int(input("Введите Y-координату ячейки для хода: "))
            if 0 < coorinateY <= len(self.__arrayTicTacToe) and 0 < coorinateX <= len(self.__arrayTicTacToe):
                if value == 1 and self.__arrayTicTacToe[len(self.__arrayTicTacToe) - coorinateY][coorinateX - 1].getValue() == "_":
                    self.__arrayTicTacToe[len(self.__arrayTicTacToe) - coorinateY][coorinateX - 1] = Cross(coorinateX, coorinateY)
                    break
                elif value == 2 and self.__arrayTicTacToe[len(self.__arrayTicTacToe) - coorinateY][coorinateX - 1].getValue() == "_":
                    self.__arrayTicTacToe[len(self.__arrayTicTacToe) - coorinateY][coorinateX - 1] = Сircle(coorinateX, coorinateY)
                    break
                else:
                    print("Cell is not empty!\n")
                    continue
            else:
                print("Wrong input!\n")
                continue

        with open("gameLOGS.txt", 'a') as file:
            file.write(f"\nPlayer\t'{playerName}' set into cell\t{coorinateX},{coorinateY} symbol\t{symbol}")


    def __showField(self):
        print("\n=> ПОЛЕ:")
        for row in self.__arrayTicTacToe:
            for column in row:
                print("\t", str(column.getValue()), "\t", end="")
            print("\n")

    def __isWin(self, playerName):
        if playerName == self.__firstPlayerName:
            symbol = "X"
        elif playerName == self.__secondPlayerName:
            symbol = "O"
        else:  # Передано несуществующее имя игрока
            symbol = "NONE"

        FieldSize = len(self.__arrayTicTacToe)

        # Проверка столбцов
        for i in range(FieldSize):
            isWin = True
            for j in range(FieldSize):
                if self.__arrayTicTacToe[i][j].getValue() != symbol:
                    isWin = False
                    break
            if isWin:
                return True

        # Проверка рядков
        for j in range(FieldSize):
            isWin = True
            for i in range(FieldSize):
                if self.__arrayTicTacToe[i][j].getValue() != symbol:
                    isWin = False
                    break
            if isWin:
                return True

        # Проверка по главной диагонали
        isWin = True
        for i in range(FieldSize):
            if self.__arrayTicTacToe[i][i].getValue() != symbol:
                isWin = False
                break
        if isWin:
            return True

        # Проверка по второй диагонали
        isWin = True
        for i in range(FieldSize):
            if self.__arrayTicTacToe[i][FieldSize - 1 - i].getValue() != symbol:
                isWin = False
                break
        if isWin:
            return True

        return False

    def startGame(self):
        while(True):
            print("Посмотреть информацию про прошлую игру?")
            showLogsLastGame = input("ДА - '+'  |  НЕТ - '-': ")
            if showLogsLastGame == '+':
                for item in self.getLogsOfLastGame():
                    print(item, end="")
                print("\n")
                break
            elif showLogsLastGame == '-':
                break
            else:
                print("Wrong input!\n")
                continue

        print("Новая игра начата!")
        startTime = datetime.now()
        startTime.strftime("%Y-%m-%d %H:%M:%S")
        self.__firstPlayerName = input("Введите имя первого игрока (CROSS): ")
        self.__secondPlayerName = input("Введите имя второго игрока (CIRCLE): ")
        with open("gameLOGS.txt", 'w') as file:
            file.write(f"Game start time:\t{startTime}" +
                       f"\nFirst player name:\t{str(self.__firstPlayerName)}" +
                       f"\nSecond player name:\t{str(self.__secondPlayerName)}")

        print("3*3 - 1  |  6*6 - 2  |  9*9 - 3")
        choise = int(input("Выберите поле: "))
        if choise == 1:
            rows = 3
            colums = 3
        elif choise == 2:
            rows = 6
            colums = 6
        elif choise == 3:
            rows = 9
            colums = 9
        else:
            print("Wrong input!")
        with open("gameLOGS.txt", 'a') as file:
            file.write(f"\nField size (rows*columns):\t{rows}*{colums}\n")
        self.__makeArray(rows, colums)
        self.__showField()

        while(True):
            # Ходит первый игрок
            self.__changeCell(self.__firstPlayerName)
            self.__showField()
            if self.__isWin(self.__firstPlayerName):
                print(f"=-=-=* Игрок '{self.__firstPlayerName}' победил!!! *=-=-=")
                with open("gameLOGS.txt", 'a') as file:
                    file.write(f"\nWon player:\t'{self.__firstPlayerName}'")
                break

            # Ходит второй игрок
            self.__changeCell(self.__secondPlayerName)
            self.__showField()
            if self.__isWin(self.__secondPlayerName):
                print(f"=-=-=* Игрок '{self.__secondPlayerName}' победил!!! *=-=-=")
                with open("gameLOGS.txt", 'a') as file:
                    file.write(f"\nWon player:\t'{self.__firstPlayerName}'")
                break