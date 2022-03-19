import math, copy, os
import random
from cmu_112_graphics import *
import time

def init(app):
    app.loggedIn = False 
    app.color = 'brown4'
    app.board = []
    app.flipped = False 
    app.counter = 0
    app.password = ''
    app.middlePiece = 1
    app.registering = False 
    height, width, app.margin, app.rows, app.cols, app.cellSizeHeight = getDimensions()
    app.cellSizeWidth = app.cellSizeHeight
    #app.mainImageLoggedOut = app.loadImage('testImage2.gif')
    url1 = 'https://tcf.admeen.org/game/13000/12674/320x160/fireboy-and-watergirl.jpg'
    url2 = 'https://static.wikia.nocookie.net/falkuzrules/images/1/1c/FBWG1.png/revision/latest?cb=20160319085829'
    url3 = 'https://images-na.ssl-images-amazon.com/images/I/515%2Br6pkGUL.png'
    urlFireboyCharacter = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTk66vZI_QPwx_O3Ke5ILIV8OP7VodiRLZtzg&usqp=CAU'
    app.fireboy1 = app.loadImage(urlFireboyCharacter)
    app.fireboy = app.scaleImage(app.fireboy1,0.12)
    app.mainImageLoggedOut = app.loadImage(url1)
    app.backgroundI = app.loadImage(url2)
    app.backgroundImage = app.scaleImage(app.backgroundI, 1.4)
    app.returnImage = app.loadImage(url3)
    app.returnLogo = app.scaleImage(app.returnImage, 0.15)
    app.blockColor = 'green4'
    app.registeredUsers = []
    app.invalidPassword = False
    app.message = ''
    app.board = [(app.cols * ['brown4']) for row in range(app.rows)]
    for row in range(0, app.rows-1, 4):
        for col in range(app.cols):
            if(col > 15):
                app.board[row][col] = 'green4'
            else:
                app.board[row][col] = 'brown4'
    
    for row in range(1, app.rows-1, 2):
        for col in range(app.cols):
            if(7 <= col <= 13):
                app.board[row][col] = 'green4'
            else:
                app.board[row][col] = 'brown4'
    
    for row in range(2, app.rows-1, 4):
        for col in range(app.cols):
            if(col <= 5):
                app.board[row][col] = 'green4'
            else:
                app.board[row][col] = 'brown4'

    app.obstacles = copy.deepcopy(app.board)
    app.characterMoves = [(len(app.board[0]) * [0]) for row in range(len(app.board))]
    app.characterMoves[len(app.characterMoves)-1][0] = 'fireboy'
    app.characterMoves[len(app.characterMoves)-1][1] = 'watergirl'
    placeObstacles(app)
    app.obstacles = smartBoardGeneration(app, app.obstacles)
    app.hitSwitchFireboy = False
    app.hitSwitchWaterGirl = False
    app.popUpQuestion = False
    app.gameOver = False
    app.pressHoldFireboy = False
    app.pressHoldWatergirl = False
    app.solution = findSolutionWaterGirl(app)
    app.pressedSolution = False
    app.time = time.time()

#Collect all the stars 
def appStarted(app):
    app.loggedIn = False 
    app.color = 'brown4'
    app.board = []
    app.flipped = False 
    app.counter = 0
    app.password = ''
    app.middlePiece = 1
    app.registering = False 
    height, width, app.margin, app.rows, app.cols, app.cellSizeHeight = getDimensions()
    app.cellSizeHeight = (app.height - 2*app.margin) / app.rows
    app.cellSizeWidth = (app.width - 2*app.margin) / app.cols
    #app.mainImageLoggedOut = app.loadImage('testImage2.gif')
    url1 = 'https://tcf.admeen.org/game/13000/12674/320x160/fireboy-and-watergirl.jpg'
    url2 = 'https://static.wikia.nocookie.net/falkuzrules/images/1/1c/FBWG1.png/revision/latest?cb=20160319085829'
    url3 = 'https://images-na.ssl-images-amazon.com/images/I/515%2Br6pkGUL.png'
    urlFireboyCharacter = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTk66vZI_QPwx_O3Ke5ILIV8OP7VodiRLZtzg&usqp=CAU'
    app.fireboy1 = app.loadImage(urlFireboyCharacter)
    app.fireboy = app.scaleImage(app.fireboy1,0.12)
    app.mainImageLoggedOut = app.loadImage(url1)
    app.backgroundI = app.loadImage(url2)
    app.backgroundImage = app.scaleImage(app.backgroundI, 1.4)
    app.returnImage = app.loadImage(url3)
    app.returnLogo = app.scaleImage(app.returnImage, 0.15)
    app.blockColor = 'green4'
    app.registeredUsers = []
    app.invalidPassword = False
    app.message = '' 
    app.board = [(app.cols * ['brown4']) for row in range(app.rows)]
    for row in range(0, app.rows-1, 4):
        for col in range(app.cols):
            if(col > 15):
                app.board[row][col] = 'green4'
            else:
                app.board[row][col] = 'brown4'
    
    for row in range(1, app.rows-1, 2):
        for col in range(app.cols):
            if(7 <= col <= 13):
                app.board[row][col] = 'green4'
            else:
                app.board[row][col] = 'brown4'
    
    for row in range(2, app.rows-1, 4):
        for col in range(app.cols):
            if(col <= 5):
                app.board[row][col] = 'green4'
            else:
                app.board[row][col] = 'brown4'

    app.obstacles = copy.deepcopy(app.board)
    app.characterMoves = [(len(app.board[0]) * [0]) for row in range(len(app.board))]
    app.characterMoves[len(app.characterMoves)-1][0] = 'fireboy'
    app.characterMoves[len(app.characterMoves)-1][1] = 'watergirl'
    placeObstacles(app)
    app.obstacles = smartBoardGeneration(app, app.obstacles)
    app.hitSwitchFireboy = False
    app.hitSwitchWaterGirl = False
    app.popUpQuestion = False
    app.gameOver = False
    app.pressHoldFireboy = False
    app.pressHoldWatergirl = False
    app.solution = findSolutionWaterGirl(app)
    app.pressedSolution = False
    app.time = time.time()

def smartBoardGeneration(app, L):
    if(helper(app, L,len(L)-1,0,0,len(L)-1,directionFlip=False)):
        return L
    else:
        app.obstacles = copy.deepcopy(app.board)
        placeObstacles(app)
        return smartBoardGeneration(app, app.obstacles)
        
    
    #check to try out diff maps randomly generated

#DFS Backtracking algorithm for smart board generation
def helper(app, L, newRow, newCol, currNum, total, directionFlip = False):
    #L[row][col] = currNum
    if(newRow == 0):
        return True 
    else:
        if(directionFlip == False):
            dc = 1
        else:
            dc = -1
        #print(dc)
        if(directionFlip == False):
            for col in range(newCol, len(L[0])):
                if(col + dc >= 0 and col + dc < len(L[0])):
                    newCol += dc
                    if(L[newRow][newCol] == 'black'):
                        break
                    elif(col == len(L)-1):
                        if(L[newRow][newCol] != 'black'):
                            return False

        elif(directionFlip == True):
            for col in range(newCol, -1, -1):
                if(col + dc >= 0 and col + dc < len(L[0])):
                    newCol += dc
                    if(L[newRow][newCol] == 'black'):
                        break
                    elif(col == 0):
                        if(L[newRow][newCol] != 'black'):
                            return False
        
        if(newRow >= 0 and newRow < len(L) and newCol >= 0
            and newCol < len(L[0])):
            if (L[newRow][newCol] == 'black'):
                nextRow, nextCol = nearestBlock(app,newRow,newCol)
                #print(nextRow,nextCol)
                if(app.board[nextRow+1][nextCol-1] == 'green4'):
                    boolDirection = True 
                else:
                    boolDirection = False

                if(helper(app,L,nextRow,nextCol,currNum+1,total,directionFlip = boolDirection)):
                    return True

        return False

#Uses DFS backtracking to display solution for this board
def waterGirlSolutionDisplay(app):
    pass

#def timerFired(app):
    #if(app.loggedIn):
       # move(app)

def move(app):
    row, col = returnRowColFireboy(app)
    app.characterMoves[row][col] = 0
    app.characterMoves[row][col+2] = 'fireboy'

#DFS Backtracking to create solution path with best possible score
def solveLevel(app, L, newRow, newCol, currNum, directionFlip = False):
    visited = set()
    targetRow,targetCol = 0,0
    def solve(row,col):
        # base cases
        if (row,col) in visited:
            return False
        visited.add((row,col))
        if (row,col)==(targetRow,targetCol):
            return True
        # recursive case
        else:
            pass

        visited.remove((row,col))
        return False

    return visited if solve(0,0) else None


def findSolutionWaterGirl(app):
    solution = []
    row = len(app.board)-1
    while row != 0:
        switchIndex = app.obstacles[row].index('black')
        #print(switchIndex)
        for col in range(len(app.board[0])):
            if(app.obstacles[row][col] == 'True'):
                solution.append([row,col])
        
        solution.append([row,switchIndex])
        nextRow, nextCol = nearestBlock(app, row, switchIndex)
        solution.append([nextRow,nextCol])
        row = nextRow
    
    #print(solution)
    return solution


def drawSolutionWaterGirl(app, canvas):
    if(app.pressedSolution):
        for i in range(0, len(app.solution)-1):
            row1 = app.solution[i][0]
            col1 = app.solution[i][1]

            row2 = app.solution[i+1][0]
            col2 = app.solution[i+1][1]

            x1 = (col1 * app.cellSizeWidth) + app.margin
            y1 = row1 * app.cellSizeHeight + app.margin
            x2 = (x1 + app.cellSizeWidth)
            y2 = y1 + app.cellSizeHeight
            xCoord1 = (x1+x2)//2
            yCoord1 = (y1+y2)//2

            x3 = (col2 * app.cellSizeWidth) + app.margin
            y3 = row2 * app.cellSizeHeight + app.margin
            x4 = (x3 + app.cellSizeWidth)
            y4 = y3 + app.cellSizeHeight
            xCoord2 = (x3+x4)//2
            yCoord2 = (y3+y4)//2

            canvas.create_line(xCoord1,yCoord1,xCoord2,yCoord2,fill = 'red', width = 4)


def placeObstacles(app):
    for row in range(len(app.board)):
        temp = []
        for col in range(len(app.board[0])):
            if(row != len(app.board)-1):
                if(app.board[row+1][col] == 'green4'):
                    if(app.board[row][col] != 'green4'):
                        if app.obstacles[row][col] != 'black':
                            temp.append(col)
                                
        if(len(temp)>0):
            randomNum = random.choice(temp)
            temp.remove(randomNum)
            app.obstacles[row][randomNum] = 'black'
            randomNum2 = random.choice(temp)
            temp.remove(randomNum2)
            randomColor = random.choice(['pink','blue'])
            app.obstacles[row][randomNum2] = randomColor
            randomNum3 = random.choice(temp)
            randomColorBool = random.choice(['True','False'])
            app.obstacles[row][randomNum3] = randomColorBool
 
    for row in range(len(app.board)):
        if(row != len(app.obstacles)-1 and row != 0):
            randomNumberOfStars = random.randint(0,3)
            for col in (range(randomNumberOfStars)):
                randomCol = random.randint(7,14)
                if(app.board[row+1][randomCol] == 'green4'):
                    if(app.board[row][randomCol] != 'green4'):
                        randomColorBool1 = random.choice(['True','False'])
                        app.obstacles[row][randomCol] = randomColorBool1
        elif(row == len(app.board)-1):
            randomNumberOfStars = random.randint(1,6)
            for col in (range(randomNumberOfStars)):
                randomColumn = random.randint(3,len(app.obstacles[0])-1)
                randomColorBool = random.choice(['True','False'])
                app.obstacles[row][randomColumn] = randomColorBool
    
    randomBaseCol = random.randint(0,len(app.obstacles[0])-1)
    app.obstacles[len(app.obstacles)-1][15] = 'black'

'''
def placeTeleports(app):
    for row in range(len(app.board)):
        for col in range(len(app.board[0])):
'''

def drawMainCharacters(app,canvas):
    for row in range(len(app.characterMoves)):
        for col in range(len(app.characterMoves[0])):
            if(app.characterMoves[row][col] == 'fireboy'):
                drawCharacter(app,canvas,row,col,'blue')
            elif(app.characterMoves[row][col] == 'watergirl'):
                drawCharacter(app,canvas,row,col,'HotPink3')
            elif(app.characterMoves[row][col] == 'duo'):
                drawDuo(app,canvas,row,col)


def drawDuo(app,canvas,row,col):
    x1 = (col * app.cellSizeWidth) + app.margin
    y1 = row * app.cellSizeHeight + app.margin
    x2 = x1 + app.cellSizeWidth
    y2 = y1 + app.cellSizeHeight
    canvas.create_oval(x1,y1,(x1+x2)//2,(y1+y2)//2,fill = 'blue' , outline = 'black')
    canvas.create_oval((x1+x2)//2,(y1+y2)//2,x2,y2,fill = 'HotPink3' , outline = 'black')

def drawObstacles(app, canvas):
    for row in range(len(app.obstacles)):
        for col in range(len(app.obstacles[0])):
            if(app.obstacles[row][col] == 'black'):
                x1 = (col * app.cellSizeWidth) + app.margin + 10
                y1 = row * app.cellSizeHeight + app.margin + 25
                x2 = x1 + 10
                y2 = y1 + 5
                canvas.create_rectangle(x1,y1,x2,y2,fill = 'black' ,width = 4)
            elif(app.obstacles[row][col] == 'blue'):
                x1 = (col * app.cellSizeWidth) + app.margin
                y1 = row * app.cellSizeHeight + app.margin + app.cellSizeHeight
                x2 = x1 + app.cellSizeWidth
                y2 = y1 + 15
                canvas.create_polygon(x1,y1,(x1+x2)//2,y2,x2,y1,fill = 'blue',outline = 'black')
            elif(app.obstacles[row][col] == 'pink'):
                x1 = (col * app.cellSizeWidth) + app.margin
                y1 = row * app.cellSizeHeight + app.margin + app.cellSizeHeight
                x2 = x1 + app.cellSizeWidth
                y2 = y1 + 15
                canvas.create_polygon(x1,y1,(x1+x2)//2,y2,x2,y1,fill = 'HotPink3',outline = 'black' )
            elif(app.obstacles[row][col] == 'True'):
                x1 = (col * app.cellSizeWidth) + app.margin
                y1 = row * app.cellSizeHeight + app.margin 
                x2 = x1 + app.cellSizeWidth
                y2 = y1 + app.cellSizeHeight
                startX = (x1+x2)//2
                xFirstVertex = (startX + x2)//2 
                xSecondVertex = (startX + x1)//2
                yFirstVertex = y1 + 11
                canvas.create_polygon(startX, y1,
                    xFirstVertex, yFirstVertex, x2, (y1+y2)//2,
                    xFirstVertex,yFirstVertex + 8,
                    startX,y2,xSecondVertex,yFirstVertex+8,
                    x1,(y1+y2)//2,xSecondVertex,yFirstVertex,
                    startX,y1,fill = 'blue', outline = 'black')
            elif(app.obstacles[row][col] == 'False'):
                x1 = (col * app.cellSizeWidth) + app.margin
                y1 = row * app.cellSizeHeight + app.margin 
                x2 = x1 + app.cellSizeWidth
                y2 = y1 + app.cellSizeHeight
                startX = (x1+x2)//2
                xFirstVertex = (startX + x2)//2 
                xSecondVertex = (startX + x1)//2
                yFirstVertex = y1 + 11
                canvas.create_polygon(startX, y1,
                    xFirstVertex, yFirstVertex, x2, (y1+y2)//2,
                    xFirstVertex,yFirstVertex + 8,
                    startX,y2,xSecondVertex,yFirstVertex+8,
                    x1,(y1+y2)//2,xSecondVertex,yFirstVertex,
                    startX,y1,fill = 'HotPink3', outline = 'black')
            elif(app.obstacles[row][col] == 'orange'):
                x1 = (col * app.cellSizeWidth) + app.margin + 10
                y1 = row * app.cellSizeHeight + app.margin + 10
                x2 = x1 + 10
                y2 = y1 + 10
                canvas.create_oval(x1,y1,x2,y2,fill='orange')
    
    
def returnRowColFireboy(app):
    for row in range(len(app.characterMoves)):
        for col in range(len(app.characterMoves[0])):
            if(app.characterMoves[row][col] == 'fireboy' or
                app.characterMoves[row][col] == 'duo'):
                return row, col

def returnRowColWaterGirl(app):
    for row in range(len(app.characterMoves)):
        for col in range(len(app.characterMoves[0])):
            if(app.characterMoves[row][col] == 'watergirl' or
                app.characterMoves[row][col] == 'duo'):
                return row, col

def fireboyGetsStar(app):
    rowFireboy, colFireboy = returnRowColFireboy(app)
    if(app.obstacles[rowFireboy][colFireboy] == 'True'):
        app.obstacles[rowFireboy][colFireboy] = 'brown4'
    
def watergirlGetsStar(app):
    rowWaterGirl, colWaterGirl = returnRowColWaterGirl(app)
    if(app.obstacles[rowWaterGirl][colWaterGirl] == 'False'):
        app.obstacles[rowWaterGirl][colWaterGirl] = 'brown4'

def nearestBlock(app, rowBase, colBase):
    minimumDifference = 100000
    minRow = 0
    minCol = 0
    for row in range(len(app.board)):
        for col in range(len(app.board[0])):
            if(row != len(app.board)-1):
                if(app.board[row][col] == 'brown4'):
                    if(app.board[row+1][col] == 'green4'):
                        diffRow = abs(row - rowBase)
                        diffCol = abs(col - colBase)
                        
                        pythagoreanthirdSide = (diffRow ** 2) + (diffCol ** 2)

                        if(pythagoreanthirdSide < minimumDifference):
                            if(diffCol != 0 and diffRow != 0):
                                if(row == isClosestLegalRow(app,rowBase,colBase)):
                                    minimumDifference = pythagoreanthirdSide
                                    minRow = row
                                    minCol = col
    return minRow, minCol

def isClosestLegalRow(app, rowBase, colBase):
    for row in range(rowBase-1,-1,-1):
        for col in range(len(app.board[0])):
            if(app.board[row][col] == 'brown4'):
                if(app.board[row+1][col] == 'green4'):
                    return row

def characterStepsOnSwitch(app):
    row, col = returnRowColFireboy(app)
    if(app.obstacles[row][col] == 'black'):
        return True 
    else:
        return False

def setSwitchBoolean(app):  
    row, col = returnRowColFireboy(app)
    if(app.obstacles[row][col] == 'black'):
        app.hitSwitchFireboy = True 
    else:
        app.hitSwitchFireboy = False

def setSwitchBooleanWaterGirl(app):
    row, col = returnRowColWaterGirl(app)
    if(app.obstacles[row][col] == 'black'):
        #print("YEPP")
        app.hitSwitchWaterGirl = True
    else:
        app.hitSwitchWaterGirl = False

def characterHitsSwitch(app, canvas):
    if(app.hitSwitchFireboy == True):
        row, col = returnRowColFireboy(app)
        row2, col2 = nearestBlock(app, row, col)
        if(app.board[row2+1][col2+1] == 'green4'):
            drawSwitchConnector(app,canvas,row,col,row2,col2)
            if(app.pressHoldWatergirl == False and app.pressHoldFireboy == False):
                drawTapButton(app,canvas,row,col)
        else:
            drawSwitchConnector(app,canvas,row,col-1,row2,col2+1)
            if(app.pressHoldWatergirl == False and app.pressHoldFireboy == False):
                drawTapButton(app,canvas,row,col)

    elif(app.hitSwitchWaterGirl == True):
        row, col = returnRowColWaterGirl(app)
        row2, col2 = nearestBlock(app, row, col)
        if(app.board[row2+1][col2+1] == 'green4'):
            drawSwitchConnector(app,canvas,row,col,row2,col2)
            if(app.pressHoldWatergirl == False and app.pressHoldFireboy == False):
                drawTapButton(app,canvas,row,col)
        else:
            drawSwitchConnector(app,canvas,row,col-1,row2,col2+1)
            if(app.pressHoldWatergirl == False and app.pressHoldFireboy == False):
                drawTapButton(app,canvas,row,col)

def drawTapButton(app, canvas, row, col):
    x1 = (col * app.cellSizeWidth) + app.margin
    y1 = row * app.cellSizeHeight + app.margin
    x2 = (x1 + app.cellSizeWidth)
    y2 = y1 + app.cellSizeHeight
    canvas.create_text((x1+x2)//2,(y1+y2)//2, text = 'Tap!', fill = 'black')

def drawSwitchConnector(app,canvas,row1,col1,row2,col2):
    x1 = (col1 * app.cellSizeWidth) + app.margin
    y1 = row1 * app.cellSizeHeight + app.margin
    x2 = (x1 + app.cellSizeWidth)
    y2 = y1 + app.cellSizeHeight

    xCoord2 = (col2 * app.cellSizeWidth) + app.margin
    yCoord2 = row2 * app.cellSizeHeight + app.margin
    yCoordConnectorLine = yCoord2 + app.cellSizeHeight

    canvas.create_line(x2,y2,xCoord2,yCoordConnectorLine,fill = 'black', width = 4)

def drawCharacter(app,canvas,row,col,color):
    x1 = (col * app.cellSizeWidth) + app.margin
    y1 = row * app.cellSizeHeight + app.margin
    x2 = x1 + app.cellSizeWidth
    y2 = y1 + app.cellSizeHeight
    canvas.create_oval(x1,y1,x2,y2,fill = color , outline = 'black')

def timerFired(app):
    if(time.time() - app.time >= 1.5):
        for row in range(0, len(app.board)-2, 2):
            for col in range(14,16):
                app.obstacles[row][col] = 'orange'

def keyPressed(app, event):
    if(app.loggedIn == False):
        if(event.key == 'Enter'):
            if(app.password == ''):
                app.loggedIn = False 
                app.invalidPassword = True
                app.message = 'Enter User Above'
            else:
                if(loginChecker(app)):
                    app.invalidPassword = False
                    app.loggedIn = True
                else:
                    app.loggedIn = False 
                    app.invalidPassword = True
                    app.message = 'User Not Registered'
                    print(app.invalidPassword)
    
    if(app.registering):
        if(event.key == 'Enter'):
            app.registering = False
            app.loggedIn = False 
            app.registeredUsers.append(app.password)
            app.password = ''

    if(event.key != 'Delete'):
        if(event.key != 'Enter'):
            app.password += event.key
    else:
        app.password = app.password[:-1]
    
    if(event.key == 'q'):
        if(app.loggedIn):
            app.loggedIn = False
            app.password = ''
    
    if(event.key == '/'):
        app.loggedIn = True
    
    if(app.loggedIn):
        if(event.key == 'Right'):
            moveWaterGirlRight(app)
        elif(event.key == 'Left'):
            moveWaterGirlLeft(app)

        if(event.key == 'd'):
            moveFireboyRight(app)
        elif(event.key == 'a'):
            moveFireboyLeft(app)
    
    if(app.loggedIn):
        if(event.key == 'r'):
            init(app)
        elif(event.key == 'm'):
            move(app)
        elif(event.key == 's'):
            app.pressedSolution = not app.pressedSolution

def moveFireboyLeft(app):
    for row in range(len(app.characterMoves)):
        for col in range(len(app.characterMoves[0])):
            if(col - 1 >= 0):
                if(app.characterMoves[row][col] == 'fireboy'):
                    if(app.characterMoves[row][col-1] == 'watergirl'):
                        app.characterMoves[row][col] = 0
                        app.characterMoves[row][col-1] = 'duo'
                        fireboyGetsStar(app)
                        setSwitchBoolean(app)
                        checkTerrainLavaFireboy(app)
                        checkIfLavaInfrontFireboy(app)
                        break
                    else:
                        app.characterMoves[row][col] = 0
                        app.characterMoves[row][col-1] = 'fireboy'
                        fireboyGetsStar(app)
                        setSwitchBoolean(app)
                        checkTerrainLavaFireboy(app)
                        checkIfLavaInfrontFireboy(app)
                        break
                elif(app.characterMoves[row][col] == 'duo'):
                        app.characterMoves[row][col] = 'watergirl'
                        app.characterMoves[row][col-1] = 'fireboy'
                        fireboyGetsStar(app)
                        setSwitchBoolean(app)
                        checkTerrainLavaFireboy(app)
                        checkIfLavaInfrontFireboy(app)
                        break

def moveFireboyRight(app):
    for row in range(len(app.characterMoves)):
        for col in range(len(app.characterMoves[0])):
            if(col + 1 < len(app.characterMoves[0])):
                if(app.characterMoves[row][col] == 'fireboy'):
                    if(app.characterMoves[row][col+1] == 'watergirl'):
                        app.characterMoves[row][col] = 0
                        app.characterMoves[row][col+1] = 'duo'
                        fireboyGetsStar(app)
                        setSwitchBoolean(app)
                        checkTerrainLavaFireboy(app)
                        checkIfLavaInfrontFireboy(app)
                        break
                    else:
                        app.characterMoves[row][col] = 0
                        app.characterMoves[row][col+1] = 'fireboy'
                        fireboyGetsStar(app)
                        setSwitchBoolean(app)
                        checkTerrainLavaFireboy(app)
                        checkIfLavaInfrontFireboy(app)
                        break
                elif(app.characterMoves[row][col] == 'duo'):
                        app.characterMoves[row][col] = 'watergirl'
                        app.characterMoves[row][col+1] = 'fireboy'
                        fireboyGetsStar(app)
                        setSwitchBoolean(app)
                        checkTerrainLavaFireboy(app)
                        checkIfLavaInfrontFireboy(app)
                        break
                
def moveWaterGirlRight(app):
    for row in range(len(app.characterMoves)):
        for col in range(len(app.characterMoves[0])):
            if(col + 1 < len(app.characterMoves[0])):
                if(app.characterMoves[row][col] == 'watergirl'):
                    if(app.characterMoves[row][col+1] == 'fireboy'):
                        checkIfLavaInfrontWatergirl(app)
                        app.characterMoves[row][col] = 0
                        app.characterMoves[row][col+1] = 'duo'
                        watergirlGetsStar(app)
                        setSwitchBooleanWaterGirl(app)
                        checkTerrainLavaWatergirl(app)
                        checkIfLavaInfrontWatergirl(app)
                        
                        break
                    else:
                        checkIfLavaInfrontWatergirl(app)
                        app.characterMoves[row][col] = 0
                        app.characterMoves[row][col+1] = 'watergirl'
                        watergirlGetsStar(app)
                        setSwitchBooleanWaterGirl(app)
                        checkTerrainLavaWatergirl(app)
                        checkIfLavaInfrontWatergirl(app)
                        break
                elif(app.characterMoves[row][col] == 'duo'):
                        checkIfLavaInfrontWatergirl(app)
                        app.characterMoves[row][col] = 'fireboy'
                        app.characterMoves[row][col+1] = 'watergirl'
                        watergirlGetsStar(app)
                        setSwitchBooleanWaterGirl(app)
                        checkTerrainLavaWatergirl(app)
                        checkIfLavaInfrontWatergirl(app)
                        break

def moveWaterGirlLeft(app):
    for row in range(len(app.characterMoves)):
        for col in range(len(app.characterMoves[0])):
            if(col - 1 >= 0):
                if(app.characterMoves[row][col] == 'watergirl'):
                    if(app.characterMoves[row][col-1] == 'fireboy'):
                        app.characterMoves[row][col] = 0
                        app.characterMoves[row][col-1] = 'duo'
                        watergirlGetsStar(app)
                        setSwitchBooleanWaterGirl(app)
                        checkTerrainLavaWatergirl(app)
                        checkIfLavaInfrontWatergirl(app)
                        break
                    else:
                        app.characterMoves[row][col] = 0
                        app.characterMoves[row][col-1] = 'watergirl'
                        watergirlGetsStar(app)
                        setSwitchBooleanWaterGirl(app)
                        checkTerrainLavaWatergirl(app)
                        checkIfLavaInfrontWatergirl(app)
                        break
                elif(app.characterMoves[row][col] == 'duo'):
                        app.characterMoves[row][col] = 'fireboy'
                        app.characterMoves[row][col-1] = 'watergirl'
                        watergirlGetsStar(app)
                        setSwitchBooleanWaterGirl(app)
                        checkTerrainLavaWatergirl(app)
                        checkIfLavaInfrontWatergirl(app)
                        break

def checkTerrainLavaWatergirl(app):
    row, col = returnRowColWaterGirl(app)
    if(app.obstacles[row][col] == 'blue'):
        app.gameOver = True

def checkIfLavaInfrontFireboy(app):
    if(app.hitSwitchFireboy):
        baseRow, baseCol = returnRowColFireboy(app)
        row, col = nearestBlock(app,baseRow,baseCol)
        if(col != len(app.board[0])-1 and col != 0):
            if(app.obstacles[row][col] == 'blue' or app.obstacles[row][col] == 'blue'):
                app.pressHoldFireboy = True
            else:
                app.pressHoldFireboy = False
    else:
        row, col = returnRowColFireboy(app)
        if(col != len(app.board[0])-1 and col != 0):
            if(app.obstacles[row][col+1] == 'pink' or app.obstacles[row][col-1] == 'pink'):
                app.pressHoldFireboy = True
            else:
                app.pressHoldFireboy = False

def checkIfLavaInfrontWatergirl(app):
    if(app.hitSwitchWaterGirl):
        baseRow, baseCol = returnRowColWaterGirl(app)
        row, col = nearestBlock(app,baseRow,baseCol)
        if(col != len(app.board[0])-1 and col != 0):
            if(app.obstacles[row][col] == 'blue' or app.obstacles[row][col] == 'blue'):
                app.pressHoldWatergirl = True
            else:
                app.pressHoldWatergirl = False
    else:
        row, col = returnRowColWaterGirl(app)
        if(col != len(app.board[0])-1 and col != 0):
            if(app.obstacles[row][col+1] == 'blue' or app.obstacles[row][col-1] == 'blue'):
                app.pressHoldWatergirl = True
            else:
                app.pressHoldWatergirl = False

def checkTerrainLavaFireboy(app):
    row, col = returnRowColFireboy(app)
    if(app.obstacles[row][col] == 'pink'):
        app.gameOver = True
        
def drawHoldButton(app, canvas, row, col):
    x1 = (col * app.cellSizeWidth) + app.margin
    y1 = row * app.cellSizeHeight + app.margin
    x2 = (x1 + app.cellSizeWidth)
    y2 = y1 + app.cellSizeHeight
    canvas.create_text((x1+x2)//2,(y1+y2)//2, text = 'Hold!', fill = 'black')


def drawHoldFunction(app,canvas):
    if(app.pressHoldFireboy == True):
        row, col = returnRowColFireboy(app)
        drawHoldButton(app,canvas,row,col)

    elif(app.pressHoldWatergirl == True):
        row, col = returnRowColWaterGirl(app)
        drawHoldButton(app,canvas,row,col)


def drawGameOverMessage(app, canvas):
    canvas.create_rectangle(app.width//4,app.height//4,app.width*3//4,app.height*3//4,fill = 'black')
    canvas.create_text(app.width//2, app.height//2,text = 'Game Over!', 
    font = 'Helvetica 26 bold', fill='white')

#Add sprites, motion --> adds complexity
#Gravity components, sliding
#Lava components
#Working game --> by TP1 Monday
#Path generation


def loginChecker(app):
    for user in app.registeredUsers:
        if(app.password == user):
            return True 
    return False

def mousePressed(app, event):
    if(app.loggedIn == False):
        if(event.x >= app.width//4 and event.x <= app.width//4+150):
            if(event.y >= app.height//4+90 and event.y <= app.height//4+120):
                if(app.password == ''):
                    app.loggedIn = False
                    app.invalidPassword = True
                    app.message = 'Enter User Above'
                else:
                    if(loginChecker(app)):
                        app.invalidPassword = False
                        app.loggedIn = True
                    else:
                        app.loggedIn = False
                        app.invalidPassword = True
                        app.message = 'User Not Registered'
                        print(app.invalidPassword)

    if(app.loggedIn == False):
        if(event.x >= app.width//4 and event.x <= app.width//4+150):
            if(event.y >= app.height//4 and event.y <= app.height//4+30):
                app.invalidPassword = False
                app.registering = True
                app.password = ''
    
    if(app.registering == True):
        if(event.x >= app.width//4 +320 and event.x <= app.width//4+390):
            if(event.y >= app.height//4+90 and event.y <= app.height//4+120):
                app.registering = False
                app.loggedIn = False
                app.registeredUsers.append(app.password)
                app.password = ''
                print(app.registeredUsers)
        elif(event.x >= app.width//4 -40 and event.x <= app.width//4+40):
            if(event.y >= 365 and event.y <= 435):
                app.registering = False
                app.password = app.password[:-1]
                app.password= ''
    
    if(app.loggedIn):
        if(app.hitSwitchFireboy == True):
            row, col = returnRowColFireboy(app)
            row2, col2 = nearestBlock(app, row, col)
            x1 = (col * app.cellSizeWidth) + app.margin
            y1 = row * app.cellSizeHeight + app.margin
            x2 = (x1 + app.cellSizeWidth)
            y2 = y1 + app.cellSizeHeight

            if(event.x >= x1 and event.x <= x2):
                if(event.y >= y1 and event.y <= y2):
                    app.characterMoves[row][col] = 0
                    app.characterMoves[row2][col2] = 'fireboy'
                    app.hitSwitchFireboy = False
                    app.popUpQuestion = True
                    fireboyGetsStar(app)
                    setSwitchBoolean(app)
                    checkIfLavaInfrontFireboy(app)
                    #app.pressHoldFireboy = False 
                else:
                    app.popUpQuestion = False
            else:
                app.popUpQuestion = False

        elif(app.hitSwitchWaterGirl == True):
            row, col = returnRowColWaterGirl(app)
            row2, col2 = nearestBlock(app, row, col)
            x1 = (col * app.cellSizeWidth) + app.margin
            y1 = row * app.cellSizeHeight + app.margin
            x2 = (x1 + app.cellSizeWidth)
            y2 = y1 + app.cellSizeHeight

            if(event.x >= x1 and event.x <= x2):
                if(event.y >= y1 and event.y <= y2):
                    app.characterMoves[row][col] = 0
                    app.characterMoves[row2][col2] = 'watergirl'
                    app.hitSwitchWaterGirl = False
                    app.popUpQuestion = True
                    watergirlGetsStar(app)
                    setSwitchBoolean(app)
                    checkIfLavaInfrontWatergirl(app)
                    #app.pressHoldWatergirl = False
                else:
                    app.popUpQuestion = False
            else:
                app.popUpQuestion = False

        elif(app.pressHoldFireboy):
            row1, col1 = returnRowColFireboy(app)
            x1 = (col1 * app.cellSizeWidth) + app.margin
            y1 = row1 * app.cellSizeHeight + app.margin
            x2 = (x1 + app.cellSizeWidth)
            y2 = y1 + app.cellSizeHeight
            if(event.x >= x1 and event.x <= x2):
                if(event.y >= y1 and event.y <= y2):
                    if(app.obstacles[row1][col1-1] == 'pink'):
                        app.obstacles[row1][col1-1] = 'blue'
                    elif(app.obstacles[row1][col1+1] == 'pink'):
                        app.obstacles[row1][col1+1] = 'blue'
                    app.pressHoldFireboy = False 


        elif(app.pressHoldWatergirl):
            row, col = returnRowColWaterGirl(app)
            x1 = (col * app.cellSizeWidth) + app.margin
            y1 = row * app.cellSizeHeight + app.margin
            x2 = (x1 + app.cellSizeWidth)
            y2 = y1 + app.cellSizeHeight

            if(event.x >= x1 and event.x <= x2):
                if(event.y >= y1 and event.y <= y2):
                    if(app.obstacles[row][col-1] == 'blue'):
                        app.obstacles[row][col-1] = 'pink'
                    elif(app.obstacles[row][col+1] == 'blue'):
                        app.obstacles[row][col+1] = 'pink'

                    app.pressHoldWatergirl = False



def drawCell(app,canvas,row,col,color):
    x1 = (col * app.cellSizeWidth) + app.margin
    y1 = row * app.cellSizeHeight + app.margin
    x2 = x1 + app.cellSizeWidth
    y2 = y1 + app.cellSizeHeight
    canvas.create_rectangle(x1,y1,x2,y2,fill = color,width = 4)

def drawBoard(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill = 'black')
    for row in range(app.rows):
        if(app.middlePiece == 5):
            print(app.middlePiece)
        for col in range(app.cols):
            if(row == 0 and col > 15):
                if(app.board[row][col] == 'green4'):
                    drawCell(app,canvas,row,col,'brown4')
                    x1 = (col * app.cellSizeWidth) + app.margin
                    y1 = row * app.cellSizeHeight + app.margin + 25
                    x2 = x1 + app.cellSizeWidth
                    y2 = y1 + 5
                    canvas.create_oval(x1,y1,x2,y2,fill='black')
            else:
                if(app.board[row][col] == 'pink'):
                    drawCell(app,canvas,row,col,'brown4')
                    drawFigure(app,canvas,row,col,color='pink')
                elif(app.board[row][col] == 'blue'):
                    drawCell(app,canvas,row,col,'brown4')
                    drawFigure(app,canvas,row,col,color='blue')
                elif(app.board[row][col] == 'orange'):
                    x1 = (col * app.cellSizeWidth) + app.margin + 10
                    y1 = row * app.cellSizeHeight + app.margin + 10
                    x2 = x1 + 10
                    y2 = y1 + 10
                    canvas.create_oval(x1,y1,x2,y2,fill='orange')
                else:
                    color = app.board[row][col]
                    drawCell(app,canvas,row,col,color)

def drawFigure(app,canvas,row,col,color):
    x1 = (col * app.cellSizeWidth) + app.margin 
    y1 = row * app.cellSizeHeight + app.margin
    x2 = x1 + app.cellSizeWidth
    y2 = y1 + app.cellSizeHeight
    canvas.create_oval(x1,y1,x2,y2,fill = f'{color}')
    

def drawMainScreen(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.backgroundImage))
    canvas.create_rectangle(app.width//4,app.height//4,app.width//4+150,app.height//4+30,fill = 'white')
    canvas.create_text(app.width//4 + 80, app.height//4+15, text = 'Register User',fill='black')
    canvas.create_rectangle(app.width//4,app.height//4+90,app.width//4+150,app.height//4+120,fill = 'white')
    canvas.create_text(app.width//4 + 80, app.height//4+105, text = 'Login (Click)',fill='black')
    canvas.create_text(app.width//2+20, app.height//2 - 20, text = f'{app.password}',fill='white', anchor = 'w')
    canvas.create_line(app.width//4 + 170,app.height//4+120,app.width//4 + 310,app.height//4+120, fill = 'white')
    canvas.create_text(app.width//4 + 220, app.height//4+130, text = 'User', anchor = 'w', fill = 'white')
    canvas.create_image(app.width//2, 400, image=ImageTk.PhotoImage(app.mainImageLoggedOut))

def drawRegistrationPage(app,canvas):
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.backgroundImage))
    canvas.create_rectangle(app.width//4,app.height//4+90,app.width//4+150,app.height//4+120,fill = 'white')
    canvas.create_text(app.width//4 + 80, app.height//4+105, text = 'Type Username',fill='black')
    canvas.create_text(app.width//2+20, app.height//2 - 20, text = f'{app.password}',fill='white', anchor = 'w')
    canvas.create_line(app.width//4 + 170,app.height//4+120,app.width//4 + 310,app.height//4+120, fill = 'white')
    canvas.create_text(app.width//4 + 220, app.height//4+130, text = 'User', anchor = 'w', fill = 'white')
    canvas.create_oval(app.width//4+320,app.height//4+90,app.width//4+390,app.height//4+120,fill = 'blue')
    canvas.create_text(app.width//4+337, app.height//4 + 105, text = 'Submit',fill='red', anchor = 'w')
    canvas.create_rectangle(app.width//4-40,365,app.width//4+40,435,fill = 'black')
    canvas.create_image(app.width//4, 400, image=ImageTk.PhotoImage(app.returnLogo))

def invalidPasswordMessage(app,canvas):
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.backgroundImage))
    canvas.create_rectangle(app.width//4,app.height//4,app.width//4+150,app.height//4+30,fill = 'white')
    canvas.create_text(app.width//4 + 80, app.height//4+15, text = 'Register User',fill='black')
    canvas.create_rectangle(app.width//4,app.height//4+90,app.width//4+150,app.height//4+120,fill = 'white')
    canvas.create_text(app.width//4 + 80, app.height//4+105, text = 'Login (Click)',fill='black')
    canvas.create_text(app.width//2+20, app.height//2 - 20, text = f'{app.password}',fill='white', anchor = 'w')
    canvas.create_line(app.width//4 + 170,app.height//4+120,app.width//4 + 310,app.height//4+120, fill = 'white')
    canvas.create_text(app.width//4 + 220, app.height//4+130, text = 'User', anchor = 'w', fill = 'white')
    canvas.create_image(app.width//2, 400, image=ImageTk.PhotoImage(app.mainImageLoggedOut))
    canvas.create_text(app.width//2,app.height//2+30,text = f'{app.message}', fill = 'red')

def redrawAll(app,canvas):
    if(app.invalidPassword == True):
        invalidPasswordMessage(app,canvas)
    else:     
        if(app.loggedIn == True):
            drawBoard(app,canvas)
            drawObstacles(app,canvas)
            drawMainCharacters(app,canvas)
            characterHitsSwitch(app,canvas)
            drawHoldFunction(app, canvas)
            drawSolutionWaterGirl(app,canvas)
            if(app.gameOver == True):
                drawGameOverMessage(app,canvas)
        else:
            drawMainScreen(app,canvas)
        if(app.registering == True):
            drawRegistrationPage(app,canvas)


def getDimensions():
    cols = 20
    margin = 30
    rows = random.choice([15,16])
    cellSizeHeight = 30
    height = (cellSizeHeight * rows) + (2 * margin)
    width = (cellSizeHeight * cols) + (2 * margin)
    return height, width, margin, rows, cols, cellSizeHeight

def playFireboyWaterGirl():
    height, width, margin, rows, cols, cellSizeHeight = getDimensions()
    runApp(width = width, height = height)


def main():
    playFireboyWaterGirl()

if __name__ == '__main__':
    main()

