#Vasudha Srinivasan
#15-112 Term Project
#Section A
#Andrew ID: vasudhas

#cmu_112_graphics file from http://www.cs.cmu.edu/~112/notes/hw7.html
from cmu_112_graphics import *
from tkinter import *
import random, string, math, copy, time

#draws title screen
class TitleScreenMode(Mode):
    #goes to intro when any key is pressed
    def keyPressed(mode, event):
        mode.app.setActiveMode(mode.app.introMode)

    #draws title screen
    def redrawAll(mode, canvas):
        canvas.create_rectangle(0,0,mode.width, mode.height, fill='black')
        canvas.create_text(mode.width//2, mode.height//3,text='ESCAPE!',
                font='MSSerif 40 bold', fill='white')
        canvas.create_text(mode.width//2, mode.height*2/3,
                text='press any key to begin',
                font='MSSerif 20 bold', fill='white')

#put starting animation (introduction to storyline) here
class IntroMode(Mode):
    #draws intro text
    def redrawAll(mode,canvas):
        introText='''
        You wake up in a dark room,
        with no memories of who you are and how you got there.
        All you know is that you must return home. You must escape.
        Slowly, you get up move forward to face the journey ahead.
    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
        
        You are about to enter the maze that will determine your fate.

        Press the arrow keys to navigate.
            (in 3D mode, press 'Up' to move forward, 'Down' to move back, 
            and the left and right arrow keys to change orientation)

        Press 'i' to see the instructions again.

        Press 's' to give up, I will light the way.

        Press 'c' for a change in your form.

        Good Luck.
        press any key to begin.
            '''
        canvas.create_rectangle(0,0,mode.width, mode.height, fill='black')
        canvas.create_text(mode.width/2,mode.height/2,text=introText,
                font='MSSerif 17', fill='white', anchor='center')

    #goes on to game mode when any key is pressed
    def keyPressed(mode, event):
        mode.app.setActiveMode(mode.app.chooseColor)

class ChooseColor(Mode):
    #sets up initial list of colors
    def appStarted(mode):
        mode.colorList=['rosybrown','lightpink','coral','lightgreen',
                'cyan','lightblue','violet','plum','brown','red',
                'darkorange','green','blue','indigo','purple','black']

    #chooses color for board & sets app variable based on where player clicks
    def mousePressed(mode, event):
        if (event.x>mode.width*2/12 and event.x<mode.width*3/12
            and event.y>mode.height*7/12 and event.y<mode.height*8/12):
            mode.app.color=mode.colorList[0]
        elif (event.x>mode.width*3/12 and event.x<mode.width*4/12
            and event.y>mode.height*7/12 and event.y<mode.height*8/12):
            mode.app.color=mode.colorList[1]
        elif (event.x>mode.width*4/12 and event.x<mode.width*5/12
            and event.y>mode.height*7/12 and event.y<mode.height*8/12):
            mode.app.color=mode.colorList[2]
        elif (event.x>mode.width*5/12 and event.x<mode.width*6/12
            and event.y>mode.height*7/12 and event.y<mode.height*8/12):
            mode.app.color=mode.colorList[3]
        elif (event.x>mode.width*6/12 and event.x<mode.width*7/12
            and event.y>mode.height*7/12 and event.y<mode.height*8/12):
            mode.app.color=mode.colorList[4]
        elif (event.x>mode.width*7/12 and event.x<mode.width*8/12
            and event.y>mode.height*7/12 and event.y<mode.height*8/12):
            mode.app.color=mode.colorList[5]
        elif (event.x>mode.width*8/12 and event.x<mode.width*9/12
            and event.y>mode.height*7/12 and event.y<mode.height*8/12):
            mode.app.color=mode.colorList[6]
        elif (event.x>mode.width*9/12 and event.x<mode.width*10/12
            and event.y>mode.height*7/12 and event.y<mode.height*8/12):
            mode.app.color=mode.colorList[7]
        elif (event.x>mode.width*2/12 and event.x<mode.width*3/12
            and event.y>mode.height*8/12 and event.y<mode.height*9/12):
            mode.app.color=mode.colorList[8]
        elif (event.x>mode.width*3/12 and event.x<mode.width*4/12
            and event.y>mode.height*8/12 and event.y<mode.height*9/12):
            mode.app.color=mode.colorList[9]
        elif (event.x>mode.width*4/12 and event.x<mode.width*5/12
            and event.y>mode.height*8/12 and event.y<mode.height*9/12):
            mode.app.color=mode.colorList[10]
        elif (event.x>mode.width*5/12 and event.x<mode.width*6/12
            and event.y>mode.height*8/12 and event.y<mode.height*9/12):
            mode.app.color=mode.colorList[11]
        elif (event.x>mode.width*6/12 and event.x<mode.width*7/12
            and event.y>mode.height*8/12 and event.y<mode.height*9/12):
            mode.app.color=mode.colorList[12]
        elif (event.x>mode.width*7/12 and event.x<mode.width*8/12
            and event.y>mode.height*8/12 and event.y<mode.height*9/12):
            mode.app.color=mode.colorList[13]
        elif (event.x>mode.width*8/12 and event.x<mode.width*9/12
            and event.y>mode.height*8/12 and event.y<mode.height*9/12):
            mode.app.color=mode.colorList[14]
        elif (event.x>mode.width*9/12 and event.x<mode.width*10/12
            and event.y>mode.height*8/12 and event.y<mode.height*9/12):
            mode.app.color=mode.colorList[15]
        elif (event.x>mode.width*2/12 and event.x<mode.width*10/12
            and event.y>mode.height*6/12 and event.y<mode.height*7/12):
            mode.app.color=random.choice(mode.colorList)
        mode.app.setActiveMode(mode.app.levelSelection)

    #draws screen and possible color choices
    def redrawAll(mode, canvas):
        canvas.create_rectangle(0,0,mode.width, mode.height, fill='black')
        canvas.create_text(mode.width//2, mode.height*3/14,
                text='Choose your color theme',
                font='MSSerif 30 bold', fill='white')
        canvas.create_text(mode.width//2, mode.height*2/7,
                text='(click below)',
                font='MSSerif 15 bold', fill='white')     
        for cell in range(len(mode.colorList)//2):
            canvas.create_rectangle(mode.width*(cell+2)/12,mode.height*7/12,
                                mode.width*(cell+3)/12, mode.height*8/12,
                                outline='grey',fill=mode.colorList[cell])
            canvas.create_rectangle(mode.width*(cell+2)/12,mode.height*8/12,
                                mode.width*(cell+3)/12, mode.height*9/12,
                                outline='grey',fill=mode.colorList[cell+8])
        canvas.create_rectangle(mode.width*2/12,mode.height*6/12,
                            mode.width*10/12,mode.height*7/12,
                            outline='grey',fill=random.choice(mode.colorList))
        canvas.create_text(mode.width//2, mode.height*15/28,
                text='RANDOM',
                font='MSSerif 15 bold', fill='black')

#allows player to choose different levels(each maze generating algorithm is
# another level)
class LevelSelection(Mode):
    def mousePressed(mode, event):
        #easy-kruskal
        if (event.x>mode.width//12 and event.x<mode.width*3/12
            and event.y>mode.height*6/12 and event.y<mode.height*8/12):
            mode.app.level='easy'
            mode.app.setActiveMode(mode.app.kruskal2D)
            #medium-prim w/ less paths
        elif (event.x>mode.width*5/12 and event.x<mode.width*7/12
            and event.y>mode.height*6/12 and event.y<mode.height*8/12):
            mode.app.level='medium'
            mode.app.setActiveMode(mode.app.prim2D)
            #hard-prim w/ more paths
        elif (event.x>mode.width*9/12 and event.x<mode.width*11/12
            and event.y>mode.height*6/12 and event.y<mode.height*8/12):
            mode.app.level='hard'
            mode.app.setActiveMode(mode.app.prim2D)
        elif (event.x>mode.width*3/12 and event.x<mode.width*5/12
            and event.y>mode.height*9/12 and event.y<mode.height*11/12):
            mode.app.level='hard'
            mode.app.setActiveMode(mode.app.maze3D)
            #random
        elif (event.x>mode.width*7/12 and event.x<mode.width*9/12
            and event.y>mode.height*9/12 and event.y<mode.height*11/12):
            algList=[mode.app.kruskal2D,mode.app.prim2D,mode.app.maze3D]
            randomAlg=random.choice(algList)
            if randomAlg==mode.app.prim2D:
                mode.app.level=random.choice(['medium','hard'])
            mode.app.setActiveMode(randomAlg)

    #draws screen for player to make choice
    def redrawAll(mode, canvas):
        canvas.create_rectangle(0,0,mode.width, mode.height, fill='black')
        canvas.create_text(mode.width//2, mode.height*3/14,
                text='Choose the level of difficulty ahead',
                font='MSSerif 30 bold', fill='white')
        canvas.create_text(mode.width//2, mode.height*2/7,
                text='(click below)',
                font='MSSerif 15 bold', fill='white')
        canvas.create_rectangle(mode.width//12,mode.height*6/12,
                                mode.width*3/12, mode.height*8/12,
                                outline='red',fill='maroon')
        canvas.create_text(mode.width/6,mode.height*7/12,
                            text='easy',
                            font='MSSerif 20 bold', fill='white')
        canvas.create_rectangle(mode.width*5/12,mode.height*6/12,
                                mode.width*7/12, mode.height*8/12,
                                outline='red',fill='maroon')
        canvas.create_text(mode.width/2,mode.height*7/12,
                            text='medium',
                            font='MSSerif 20 bold', fill='white')
        canvas.create_rectangle(mode.width*9/12,mode.height*6/12,
                                mode.width*11/12, mode.height*8/12,
                                outline='red',fill='maroon')
        canvas.create_text(mode.width*5/6,mode.height*7/12,
                            text='hard',
                            font='MSSerif 20 bold', fill='white')
        canvas.create_rectangle(mode.width*3/12,mode.height*9/12,
                                mode.width*5/12, mode.height*11/12,
                                outline='red',fill='maroon')
        canvas.create_text(mode.width*4/12,mode.height*10/12,
                            text='3D',
                            font='MSSerif 20 bold', fill='white')
        canvas.create_rectangle(mode.width*7/12,mode.height*9/12,
                                mode.width*9/12, mode.height*11/12,
                                outline='red',fill='maroon')
        canvas.create_text(mode.width*8/12,mode.height*10/12,
                            text='RANDOM',
                            font='MSSerif 20 bold', fill='white')


#uses Prim's algorithm to generate maze: pick random point on grid 
# (represented by list that will be added to), picks a 
#random neighbor, and connects if neighbor is not already in list of the
#initial point (the list is untimately the path that will branch out)
class Prim2D(Mode):
    #initial variables, establishes initial board
    def appStarted(mode):
        #changes number of paths based on level selected
        if mode.app.level=='medium':
            mode.margin=mode.cellSize=60
        elif mode.app.level=='hard':
            mode.margin=mode.cellSize=30
        mode.cols=mode.rows=(mode.height-mode.margin*2)//mode.cellSize
        mode.subdivision=3
        mode.subcellSize=mode.cellSize/mode.subdivision
        theBoard=[]
        for row in range(mode.rows):
            colList=[]
            for col in range(mode.cols):
                subRowList=[]
                for subRow in range(mode.subdivision):
                    subColList=[]
                    for subCol in range(mode.subdivision):
                        subColList+=[mode.app.color]
                    subRowList+=[subColList]
                colList+=[subRowList]
            theBoard+=[colList]
        mode.Board=theBoard
        initialRow=random.randint(0,mode.rows-1)
        initialCol=random.randint(0,mode.cols-1)
        mode.points=[(initialRow,initialCol)]
        mode.pointDict={}
        mode.dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        mode.makePath()
        mode.ball=Ball(mode)
        mode.isGameOver=False
        mode.showInstructions=False

    #makes the randomly generated pathways based off of Prim's algorithm    
    def makePath(mode):
        #loops until all cells have been visited
        while len(mode.pointDict)<mode.rows*mode.cols:
            rowStep,colStep=random.choice(mode.dirs)
            randomRow,randomCol=random.choice(mode.points)
            newRow=randomRow+rowStep
            newCol=randomCol+colStep
            if ((newRow,newCol) not in mode.pointDict and
                newRow<mode.rows and newRow>-1 and
                newCol<mode.cols and newCol>-1):
                mode.points.append((newRow,newCol))
                if (randomRow,randomCol) in mode.pointDict:
                    mode.pointDict[(randomRow,randomCol)]+=[(newRow,newCol)]
                else:
                    mode.pointDict[(randomRow,randomCol)]=[(newRow,newCol)]
                mode.pointDict[(newRow,newCol)]=[(randomRow,randomCol)]
                if rowStep==1:
                    mode.Board[randomRow][randomCol][2][1]='white'
                    mode.Board[newRow][newCol][0][1]='white'
                elif rowStep==-1:
                    mode.Board[randomRow][randomCol][0][1]='white'
                    mode.Board[newRow][newCol][2][1]='white'
                elif colStep==1:
                    mode.Board[randomRow][randomCol][1][2]='white'
                    mode.Board[newRow][newCol][1][0]='white'
                elif colStep==-1:
                    mode.Board[randomRow][randomCol][1][0]='white'
                    mode.Board[newRow][newCol][1][2]='white'   
        for row,col in mode.points:
            mode.Board[row][col][1][1]='white'
        #makes start and end white
        mode.Board[0][0][1][0]='white'
        mode.Board[mode.rows-1][mode.cols-1][1][2]='white'

    #draws board
    def drawPrimMaze(mode,canvas):
        for row in range(len(mode.Board)):
            for col in range(len(mode.Board[0])):
                for subRow in range(len(mode.Board[0][0])):
                    for subCol in range(len(mode.Board[0][0][0])):
                        x0=(mode.margin+mode.cellSize*col+
                            mode.subcellSize*subCol)
                        x1=(mode.margin+mode.cellSize*col+
                            mode.subcellSize*(subCol+1))
                        y0=(mode.margin+mode.cellSize*row+
                            mode.subcellSize*subRow)
                        y1=(mode.margin+mode.cellSize*row+
                            mode.subcellSize*(subRow+1))
                        canvas.create_rectangle(x0,y0,x1,y1,
                        fill=mode.Board[row][col][subRow][subCol],
                        outline=mode.Board[row][col][subRow][subCol])
        canvas.create_text(mode.margin//2,mode.margin*3/2,
                            text='START', font=f'MSSerif {mode.cellSize*3//17}')
        canvas.create_text(mode.margin*3/2+mode.cellSize*mode.cols,
                            mode.margin//2+mode.cellSize*mode.rows,
                            text='END', font=f'MSSerif {mode.cellSize*3//17}')

    #allows player to move through maze                   
    def keyPressed(mode,event):
        #solves maze if player gives up
        if event.key=='s':
            mode.solveMaze()
        elif event.key=='i':
            mode.showInstructions=not mode.showInstructions
        mode.ball.keyPressed(mode,event)
        mode.gameOver()

    #checks if game over 
    def gameOver(mode):
        if (mode.ball.cx>=mode.cellSize*mode.rows+2*mode.subcellSize and 
            mode.ball.cy>=mode.cellSize*mode.cols+mode.subcellSize):
            mode.isGameOver=True

    #draws aspects on mode (prim maze, ball, game over screen if reached, etc.)
    def redrawAll(mode,canvas):
        mode.drawPrimMaze(canvas)
        mode.ball.redrawAll(mode,canvas)
        if mode.isGameOver==True:
            canvas.create_rectangle(0,mode.height/3,mode.width,mode.height*2/3,
            fill='black')
            canvas.create_text(mode.width//2,mode.height//2, 
            text='You Win!', font='MSSerif 30', fill='white')

        #shows instructions to player
        elif mode.showInstructions==True:
            instructionText='''
            Press the arrow keys to navigate.

            (in 3D mode, press 'Up' to move forward,
            'Down to move back, and the left and right
            arrow keys to change orientation)

            Press 'i' to see the instructions again.

            Press 's' to give up, I will light the way.

            Press 'c' for a change in your form.

            Good Luck.

            Press i to continue.
            '''
            canvas.create_rectangle(0,0,mode.width,mode.height,fill='black')
            canvas.create_text(mode.width//2,mode.height//2,
                    text=instructionText, fill='white', font='MSSerif 20')

    #provides solution to player
    def solveMaze(mode):
        (moves,solution)=mazeSolver(mode.rows).solve(mode)
        for (row,col) in moves:
            mode.Board[row][col][1][1]='yellow'
        mode.Board[0][0][1][1]='yellow'

#based off of Kruskal's algorithm: generates random pairs of cells and connects their centers 
# until all the cells are visited 
class Kruskal2D(Mode):
    #initial set up, sets up initial board and dimensions
    def appStarted(mode):
        mode.margin=mode.cellSize=60
        mode.rows=(mode.width-mode.margin*2)//mode.cellSize
        mode.cols=mode.numOfRows=(mode.width-mode.margin*2)//mode.cellSize
        mode.subdivision=3
        mode.subcellSize=mode.cellSize/mode.subdivision
        theBoard=[]
        for row in range(mode.rows):
            colList=[]
            for col in range(mode.cols):
                subRowList=[]
                for subRow in range(mode.subdivision):
                    subColList=[]
                    for subCol in range(mode.subdivision):
                        subColList+=['white']
                    subRowList+=[subColList]
                colList+=[subRowList]
            theBoard+=[colList]
        mode.Board=theBoard
        mode.dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        mode.makePath()
        mode.ball=Ball(mode)
        mode.isGameOver=False
        mode.showInstructions=False
        
    #makes path of a solvable maze
    def makePath(mode):
        mode.pointSet=set()
        mode.pointDict={}
        for row in range(len(mode.Board)):
            for col in range(len(mode.Board)):
                mode.pointDict[(row,col)]=[]
                if row!=len(mode.Board)-1:
                    mode.pointDict[(row,col)]+=[(row+1,col)]
                if row!=0:
                    mode.pointDict[(row,col)]+=[(row-1,col)]
                if col!=len(mode.Board)-1:
                    mode.pointDict[(row,col)]+=[(row,col+1)]
                if col!=0:
                    mode.pointDict[(row,col)]+=[(row,col-1)]
        while len(mode.pointSet)<mode.rows*mode.cols:
            row1=random.randint(0,mode.rows-1)
            col1=random.randint(0,mode.cols-1)
            rowStep,colStep=random.choice(mode.dirs)
            row2=row1+rowStep
            col2=col1+colStep
            if (((row1,col1) not in mode.pointSet or 
                (row2,col2) not in mode.pointSet) and
                row2<mode.rows and row2>-1 and
                col2<mode.cols and col2>-1):
                mode.pointSet.add((row1,col1))
                mode.pointSet.add((row2,col2))
                mode.pointDict[(row1,col1)].remove((row2,col2))
                mode.pointDict[(row2,col2)].remove((row1,col1))
                if rowStep==1:
                    mode.Board[row1][col1][2][1]=mode.app.color
                    mode.Board[row2][col2][0][1]=mode.app.color
                elif rowStep==-1:
                    mode.Board[row1][col1][0][1]=mode.app.color
                    mode.Board[row2][col2][2][1]=mode.app.color
                elif colStep==1:
                    mode.Board[row1][col1][1][2]=mode.app.color
                    mode.Board[row2][col2][1][0]=mode.app.color
                elif colStep==-1:
                    mode.Board[row1][col1][1][0]=mode.app.color
                    mode.Board[row2][col2][1][2]=mode.app.color
        for row,col in mode.pointSet:
            mode.Board[row][col][1][1]=mode.app.color

        #makes start and end white
        mode.Board[0][0][1][1]='white'
        mode.Board[0][0][1][2]='white'
        mode.Board[mode.rows-1][mode.cols-1][1][0]='white'
        mode.Board[mode.rows-1][mode.cols-1][1][1]='white'
        mode.Board[mode.rows-1][mode.cols-1][1][2]='white'

    #draws board
    def drawKruskalMaze(mode,canvas):
        for row in range(len(mode.Board)):
            for col in range(len(mode.Board[0])):
                for subRow in range(len(mode.Board[0][0])):
                    for subCol in range(len(mode.Board[0][0][0])):
                        x0=(mode.margin+mode.cellSize*col+
                            mode.subcellSize*subCol)
                        x1=(mode.margin+mode.cellSize*col+
                            mode.subcellSize*(subCol+1))
                        y0=(mode.margin+mode.cellSize*row+
                            mode.subcellSize*subRow)
                        y1=(mode.margin+mode.cellSize*row+
                            mode.subcellSize*(subRow+1))
                        canvas.create_rectangle(x0,y0,x1,y1,
                        fill=mode.Board[row][col][subRow][subCol],
                        outline=mode.Board[row][col][subRow][subCol])
        canvas.create_text(mode.margin//2,mode.margin*3/2,
                            text='START', font=f'MSSerif {mode.cellSize*3//17}')
        canvas.create_text(mode.margin*3/2+mode.cellSize*mode.cols,
                            mode.margin//2+mode.cellSize*mode.rows,
                            text='END', font=f'MSSerif {mode.cellSize*3//17}')

        
    #allows player to go through maze                 
    def keyPressed(mode,event):
        if event.key=='s':
            mode.solveMaze()
        elif event.key=='i':
            mode.showInstructions=not mode.showInstructions
        mode.ball.keyPressed(mode,event)
        mode.gameOver()

    #checks if game is over (if maze is solved)
    def gameOver(mode):
        if (mode.ball.cx>=mode.cellSize*mode.rows+2*mode.subcellSize and 
            mode.ball.cy>=mode.cellSize*mode.cols+mode.subcellSize):
            mode.isGameOver=True

    #draws kruskal maze and objects and game over when it is true
    def redrawAll(mode,canvas):
        mode.drawKruskalMaze(canvas)
        mode.ball.redrawAll(mode,canvas)
        if mode.isGameOver==True:
            canvas.create_rectangle(0,mode.height/3,mode.width,mode.height*2/3,
            fill='black')
            canvas.create_text(mode.width//2,mode.height//2, 
            text='You Win!', font='MSSerif 30', fill='white')

        #shows instructions to player
        elif mode.showInstructions==True:
            instructionText='''
            Press the arrow keys to navigate.

            (in 3D mode, press 'Up' to move forward,
            'Down to move back, and the left and right
            arrow keys to change orientation)

            Press 'i' to see the instructions again.

            Press 's' to give up, I will light the way.

            Press 'c' for a change in your form.

            Good Luck.
            
            Press i to continue.
            '''
            canvas.create_rectangle(0,0,mode.width,mode.height,fill='black')
            canvas.create_text(mode.width//2,mode.height//2,
                        text=instructionText, fill='white', font='MSSerif 20')
        
        #provides solution to player
    def solveMaze(mode):
        for row in range(mode.rows):
            mode.Board[row][0][2][0]='yellow'
            for col in range(mode.cols):
                mode.Board[mode.rows-1][col][2][2]='yellow'   

#object that represents player and allows them to go through maze
class Ball(object):
    #initial ball dimensions & position
    def __init__(self, mode):
        self.mode=mode
        self.cx=mode.margin+mode.subcellSize/2
        self.cy=mode.margin+mode.subcellSize*3/2
        self.r=mode.subcellSize/3
        self.dx=self.dy=mode.subcellSize
        mode.colorCount=0
        mode.colorList=['rosybrown','lightpink','coral','lightgreen',
                'cyan','lightblue','violet','plum','brown','red',
                'darkorange','green','blue','indigo','purple','black']
        self.fillColor='red'

    #gets row,col,subrow,subcol from xy coordinate position
    def getRowCol(self, mode):
        col=int((self.cx-mode.margin)/mode.cellSize)
        subCol=int(((self.cx-mode.margin)/mode.subcellSize)
                    -col*mode.subdivision)
        row=int((self.cy-mode.margin)/mode.cellSize)
        subRow=int(((self.cy-mode.margin)/mode.subcellSize)
                    -row*mode.subdivision)
        return (row, col, subRow, subCol)

    #sees if ball is allowed to move to certin position (in maze and on path)
    def legalMove(self,mode):
        if (self.cx>mode.margin and 
            self.cx<mode.margin+mode.cols*mode.cellSize-mode.subcellSize//3 and 
            self.cy>mode.margin and
            self.cy<mode.margin+mode.rows*mode.cellSize-mode.subcellSize//3):
            row,col,subRow,subCol=self.getRowCol(mode)
            if (mode.Board[row][col][subRow][subCol]=='white' or
                mode.Board[row][col][subRow][subCol]=='yellow'):
                return True
        return False

    #moves ball according to key press
    def keyPressed(self,mode,event):
        if event.key=='Right':
            self.cx+=self.dx
            if not self.legalMove(mode):self.cx-=self.dx
        elif event.key=='Left':
            self.cx-=self.dx
            if not self.legalMove(mode):self.cx+=self.dx
        elif event.key=='Down':
            self.cy+=self.dy
            if not self.legalMove(mode):self.cy-=self.dy
        elif event.key=='Up':
            self.cy-=self.dy
            if not self.legalMove(mode):self.cy+=self.dy
        elif event.key=='c':
            mode.colorCount+=1
            self.fillColor=mode.colorList[mode.colorCount%16]

    #draw ball
    def redrawAll(self,mode,canvas):
        canvas.create_oval(self.cx-self.r,self.cy-self.r, 
                        self.cx+self.r,self.cy+self.r, 
                        fill=self.fillColor)

#3D mode of maze: generates a simple maze and then makes 3D version
class Maze3D(Mode):
    #initial maze conditions for board and 3D maze
    def appStarted(mode):
        mode.margin=mode.cellSize=30
        mode.screen2Dx=mode.screen2Dy=mode.height//4
        mode.cols=mode.rows=(mode.screen2Dx-mode.margin*2)//mode.cellSize
        mode.subdivision=3
        mode.subcellSize=mode.cellSize/mode.subdivision
        theBoard=[]
        for row in range(mode.rows):
            colList=[]
            for col in range(mode.cols):
                subRowList=[]
                for subRow in range(mode.subdivision):
                    subColList=[]
                    for subCol in range(mode.subdivision):
                        subColList+=[mode.app.color]
                    subRowList+=[subColList]
                colList+=[subRowList]
            theBoard+=[colList]
        mode.Board=theBoard
        initialRow=random.randint(0,mode.rows-1)
        initialCol=random.randint(0,mode.cols-1)
        mode.points=[(initialRow,initialCol)]
        mode.pointDict={}
        mode.dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        mode.makePath()
        mode.showInstructions=False
        mode.x=0
        mode.y=0
        mode.orientations=['east','south','west','north']
        mode.presentOrientation='east'
        mode.initialBlock()
        mode.isGameOver=False
        mode.showInstructions=False

        #makes the randomly generated pathways based off of Prim's algorithm    
    def makePath(mode):
        #loops until all cells have been visited
        while len(mode.pointDict)<mode.rows*mode.cols:
            rowStep,colStep=random.choice(mode.dirs)
            randomRow,randomCol=random.choice(mode.points)
            newRow=randomRow+rowStep
            newCol=randomCol+colStep
            if ((newRow,newCol) not in mode.pointDict and
                newRow<mode.rows and newRow>-1 and
                newCol<mode.cols and newCol>-1):
                mode.points.append((newRow,newCol))
                if (randomRow,randomCol) in mode.pointDict:
                    mode.pointDict[(randomRow,randomCol)]+=[(newRow,newCol)]
                else:
                    mode.pointDict[(randomRow,randomCol)]=[(newRow,newCol)]
                mode.pointDict[(newRow,newCol)]=[(randomRow,randomCol)]
                if rowStep==1:
                    mode.Board[randomRow][randomCol][2][1]='white'
                    mode.Board[newRow][newCol][0][1]='white'
                elif rowStep==-1:
                    mode.Board[randomRow][randomCol][0][1]='white'
                    mode.Board[newRow][newCol][2][1]='white'
                elif colStep==1:
                    mode.Board[randomRow][randomCol][1][2]='white'
                    mode.Board[newRow][newCol][1][0]='white'
                elif colStep==-1:
                    mode.Board[randomRow][randomCol][1][0]='white'
                    mode.Board[newRow][newCol][1][2]='white'   
        for row,col in mode.points:
            mode.Board[row][col][1][1]='white'
        #makes start and end white
        mode.Board[0][0][1][0]='white'
        mode.Board[mode.rows-1][mode.cols-1][1][2]='white'
    
    #draws board
    def drawPrimMaze(mode,canvas):
        for row in range(len(mode.Board)):
            for col in range(len(mode.Board[0])):
                for subRow in range(len(mode.Board[0][0])):
                    for subCol in range(len(mode.Board[0][0][0])):
                        x0=(mode.margin/2+mode.cellSize*col+
                            mode.subcellSize*subCol)
                        x1=(mode.margin/2+mode.cellSize*col+
                            mode.subcellSize*(subCol+1))
                        y0=(mode.height*3/4+mode.margin+mode.cellSize*row+
                            mode.subcellSize*subRow)
                        y1=(mode.height*3/4+mode.margin+mode.cellSize*row+
                            mode.subcellSize*(subRow+1))
                        canvas.create_rectangle(x0,y0,x1,y1,
                        fill=mode.Board[row][col][subRow][subCol],
                        outline=mode.Board[row][col][subRow][subCol])
        if mode.app.color!='red':
            mode.Board[mode.y][mode.x][1][1]='red'
        else:
            mode.Board[mode.y][mode.x][1][1]='black'
        canvas.create_text(mode.margin/2,mode.height*3/4
                        +mode.margin+mode.subcellSize*3/2,
                        text='START',font=f'MSSerif {mode.cellSize*3//17}')
        canvas.create_text(mode.margin/2+mode.cols*mode.cellSize,
                        mode.height*3/4+mode.cellSize*mode.cols+mode.margin/2, 
                        text='END',font=f'MSSerif {mode.cellSize*3//17}')

    #draws compass next to 2D maze in lower left corner for player reference
    def drawCompass(mode,canvas):
        canvas.create_line(mode.margin/2+mode.cellSize*(mode.cols-1)*2, 
                        mode.height*3/4,
                        mode.margin/2+mode.cellSize*(mode.cols-1)*2, 
                        mode.height*3/4+mode.cellSize, width=3)
        canvas.create_text(mode.margin/2+mode.cellSize*(mode.cols-1)*2, 
                        mode.height*3/4-mode.subcellSize, text='N', fill='red')
        canvas.create_text(mode.margin/2+mode.cellSize*(mode.cols-1)*2, 
                        mode.height*3/4+mode.cellSize+mode.subcellSize, 
                        text='S', fill='red')
        canvas.create_line(mode.margin//2+mode.cellSize*mode.cols, 
                        mode.height*3/4+mode.cellSize//2,
                        mode.margin//2+mode.cellSize*(mode.cols+2), 
                        mode.height*3/4+mode.cellSize//2, width=3)
        canvas.create_text(mode.margin/2+mode.cellSize*(mode.cols+2)
                        +mode.subcellSize,mode.height*3/4+mode.cellSize//2, 
                        text='E', fill='red')
        canvas.create_text(mode.margin/2+mode.cellSize*mode.cols
                        -mode.subcellSize,mode.height*3/4+mode.cellSize//2, 
                        text='W', fill='red')

    #initial block setup                
    def initialBlock(mode):
        blockWidth=mode.width//3
        blockHeight=blockWidth
        yStart=mode.height//2
        mode.xVertex=[0,blockWidth,2*blockWidth,mode.width,
                        0,blockWidth,2*blockWidth,mode.width,
                        40,blockWidth+40,2*blockWidth-40,mode.width-40,
                        40,blockWidth+40,2*blockWidth-40,mode.width-40]
        mode.yVertex=[yStart-blockHeight,yStart-blockHeight,
                        yStart-blockHeight,yStart-blockHeight,
                        yStart,yStart,yStart,yStart,
                        yStart-blockHeight-40,yStart-blockHeight-40,
                        yStart-blockHeight-40,yStart-blockHeight-40,
                        yStart-40,yStart-40,yStart-40,yStart-40]
        mode.depth=mode.width//100
        mode.depthCount=0
        mode.findBlockColors()

    #finds colors for each of the blocks in the maze (and shows if player can
    # move to the next set of blocks or if there is a wall)
    def findBlockColors(mode):
        mode.nextBlock1Color='grey'
        mode.nextBlock2Color='grey'
        mode.nextBlock3Color='grey'
        #EAST
        if mode.presentOrientation=='east':
            mode.block1Color=mode.Board[mode.y][mode.x][0][2]
            mode.block2Color=mode.Board[mode.y][mode.x][1][2]
            mode.block3Color=mode.Board[mode.y][mode.x][2][2]
            if mode.x+1<len(mode.Board):
                mode.nextBlock1Color=mode.Board[mode.y][mode.x+1][0][0]
                mode.nextBlock2Color=mode.Board[mode.y][mode.x+1][1][0]
                mode.nextBlock3Color=mode.Board[mode.y][mode.x+1][2][0]
            else:
                mode.nextBlock2Color='white'
                mode.nextBlock3Color='white'
        #SOUTH      
        elif mode.presentOrientation=='south':
            mode.block1Color=mode.Board[mode.y][mode.x][2][0]
            mode.block2Color=mode.Board[mode.y][mode.x][2][1]
            mode.block3Color=mode.Board[mode.y][mode.x][2][2]
            if mode.y+1<len(mode.Board):
                mode.nextBlock1Color=mode.Board[mode.y+1][mode.x][0][0]
                mode.nextBlock2Color=mode.Board[mode.y+1][mode.x][0][1]
                mode.nextBlock3Color=mode.Board[mode.y+1][mode.x][0][2]
        #WEST
        elif mode.presentOrientation=='west':
            mode.block1Color=mode.Board[mode.y][mode.x][0][0]
            mode.block2Color=mode.Board[mode.y][mode.x][1][0]
            mode.block3Color=mode.Board[mode.y][mode.x][2][0]
            if mode.x-1>-1:
                mode.nextBlock1Color=mode.Board[mode.y][mode.x-1][0][2]
                mode.nextBlock2Color=mode.Board[mode.y][mode.x-1][1][2]
                mode.nextBlock3Color=mode.Board[mode.y][mode.x-1][2][2]
        #NORTH
        elif mode.presentOrientation=='north':
            mode.block1Color=mode.Board[mode.y][mode.x][0][0]
            mode.block2Color=mode.Board[mode.y][mode.x][0][1]
            mode.block3Color=mode.Board[mode.y][mode.x][0][2]
            if mode.y-1>-1:
                mode.nextBlock1Color=mode.Board[mode.y-1][mode.x][2][0]
                mode.nextBlock2Color=mode.Board[mode.y-1][mode.x][2][1]
                mode.nextBlock3Color=mode.Board[mode.y-1][mode.x][2][2]
    
    #provides solution to 2D maze in lower left corner
    def solveMaze(mode):
        (moves,solution)=mazeSolver(mode.rows).solve(mode)
        for (row,col) in moves:
            mode.Board[row][col][1][1]='yellow'
        mode.Board[0][0][1][1]='yellow'

    #actions based on keys pressed    
    def keyPressed(mode,event):
        #shows instructions
        if event.key=='i':
            mode.showInstructions=not mode.showInstructions
        #solves maze
        elif event.key=='s':
            mode.solveMaze()
        #sets orientation
        elif event.key=='Right':
            indexVal=(mode.orientations.index(mode.presentOrientation)+1)%4
            mode.presentOrientation=mode.orientations[indexVal]
            mode.initialBlock()
        elif event.key=='Left':
            indexVal=(mode.orientations.index(mode.presentOrientation)-1)%4
            mode.presentOrientation=mode.orientations[indexVal]
            mode.initialBlock()
        #sets depth
        elif event.key=="Up":
            mode.depthCount+=1
            if mode.depthCount<mode.depth:
                for index in range(0,len(mode.xVertex),2):
                    mode.xVertex[index]+=40
                    mode.xVertex[index+1]-=40
                for index in range(0,len(mode.xVertex),4):
                    mode.xVertex[index]-=160
                for index in range(3,len(mode.xVertex),4):
                    mode.xVertex[index]+=160
                for index in range(4):
                    mode.yVertex[index]-=40
                    mode.yVertex[index+len(mode.yVertex)//2]-=40
                for index in range(4):
                    mode.yVertex[index+4]+=40
                    mode.yVertex[index+4+len(mode.yVertex)//2]+=40
            elif mode.depthCount==mode.depth:
                if (mode.nextBlock2Color=='white'
                    and mode.nextBlock3Color!='white'):
                    mode.Board[mode.y][mode.x][1][1]='white'
                    if mode.presentOrientation=='east':
                        mode.x+=1
                    elif mode.presentOrientation=='south':
                        mode.y+=1
                    elif mode.presentOrientation=='west':
                        mode.x-=1
                    elif mode.presentOrientation=='north':
                        mode.y-=1
                    mode.initialBlock()
                if mode.app.color!='red':
                    mode.Board[mode.y][mode.x][1][1]='red'
                else:
                    mode.Board[mode.y][mode.x][1][1]='black'
            mode.gameOver()   
        elif event.key=="Down":
            mode.depthCount-=1
            if mode.depthCount>-1:
                for index in range(0,len(mode.xVertex),2):
                    mode.xVertex[index]-=40
                    mode.xVertex[index+1]+=40
                for index in range(0,len(mode.xVertex),4):
                    mode.xVertex[index]+=160
                for index in range(3,len(mode.xVertex),4):
                    mode.xVertex[index]-=160
                for index in range(4):
                    mode.yVertex[index]+=40
                    mode.yVertex[index+len(mode.yVertex)//2]+=40
                for index in range(4):
                    mode.yVertex[index+4]-=40
                    mode.yVertex[index+4+len(mode.yVertex)//2]-=40
            else:
                mode.depthCount=0 

    #draws cube based off of player position (sets up vertices)  
    def drawCube(mode,canvas):
        #wall
        canvas.create_polygon(mode.xVertex[8], mode.yVertex[8],
                            mode.xVertex[9], mode.yVertex[9],
                            mode.xVertex[13], mode.yVertex[13],
                            mode.xVertex[12], mode.yVertex[12], 
                            fill=mode.nextBlock1Color,outline='grey')
        canvas.create_polygon(mode.xVertex[10], mode.yVertex[10],
                            mode.xVertex[11], mode.yVertex[11],
                            mode.xVertex[15], mode.yVertex[15],
                            mode.xVertex[14], mode.yVertex[14], 
                            fill=mode.nextBlock3Color,outline='grey')
        canvas.create_polygon(mode.xVertex[9], mode.yVertex[9],
                            mode.xVertex[10], mode.yVertex[10],
                            mode.xVertex[14], mode.yVertex[14],
                            mode.xVertex[13], mode.yVertex[13], 
                            fill=mode.nextBlock2Color,outline='grey')

        #middle floor
        canvas.create_polygon(mode.xVertex[5], mode.yVertex[5],
                            mode.xVertex[6], mode.yVertex[6],
                            mode.xVertex[14], mode.yVertex[14],
                            mode.xVertex[13], mode.yVertex[13], 
                            fill=mode.block2Color,outline='grey')

        #left cube
        canvas.create_polygon(mode.xVertex[4], mode.yVertex[4],
                            mode.xVertex[12], mode.yVertex[12],
                            mode.xVertex[13], mode.yVertex[13],
                            mode.xVertex[5], mode.yVertex[5], 
                            fill=mode.block1Color,outline='grey')
        canvas.create_polygon(mode.xVertex[0], mode.yVertex[0],
                            mode.xVertex[8], mode.yVertex[8],
                            mode.xVertex[12], mode.yVertex[12],
                            mode.xVertex[4], mode.yVertex[4], 
                            fill=mode.block1Color,outline='grey')
        canvas.create_polygon(mode.xVertex[0], mode.yVertex[0],
                            mode.xVertex[8], mode.yVertex[8],
                            mode.xVertex[9], mode.yVertex[9],
                            mode.xVertex[1], mode.yVertex[1], 
                            fill=mode.block1Color,outline='grey')
        canvas.create_polygon(mode.xVertex[1], mode.yVertex[1],
                            mode.xVertex[9], mode.yVertex[9],
                            mode.xVertex[13], mode.yVertex[13],
                            mode.xVertex[5], mode.yVertex[5], 
                            fill=mode.block1Color,outline='grey')
        canvas.create_polygon(mode.xVertex[0], mode.yVertex[0],
                            mode.xVertex[1], mode.yVertex[1],
                            mode.xVertex[5], mode.yVertex[5],
                            mode.xVertex[4], mode.yVertex[4], 
                            fill=mode.block1Color,outline='grey')

        #right cube
        canvas.create_polygon(mode.xVertex[14], mode.yVertex[14],
                            mode.xVertex[15], mode.yVertex[15],
                            mode.xVertex[7], mode.yVertex[7],
                            mode.xVertex[6], mode.yVertex[6], 
                            fill=mode.block3Color,outline='grey')
        canvas.create_polygon(mode.xVertex[2], mode.yVertex[2],
                            mode.xVertex[10], mode.yVertex[10],
                            mode.xVertex[14], mode.yVertex[14],
                            mode.xVertex[6], mode.yVertex[6], 
                            fill=mode.block3Color,outline='grey')
        canvas.create_polygon(mode.xVertex[11], mode.yVertex[11],
                            mode.xVertex[3], mode.yVertex[3],
                            mode.xVertex[7], mode.yVertex[7],
                            mode.xVertex[15], mode.yVertex[15], 
                            fill=mode.block3Color,outline='grey')
        canvas.create_polygon(mode.xVertex[2], mode.yVertex[2],
                            mode.xVertex[10], mode.yVertex[10],
                            mode.xVertex[11], mode.yVertex[11],
                            mode.xVertex[3], mode.yVertex[3], 
                            fill=mode.block3Color,outline='grey')
        canvas.create_polygon(mode.xVertex[2], mode.yVertex[2],
                            mode.xVertex[3], mode.yVertex[3],
                            mode.xVertex[7], mode.yVertex[7],
                            mode.xVertex[6], mode.yVertex[6], 
                            fill=mode.block3Color,outline='grey')

        #front middle wall
        if mode.block2Color!='white':
            canvas.create_polygon(mode.xVertex[5], mode.yVertex[5],
                                mode.xVertex[6], mode.yVertex[6],
                                mode.xVertex[2], mode.yVertex[2],
                                mode.xVertex[1], mode.yVertex[1], 
                                fill=mode.block2Color,outline='grey')
            canvas.create_polygon(mode.xVertex[9], mode.yVertex[9],
                                mode.xVertex[10], mode.yVertex[10],
                                mode.xVertex[2], mode.yVertex[2],
                                mode.xVertex[1], mode.yVertex[1], 
                                fill=mode.block2Color,outline='grey')

    #makes game over true so page can be drawn
    def gameOver(mode):
        if (mode.presentOrientation=='east' and 
            mode.x==len(mode.Board)-1 and 
            mode.y==len(mode.Board)-1) and mode.depthCount>2:
            mode.isGameOver=True

    #draws all items on screen based on player's actions
    def redrawAll(mode,canvas):
        mode.drawCube(canvas)
        mode.drawPrimMaze(canvas)
        mode.drawCompass(canvas)
        canvas.create_text(mode.width*3/5, mode.height-50,
        text=f'Present Orientation: {mode.presentOrientation.upper()}',
        font='MSSerif 36')
        #shows game over screen
        if mode.isGameOver==True:
            canvas.create_rectangle(0,mode.height/3,mode.width,mode.height*2/3,
            fill='black')
            canvas.create_text(mode.width//2,mode.height//2, 
            text='You Win!', font='MSSerif 30', fill='white')
        #shows actions
        elif mode.showInstructions==True:
            instructionText='''
            Press the arrow keys to navigate.

            (in 3D mode, press 'Up' to move forward,
            'Down to move back, and the left and right
            arrow keys to change orientation)

            Press 'i' to see the instructions again.

            Press 's' to give up, I will light the way.

            Press 'c' for a change in your form.
            (Sadly, your form is not visible in 3D mode)

            Good Luck.

            Press i to continue.
            '''
            canvas.create_rectangle(0,0,mode.width,mode.height,fill='black')
            canvas.create_text(mode.width//2,mode.height//2,
                    text=instructionText, fill='white', font='MSSerif 20')

        
#BacktrackingPuzzleSolver and state class templates from: 
#http://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html
##############################################
# Generic backtracking-based puzzle solver
##############################################
class BacktrackingPuzzleSolver(object):
    def solve(self, mode, checkConstraints=True, printReport=False):
        self.moves = [ ]
        self.states = set()
        # If checkConstraints is False, then do not check the backtracking
        # constraints as we go (so instead do an exhaustive search)
        self.checkConstraints = checkConstraints
        # Be sure to set self.startArgs and self.startState in __init__
        self.startTime = time.time()
        self.solutionState = self.solveFromState(mode,self.startState)
        self.endTime = time.time()
        if (printReport): self.printReport()
        return (self.moves, self.solutionState)

    def printReport(self):
        print()
        print('***********************************')
        argsStr = str(self.startArgs).replace(',)',')') # remove singleton comma
        print(f'Report for {self.__class__.__name__}{argsStr}')
        print('checkConstraints:', self.checkConstraints)
        print('Moves:', self.moves)
        print('Solution state: ', end='')
        if ('\n' in str(self.solutionState)): print()
        print(self.solutionState)
        print('------------')
        print('Total states:', len(self.states))
        print('Total moves: ', len(self.moves))
        millis = int((self.endTime - self.startTime)*1000)
        print('Total time:  ', millis, 'ms')
        print('***********************************')

    def solveFromState(self, mode, state):
        if state in self.states:
            # we have already seen this state, so skip it
            return None
        self.states.add(state)
        if self.isSolutionState(state):
            # we found a solution, so return it!
            return state
        else:
            for move in self.getLegalMoves(state):
                # 1. Apply the move
                childState = self.doMove(state, move)
                # 2. Verify the move satisfies the backtracking constraints
                #    (only proceed if so)
                if ((self.stateSatisfiesConstraints(mode,childState)) or
                    (not self.checkConstraints)):
                    # 3. Add the move to our solution path (self.moves)
                    self.moves.append(move)
                    # 4. Try to recursively solve from this new state
                    result = self.solveFromState(mode,childState)
                    # 5. If we solved it, then return the solution!
                    if result != None:
                        return result
                    # 6. Else we did not solve it, so backtrack and
                    #    remove the move from the solution path (self.moves)
                    self.moves.pop()
            return None

    def __init__(self):
        pass

    def stateSatisfiesConstraints(self, state):
        # return True if the state satisfies the solution constraints so far
        raise NotImplementedError

    def isSolutionState(self, state):
        # return True if the state is a solution
        raise NotImplementedError

    def getLegalMoves(self, state):
        # return a list of the legal moves from this state (but not
        # taking the solution constraints into account)
        raise NotImplementedError

    def doMove(self, state, move):
        # return a new state that results from applying the given
        # move to the given state
        raise NotImplementedError

##############################################
# Generic State Class
##############################################
class State(object):
    def __eq__(self, other): 
        return (other != None) and self.__dict__ == other.__dict__
    def __hash__(self): 
        return hash(str(self.__dict__)) # hack but works even with lists
    def __repr__(self): 
        return str(self.__dict__)

#subclass of BacktracingPuzzleSolver, used as a template to create following 
#class that solves the randomly generated maze
class mazeSolver(BacktrackingPuzzleSolver):
    #initial conditions for maze solver
    def __init__(self,n):
        self.n=n
        self.startArgs=(n)
        self.startState=mazeState([(0,0)])

    #sees if path is valid (is on path and on board and can player move there)
    def stateSatisfiesConstraints(self, mode, state):
        row,col=state.pathPositionList[-1]
        pastRow,pastCol=state.pathPositionList[-2]
        if (row>=0 and row<self.n) and (col>=0 and col<self.n):
            if (row,col)in mode.pointDict[pastRow,pastCol]:
                    return True
        return False

    #sees if maze is solved and the path ends at lower right corner
    def isSolutionState(self, state):
        return (self.n-1,self.n-1)==state.pathPositionList[-1]

    #makes list of all posible directions maze could move in 
    def getLegalMoves(self, state):
        possibleDirs=[(1,0),(-1,0),(0,1),(0,-1)]
        (lastRow,lastCol)=state.pathPositionList[-1]
        possibleMoves=[]
        for row,col in possibleDirs:
            if (row+lastRow,col+lastCol) not in state.pathPositionList:
                possibleMoves.append((row+lastRow,col+lastCol))
        return possibleMoves

    #adds move to present state to return a new one
    def doMove(self, state, move):
        newPathPositionList=state.pathPositionList+[move]
        return mazeState(newPathPositionList)

#current state of maze used to solve maze in mazeSolver
class mazeState(State):
    def __init__(self,pathPositionList):
        self.pathPositionList=pathPositionList

#app class under which rest of game runs, has all the different modes and 
#overall variables
class Escape(ModalApp):
    def appStarted(app):
        app.level='medium'
        app.color='black'
        app.titleScreenMode=TitleScreenMode()
        app.chooseColor=ChooseColor()
        app.levelSelection=LevelSelection()
        app.introMode=IntroMode()
        app.kruskal2D=Kruskal2D()
        app.prim2D=Prim2D()
        app.maze3D=Maze3D()
        app.setActiveMode(app.titleScreenMode)

app=Escape(width=600, height=600)

