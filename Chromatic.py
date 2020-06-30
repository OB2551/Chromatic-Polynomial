from tkinter import *
import itertools
from Graph import *
import sympy
from io import BytesIO
from PIL import Image, ImageTk
import copy
import numpy as np



root = Tk() 
root.title('Chromatic Polynomial')
root.geometry('800x500')
i = 2
k = 0
s = 0


mincol = 0


root.configure(background = 'cyan')
count = Label(root, text = i, bg = 'cyan')
count.grid(row = 1, column = 28)

ChosenEdges = []
Vertices = [1,2]
PossibleEdges = [(1,2)]

#Label(root, text = "Chromatic Polynomial").grid(row = 0, column = 0)
Label(root, text = "Vertices:", fg = 'black', bg = 'cyan').grid(row = 1, column = 25, columnspan = 3)

displayEdge1 = Label(root, text = str(PossibleEdges[0][0]), font = 'Helvetica 12 bold', background = 'black', foreground = 'cyan')
displayEdge1.grid(row = 1, column = 16)
displayEdge1.config(height = 1, width = 2)

space= Label(root, text =  str('gg'), background = 'cyan', foreground = 'cyan')
space.grid(row = 1, column = 19)

displayEdge2 = Label(root, text = str(PossibleEdges[0][1]), font = 'Helvetica 12 bold',  background = 'black', foreground = 'pink')
displayEdge2.grid(row = 1, column = 17)
displayEdge2.config(height =1 , width = 2)

possibleEdgeLab = Label(root, text = "Possible Edges: " + str(len(PossibleEdges)), fg = 'black', bg = 'cyan')
possibleEdgeLab.grid(row = 7, column = 17, columnspan = 6)

chosenEdgeLab = Label(root, text = "Edges: " + str(len(ChosenEdges)), fg = 'black', bg = 'cyan')
chosenEdgeLab.grid(row = 8, column = 17, columnspan = 4)

choicesLeft = Label(root, text = "Choices Left: " + str(len(PossibleEdges)-k), fg= 'black', bg='cyan')
choicesLeft.grid(row = 6, column = 17, columnspan = 4 )

img_lbl = Label(root, text = '                               ', fg = 'black', bg = 'cyan')
img_lbl.grid(row = 12, column = 7, columnspan = 20)

edgeToBeAdded = Label(root, text = 'Add Edge:', fg= 'black', bg = 'cyan').grid(row = 1, column = 11, columnspan = 5)


def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
#draw circle
Canvas.create_circle = _create_circle
canvas = Canvas(root, width = 400, height = 400, bg = "black", highlightbackground = "cyan")
canvas.grid(row = 0, column = 0, rowspan = 10, columnspan = 10)
canvas.create_circle(20,200, 7.5, fill = 'cyan')
canvas.create_circle(380, 200, 7.5, fill = 'pink')
Dict = {}
VertCoords = {}
#Draws circle on black canvas
def drawCircles(canvas,x):
    global k
    global Vertices
    global Dict
    global Vertcoords
    R = 180
    canvas.delete("all")
    e = PossibleEdges[k]
    v1 = e[0]
    v2 = e[1]
    x1 = R*np.cos(v1*np.pi*2/len(Vertices))+200
    y1 = R*np.sin(v1*np.pi*2/len(Vertices))+200
    x2 = R*np.cos(v2*np.pi*2/len(Vertices))+200
    y2 = R*np.sin(v2*np.pi*2/len(Vertices))+200
    
    if x:
        canvas.create_circle(x1, y1, 7.5, fill = 'yellow')
        canvas.create_circle(x2, y2, 7.5, fill = 'yellow')
    else:
        canvas.create_circle(x1, y1, 7.5, fill = 'cyan')
        canvas.create_circle(x2, y2, 7.5, fill = 'pink')
    if x:
        Dict.clear()
    VertCoords[v1] = [x1, y1]
    VertCoords[v2] = [x2, y2]
    r = copy.deepcopy(Vertices)
    r.remove(v1)
    r.remove(v2)
    for j in r:
            x = R*np.cos(j*np.pi*2/len(Vertices))+200
            y = R*np.sin(j*np.pi*2/len(Vertices))+200
            canvas.create_circle(x, y, 7.5, fill = 'yellow')
            VertCoords[j] = [x, y]
              
        
def drawEdge(dictionary, canvas):
    global k
    x1 = dictionary[PossibleEdges[k][0]][0]
    y1 = dictionary[PossibleEdges[k][0]][1]
    x2 = dictionary[PossibleEdges[k][1]][0]
    y2 = dictionary[PossibleEdges[k][1]][1]
    canvas.create_line(x1, y1, x2, y2, fill = 'yellow', width = 1.5)
    
    
def drawEdges(dictionary, canvas):
    for v1, v2 in ChosenEdges:
        x1 = dictionary[v1][0]
        y1 = dictionary[v1][1]
        x2 = dictionary[v2][0]
        y2 = dictionary[v2][1]
        canvas.create_line(x1, y1, x2, y2, fill = 'yellow', width = 1.5)
        
        

def vertUp():
    
    global i
    global k
    global Vertices
    if i < 10:
       i +=1
       count.configure(text = i)
       global PossibleEdges
       newList = list(set(itertools.combinations(list(range(1,i+1)), 2))-set(PossibleEdges))
       PossibleEdges += newList
       PossibleEdges.sort()
       oldList = len(list(itertools.combinations(list(range(1,i)), 2)))
       if k== oldList:
           UpdateDisplayEdge(k)
       Vertices.append(i)
       possibleEdgeLab.configure(text = "Possible Edges: " + str(len(PossibleEdges)))
       drawCircles(canvas,False)
       drawEdges(VertCoords, canvas)
       choicesLeft.configure(text = "Choices Left: " + str(len(PossibleEdges)-len(ChosenEdges)-s))
    else:
      i = i

def vertDown():
    global i
    global k
    global Vertices
    if i > 2:
        i -= 1
        count.configure(text = i)
        global PossibleEdges
        x = copy.deepcopy(PossibleEdges)
        PossibleEdges.clear()
        Vertices = list(range(1, i+1))
        PossibleEdges = list(itertools.combinations(list(range(1,i+1)),2))
        r = copy.copy(k)
        
            

        possibleEdgeLab.configure(text = "Possible Edges: " + str(len(PossibleEdges)))
        removeEdge(x, PossibleEdges, ChosenEdges)
        if i != 2:
          if k>len(PossibleEdges)-1:
            UpdateDisplayEdge(len(PossibleEdges)-1)
            k = len(PossibleEdges)-1
            choicesLeft.configure(text = "Choices Left: 0")
            drawCircles(canvas,True)
            drawEdges(VertCoords, canvas)
            updateButtons()
          else:
            drawCircles(canvas, False)
            drawEdges(VertCoords, canvas)
            choicesLeft.configure(text = "Choices Left: "+str(len(PossibleEdges)-k))
        else:
          canvas.delete("all")
          canvas.create_circle(20, 200, 7.5, fill = 'pink')
          canvas.create_circle(380, 200, 7.5, fill = 'cyan')
          if r !=0:
           canvas.create_line(20, 200, 380, 200, fill = 'yellow')
           choicesLeft.configure(text = "Choices Left: 0" )
          else:
           choicesLeft.configure(text = "Choices Left: 1" )  
     
    else:
        i = i


    
def removeEdge(OldEdges, NewEdges, ChosenEdges):
    for edge in OldEdges:
        if edge not in NewEdges and edge in ChosenEdges:
            ChosenEdges.remove(edge)
    chosenEdgeLab.configure(text = "Edges: " + str(len(ChosenEdges)))    


def addEdge():
    global k
    if len(PossibleEdges)==1 and k<1:
        ChosenEdges.append(PossibleEdges[k])
        drawCircles(canvas, True)
        drawEdges(VertCoords, canvas)
        UpdateDisplayEdge2(k)
        k +=1
        choicesLeft.configure(text = "Choices Left: " + str(len(PossibleEdges)-k))  
        updateButtons()
        
    if k == len(PossibleEdges)-1 :
           UpdateDisplayEdge2(k)
           drawCircles(canvas, True)
           ChosenEdges.append(PossibleEdges[k])
           k += 1  
           drawEdges(VertCoords, canvas)
           choicesLeft.configure(text = "Choices Left: " + str(len(PossibleEdges)-k))
           
           updateButtons()
               
    if k < len(PossibleEdges)-1: 
             ChosenEdges.append(PossibleEdges[k])
             
             k+=1
             UpdateDisplayEdge(k)
             choicesLeft.configure(text = "Choices Left: " + str(len(PossibleEdges)-k))
             if str(len(PossibleEdges)-k) == 0:
                 drawCircles(canvas, True)
             else:
              drawCircles(canvas, False)
             drawEdges(VertCoords, canvas)
             
    chosenEdgeLab.configure(text = "Edges: " +str(len(list(set(ChosenEdges)))))
 
    
def updateButtons():
         calculateBut.configure(state = 'normal')
         vertButUp.configure(state = DISABLED)
         vertButDown.configure(state = DISABLED)
         edgeNo.configure(state = DISABLED)
         edgeYes.configure(state = DISABLED)
         chosenEdgeLab.configure(text = "Edges: " +str(len(list(set(ChosenEdges)))))    
         #Draw Edge
    
def skipEdge():
    global s
    global k
    s +=1
    if len(PossibleEdges)==1 and k<1:
        drawCircles(canvas, True)
        UpdateDisplayEdge2(k)
        k +=1
        choicesLeft.configure(text = "Choices Left: " + str(len(PossibleEdges)-k))
        updateButtons()
    if k == len(PossibleEdges)-1:
            UpdateDisplayEdge2(k)  
            drawCircles(canvas, True)
            drawEdges(VertCoords, canvas)
            k += 1
            choicesLeft.configure(text = "Choices Left: " + str(len(PossibleEdges)-k))
            
            calculateBut.configure(state = 'normal')
            vertButUp.configure(state = DISABLED)
            vertButDown.configure(state = DISABLED)
            edgeYes.configure(state = DISABLED)
            edgeNo.configure(state = DISABLED)
            chosenEdgeLab.configure(text = "Edges: " +str(len(list(set(ChosenEdges)))))
    
    if k < len(PossibleEdges)-1: 
             k+=1
             UpdateDisplayEdge(k)
             if str(len(PossibleEdges)-k) == 0:
                 drawCircles(canvas, True)
             else:
              drawCircles(canvas, False)
             drawEdges(VertCoords, canvas)
             choicesLeft.configure(text = "Choices Left: " + str(len(PossibleEdges)-k))
             
 
def UpdateDisplayEdge(k):
    displayEdge1.configure(text = str(PossibleEdges[k][0]), foreground = 'cyan')
    displayEdge2.configure(text = str(PossibleEdges[k][1]), foreground = 'pink')  
    
def UpdateDisplayEdge2(k):
    displayEdge1.configure(text = str(PossibleEdges[k][0]), foreground = 'yellow')
    displayEdge2.configure(text = str(PossibleEdges[k][1]), foreground = 'yellow')  
    
def Calculate():
    global mincol
    e = list(set(ChosenEdges))
    g = Graphs()
    g.setVertices(list(set(Vertices)))
    g.setEdges(e)
    
    x = g.chromaticPoly()
    chi = g.chi(x)
    
    mincol = Label(root, text = 'X(G)= ' + str(chi), bg = 'cyan')
    mincol.grid(row = 14, column = 14, columnspan = 6)
    obj = BytesIO()
    sympy.preview(x, viewer='BytesIO', output = 'png', outputbuffer=obj)
    obj.seek(0)
    img_lbl.img = ImageTk.PhotoImage(Image.open(obj))
    img_lbl.config(image=img_lbl.img)

    
  
    
def Clear():
    global Vertices
    global PossibleEdges
    global ChosenEdges
    global k
    global mincol
    k = 0
    global i
    i = 2
    global s
    s = 0
    Vertices = [1,2]
    PossibleEdges = [(1,2)]
    ChosenEdges = []
    UpdateDisplayEdge(k)
    possibleEdgeLab.configure(text = 'Possible Edges: ' + str(len(PossibleEdges)))
    chosenEdgeLab.configure(text = 'Edges: ' + str(len(ChosenEdges)))
    count.configure(text = len(Vertices))
    canvas.delete('all')
    drawCircles(canvas, False)
    img_lbl.configure(image = '')
    choicesLeft.configure(text = 'Choices Left: ' + str(len(PossibleEdges)-k))
    calculateBut.configure(state = DISABLED)
    vertButUp.configure(state = 'normal')
    vertButDown.configure(state = 'normal')
    edgeYes.configure(state = 'normal')
    edgeNo.configure(state= 'normal')
    if type(mincol) != int:
        mincol.destroy()
    
calculateBut = Button(root, command = Calculate, state = DISABLED, text = 'Calculate', bg = 'pink')
calculateBut.grid(row = 10, column = 0, columnspan = 5)
vertButUp = Button(root, command = vertUp, text = '>', bg = 'pink', fg = 'black')
vertButUp.grid(row = 2, column = 28, columnspan = 2)
vertButUp.config(height = 1, width = 4)
vertButDown = Button(root, command = vertDown, text = '<', bg = 'pink', fg = 'black')
vertButDown.grid(row = 2, column = 26, columnspan = 2)
vertButDown.config(height = 1, width = 4)
edgeYes = Button(root, command = addEdge, text = 'Yes', bg = 'pink', fg = 'black')
edgeYes.grid(row = 2, column = 16, columnspan = 2)
edgeYes.config(height = 1, width = 6)
edgeNo = Button(root, command = skipEdge, text = 'No', bg = 'pink', fg = 'black')
edgeNo.grid(row = 2, column =14, columnspan = 2)
edgeNo.config(height = 1, width = 6)
clearbut = Button(root, command = Clear, text = 'Clear Graph', bg = 'pink', fg = 'black')
clearbut.grid (row = 12, column = 0, columnspan = 5)


root.mainloop()