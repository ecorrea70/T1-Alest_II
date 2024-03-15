filename = "casos-de-teste/casoD50.txt"
initial_char = "-"
currentX = 0
currentY = 0
counter = 0

from enum import Enum

class Directions(Enum):
    RIGHT = 'right'
    LEFT = 'left'
    UP = 'up'
    DOWN = 'down'

direction = Directions.RIGHT

try: 
    with open(filename, "r") as file:
        data = file.read()

        print(data)

except FileNotFoundError:
    print(f"O arquivo '{filename}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

rows = data.split("\n")

def find_initial_line(initial_char, rows):
    global currentX, currentY 
    for indexRow, row in enumerate(rows):
        if row and row[0] == initial_char: 
            print(f"Caractere inicial encontrado na linha {indexRow + 1}")
            currentX = indexRow
            break

find_initial_line(initial_char, rows)

def moveLeft():
    global currentY 
    if currentY > 0:
        currentY -= 1

def moveRight():
    global currentY  
    if currentY < len(rows[currentX]) - 1:
        currentY += 1

def moveUp():
    global currentX  
    if currentX > 0: 
        currentX -= 1

def moveDown():
    global currentX  
    if currentX < len(rows) - 1:
        currentX += 1

while rows[currentX][currentY] != "#":
    currentChar = rows[currentX][currentY]

    if currentChar == "-":
        if(direction==Directions.RIGHT):
            moveRight();
        elif(direction==Directions.LEFT):
            moveLeft()
        elif(direction==Directions.UP):
            moveUp()  
        elif(direction==Directions.DOWN):
            moveDown()        

    elif currentChar.isdigit():
        counter += int(currentChar)
        if(direction==Directions.RIGHT):
            moveRight()
        elif(direction==Directions.LEFT):
            moveLeft()
        elif(direction==Directions.UP):
            moveUp()  
        elif(direction==Directions.DOWN):
            moveDown()                              
    

    elif currentChar =="\\":
        if(direction==Directions.RIGHT):
            moveDown()
            direction=Directions.DOWN
        elif(direction==Directions.DOWN):
            moveRight()
            direction=Directions.RIGHT
        elif(direction==Directions.UP):
            moveLeft()
            direction = Directions.LEFT
        elif(direction==Directions.LEFT):
            moveUp()
            direction=Directions.UP

    elif currentChar =="|":
        if(direction==Directions.RIGHT):
            moveRight();
        elif(direction==Directions.LEFT):
            moveLeft()
        elif(direction==Directions.UP):
            moveUp()  
        elif(direction==Directions.DOWN):
            moveDown() 

    elif currentChar =="/":
        if(direction==Directions.RIGHT):
            moveUp()
            direction=Directions.UP
        elif(direction==Directions.DOWN):
            moveLeft()
            direction=Directions.LEFT
        elif(direction==Directions.UP):
            moveRight()
            direction = Directions.RIGHT
        elif(direction==Directions.LEFT):
            moveDown()
            direction=Directions.DOWN


     

print(f"Encontrou o caractere '#' na linha {currentX + 1}, coluna {currentY + 1}")
print(counter)
