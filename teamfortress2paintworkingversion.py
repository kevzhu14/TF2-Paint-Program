#teamfortress2paintworkingversion.py
# A standard paint program featuring many common tools to create your own image.

from pygame import *
from random import *
from math import *
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

screen = display.set_mode((1024,768))

#for music
init()
mixer.music.load("songs/tf2song.mp3")
mixer.music.set_volume(0.5)
mixer.music.play(-1)

#for saving and loading
root = Tk()
root.withdraw()


#font and words setup
font.init()
arialblackFont = font.SysFont("Arial Black",35)
arialblacksmallFont = font.SysFont("Arial Black",20)
words = ["THE SNIPER","Pencil","Eraser","Brush","Highlighter","Spray Can","Line","Unfilled Rectangle","Filled Rectangle","Unfilled Ellipse","Filled Ellipse","Clear Canvas","Undo","Redo","Save","Load","Eyedropper"]


#generalpictures
backgroundpic=image.load("images/background.jpg")
screen.blit(backgroundpic,(0,0))
colourwheel=image.load("images/colourwheel.png")
screen.blit(colourwheel,(867,611))
tf2logo=image.load("images/tf2logo.png")
screen.blit(tf2logo,(5,50))
tf2emblem=image.load("images/tf2emblem.png")
screen.blit(tf2emblem,(225,125))

#icons for stamp rects
scoutstamp=image.load("images/scoutstamp.png")
soldierstamp=image.load("images/soldierstamp.png")
pyrostamp=image.load("images/pyrostamp.png")
demomanstamp=image.load("images/demomanstamp.png")
heavystamp=image.load("images/heavystamp.png")
engineerstamp=image.load("images/engineerstamp.png")
medicstamp=image.load("images/medicstamp.png")
sniperstamp=image.load("images/sniperstamp.png")
spystamp=image.load("images/spystamp.png")
scoutemblem=image.load("images/scoutemblem.png")
screen.blit(scoutemblem,(350,5))
soldieremblem=image.load("images/soldieremblem.png")
screen.blit(soldieremblem,(425,5))
pyroemblem=image.load("images/pyroemblem.png")
screen.blit(pyroemblem,(500,5))
demomanemblem=image.load("images/demomanemblem.png")
screen.blit(demomanemblem,(575,5))
heavyemblem=image.load("images/heavyemblem.png")
screen.blit(heavyemblem,(650,5))
engineeremblem=image.load("images/engineeremblem.png")
screen.blit(engineeremblem,(725,5))
medicemblem=image.load("images/medicemblem.png")
screen.blit(medicemblem,(800,5))
sniperemblem=image.load("images/sniperemblem.png")
screen.blit(sniperemblem,(875,5))
spyemblem=image.load("images/spyemblem.png")
screen.blit(spyemblem,(950,5))


#colour presets
colour=(0,0,0,255)
red=(255,0,0)
green=(0,255,0)
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
gray=(128,128,128)


#canvasdimensions
canvasRect = Rect(351,90,670,450)
canvasborderRect = Rect(349,89,672,452)

#drawingcanvas
draw.rect(screen,(255,255,255,),canvasRect)
draw.rect(screen,gray,canvasborderRect,2)


#toolselectionrectangles
pencilRect = Rect(350,550,53,52)
eraserRect = Rect(406,550,53,52)
brushRect = Rect(462,550,53,52)
highlighterRect = Rect(518,550,53,52)
spraycanRect = Rect(574,550,53,52)
lineRect= Rect(630,550,53,52)
unfilledrectangleRect = Rect(686,550,53,52)
filledrectangleRect = Rect(742,550,53,52)
unfilledellipseRect = Rect(798,550,53,52)
filledellipseRect = Rect(854,550,53,52)
eyedropperRect = Rect(910,550,53,52)
clearcanvasRect = Rect(966,550,53,52)
undoRect = Rect(350,604,53,52)
redoRect = Rect(406,604,53,52)
saveRect = Rect(462,604,53,52)
loadRect = Rect(518,604,53,52)

#stampselectrectangles
scoutstampRect = Rect(350,5,70,70)
soldierstampRect = Rect(425,5,70,70)
pyrostampRect = Rect(500,5,70,70)
demomanstampRect = Rect(575,5,70,70)
heavystampRect = Rect(650,5,70,70)
engineerstampRect = Rect(725,5,70,70)
medicstampRect = Rect(800,5,70,70)
sniperstampRect = Rect(875,5,70,70)
spystampRect = Rect(950,5,70,70)

#displaycolourRect
displaycolourRect = Rect(809,660,50,50)
displaycolourborderRect = Rect(808,659,52,52)

#pre-display (shows the size and colour of the lines/circles used for some shapes)
predisplayRect = Rect(575,606,226,160)
predisplayborderRect = Rect(574,605,228,162)
draw.rect(screen,white,predisplayborderRect)
draw.rect(screen,gray,predisplayRect)



#for lines and shapes
start = 0,0
size = 2


#lists for undo/redo
undolist=[]
redolist=[]


tool = "pencil"


running =True
while running:
    click = False
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
           if e.button == 1:
               back=screen.copy()   #screencopy
               start = e.pos
               click = True
           if e.button == 4:        #mousewheelcontrollingsize
               size += 1
           if e.button == 5:
               size -= 1
        if click:
            canvasversion = screen.subsurface(canvasRect).copy() #|saves pic of canvas and then adds it to the undolist whenever mouse is pressed 
            undolist.append(canvasversion)                       #|


    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()


    # for backgroundcharacter
    characternamePic = arialblackFont.render(words[0],True,white)
    screen.blit(characternamePic,(60,650))
    screen.blit(sniperemblem,(145,705))

    
    #for displaycolourRect
    draw.rect(screen,gray,displaycolourborderRect)
    draw.rect(screen,colour,displaycolourRect) 


    #colourwheel
    colourwheelborder=draw.rect(screen,white,(866,610,156,156),1)
    if colourwheelborder.collidepoint(mx,my) and mb[0]==1:
        colour=screen.get_at((mx,my))

    #highlightercolour   
    alphacolour=colour[:3]+(25,)


    #for highlighter 
    eraserHead = Surface((40,40),SRCALPHA)                  # make blank Surface
    draw.circle(eraserHead,(255,255,255,44),(20,20),size)     # draw using alpha
    brushHead = Surface((20,20),SRCALPHA)           
    draw.circle(brushHead,alphacolour,(10,10),size)
    if size<1:
        size=1 #avoiding negative radius
        

    #gray colour under toolrects 
    draw.rect(screen,gray,pencilRect,0)
    draw.rect(screen,gray,eraserRect,0)
    draw.rect(screen,gray,unfilledrectangleRect,0)
    draw.rect(screen,gray,clearcanvasRect,0)
    draw.rect(screen,gray,unfilledellipseRect,0)
    draw.rect(screen,gray,lineRect,0)
    draw.rect(screen,gray,highlighterRect,0)
    draw.rect(screen,gray,filledrectangleRect,0)
    draw.rect(screen,gray,filledellipseRect,0)
    draw.rect(screen,gray,spraycanRect,0)
    draw.rect(screen,gray,eyedropperRect,0)
    draw.rect(screen,gray,brushRect,0)
    draw.rect(screen,gray,undoRect,0)
    draw.rect(screen,gray,redoRect,0)
    draw.rect(screen,gray,saveRect,0)
    draw.rect(screen,gray,loadRect,0)

    #icons for tool rects (this part of code goes after "graycolour under toolrects" to have the images appear on top
    pencilicon=image.load("images/pencilicon.png")
    screen.blit(pencilicon,(353,552))
    erasericon=image.load("images/erasericon.png")
    screen.blit(erasericon,(409,552))
    brushicon=image.load("images/brushicon.png")
    screen.blit(brushicon,(465,552))
    highlightericon=image.load("images/highlightericon.png")
    screen.blit(highlightericon,(521,552))
    spraypainticon=image.load("images/spraypainticon.png")
    screen.blit(spraypainticon,(577,552))
    lineicon=image.load("images/lineicon.png")
    screen.blit(lineicon,(633,552))
    unfilledrecticon=image.load("images/unfilledrectangleicon.png")
    screen.blit(unfilledrecticon,(689,552))
    filledrecticon=image.load("images/filledrectangleicon.png")
    screen.blit(filledrecticon,(745,552))
    unfilledellipseicon=image.load("images/unfilledellipseicon.png")
    screen.blit(unfilledellipseicon,(801,552))
    filledellipseicon=image.load("images/filledellipseicon.png")
    screen.blit(filledellipseicon,(857,552))
    eyedroppericon=image.load("images/eyedroppericon.png")
    screen.blit(eyedroppericon,(913,552))
    clearcanvasicon=image.load("images/clearcanvasicon.png")
    screen.blit(clearcanvasicon,(969,552))
    undoicon=image.load("images/undoicon.png")
    screen.blit(undoicon,(353,606))
    redoicon=image.load("images/redoicon.png")
    screen.blit(redoicon,(414,611))
    saveicon=image.load("images/saveicon.png")
    screen.blit(saveicon,(465,608))
    loadicon=image.load("images/loadicon.png")
    screen.blit(loadicon,(521,606))

       
    #toolhighlights
    draw.rect(screen,white,pencilRect,2)
    draw.rect(screen,white,eraserRect,2)
    draw.rect(screen,white,unfilledrectangleRect,2)
    draw.rect(screen,white,clearcanvasRect,2)
    draw.rect(screen,white,unfilledellipseRect,2)
    draw.rect(screen,white,lineRect,2)
    draw.rect(screen,white,highlighterRect,2)
    draw.rect(screen,white,filledrectangleRect,2)
    draw.rect(screen,white,filledellipseRect,2)
    draw.rect(screen,white,spraycanRect,2)
    draw.rect(screen,white,eyedropperRect,2)
    draw.rect(screen,white,brushRect,2)
    draw.rect(screen,white,undoRect,2)
    draw.rect(screen,white,redoRect,2)
    draw.rect(screen,white,saveRect,2)
    draw.rect(screen,white,loadRect,2)

    #stamp toolhighlights
    draw.rect(screen,white,scoutstampRect,2)
    draw.rect(screen,white,soldierstampRect,2)
    draw.rect(screen,white,pyrostampRect,2)
    draw.rect(screen,white,demomanstampRect,2)
    draw.rect(screen,white,heavystampRect,2)
    draw.rect(screen,white,engineerstampRect,2)
    draw.rect(screen,white,medicstampRect,2)
    draw.rect(screen,white,sniperstampRect,2)
    draw.rect(screen,white,spystampRect,2)

 

    
    #preventgoingoffthecanvas
    if mb[0]==1 and (canvasRect.collidepoint(mx,my) or canvasRect.collidepoint(omx,omy)): #prevents your tool from drawing out of the canvas by limiting boundaries
        screen.set_clip(canvasRect)

        
    # hover highlight over tools and tool select(some instantly use the tool when pressed) 
    if pencilRect.collidepoint(mx,my):
        draw.rect(screen,red,pencilRect,2)
        if mb[0]==1:
            tool = "pencil"
                        
    if eraserRect.collidepoint(mx,my):
        draw.rect(screen,blue,eraserRect,2)
        if mb[0]==1:
            tool = "eraser"
            if size<1:
                size=1
    if unfilledrectangleRect.collidepoint(mx,my):
        draw.rect(screen,red,unfilledrectangleRect,2)
        if mb[0]==1:
            tool = "unfilledrectangle"
    if clearcanvasRect.collidepoint(mx,my):  
        draw.rect(screen,blue,clearcanvasRect,2)
        if mb[0]==1:
            tool = "clearcanvas"
            draw.rect(screen,white,canvasRect)
    if unfilledellipseRect.collidepoint(mx,my):
        draw.rect(screen,red,unfilledellipseRect,2)
        if mb[0]==1:
            tool = "unfilledellipse"
    if lineRect.collidepoint(mx,my):
        draw.rect(screen,blue,lineRect,2)
        if mb[0]==1:
            tool = "line"
    if highlighterRect.collidepoint(mx,my):
        draw.rect(screen,blue,highlighterRect,2)
        if mb[0]==1:
            tool = "highlighter"
    if filledrectangleRect.collidepoint(mx,my):
        draw.rect(screen,blue,filledrectangleRect,2)
        if mb[0]==1:
            tool = "filledrectangle"
    if filledellipseRect.collidepoint(mx,my):
        draw.rect(screen,blue,filledellipseRect,2)
        if mb[0]==1:
            tool = "filledellipse"
    if spraycanRect.collidepoint(mx,my):
        draw.rect(screen,red,spraycanRect,2)
        if mb[0]==1:
            tool = "spraycan"
    if eyedropperRect.collidepoint(mx,my):
        draw.rect(screen,red,eyedropperRect,2)
        if mb[0]==1:
            tool = "eyedropper"
    if brushRect.collidepoint(mx,my):
        draw.rect(screen,red,brushRect,2)
        if mb[0]==1:
            tool = "brush"
    if undoRect.collidepoint(mx,my):
        draw.rect(screen,red,undoRect,2)
        if mb[0]==1:
            tool = "undo"
            if len(undolist)>1:  #needs more than version of canvas to revert a change
                redolist.append(undolist[-1]) #adds the most recently added canvas version to undo to the redolist for future re-doing
                undolist.remove(undolist[-1]) #removes that most recent version of canvas from undolist as a result 
                screen.blit(undolist[-1],(351,90)) #blit a reverted screenshot of canvas
    if redoRect.collidepoint(mx,my):
        draw.rect(screen,blue,redoRect,2)
        if mb[0]==1:
            tool = "redo"
            if len(redolist)>0: #needs just at least 1 version of canvas to redo a change
                screen.blit(redolist[-1],(351,90)) #blits most recent version of canvas in the redolist
                undolist.append(redolist[-1]) #removes the version used to redo from the undolist
                redolist.remove(redolist[-1]) #removes the recently redo version that was blit from the redolist
    if saveRect.collidepoint(mx,my):
        draw.rect(screen,red,saveRect,2)
        if click:
           result = asksaveasfilename()
           if result != "":
               image.save(screen.subsurface(canvasRect),result+".jpg")
    if loadRect.collidepoint(mx,my):
        draw.rect(screen,blue,loadRect,2)
        if click:
            result = askopenfilename(filetypes = [("Picture files","*.jpg")])
            load=image.load(result)
            screen.blit(load,(351,90))



    #for predisplay (displays a word of what tool is currently selected)
    if clearcanvasRect.collidepoint(mx,my):
       draw.rect(screen,gray,predisplayRect)
       clearcanvastxtPic = arialblacksmallFont.render(words[11],True,white)
       screen.blit(clearcanvastxtPic,(620,600))

    if undoRect.collidepoint(mx,my):
       draw.rect(screen,gray,predisplayRect)
       undotxtPic = arialblacksmallFont.render(words[12],True,white)
       screen.blit(undotxtPic,(650,600))

    if redoRect.collidepoint(mx,my):
       draw.rect(screen,gray,predisplayRect)
       redotxtPic = arialblacksmallFont.render(words[13],True,white)
       screen.blit(redotxtPic,(650,600))

    if saveRect.collidepoint(mx,my):
       draw.rect(screen,gray,predisplayRect)
       savetxtPic = arialblacksmallFont.render(words[14],True,white)
       screen.blit(savetxtPic,(650,600))

    if loadRect.collidepoint(mx,my):
       draw.rect(screen,gray,predisplayRect)
       loadtxtPic = arialblacksmallFont.render(words[15],True,white)
       screen.blit(loadtxtPic,(650,600))
           
    if tool == "filledrectangle":
        draw.rect(screen,gray,predisplayRect)
        filledrectangletxtPic = arialblacksmallFont.render(words[8],True,white)
        screen.blit(filledrectangletxtPic,(600,600))

    if tool == "filledellipse":
        draw.rect(screen,gray,predisplayRect)
        filledellipsetxtPic = arialblacksmallFont.render(words[10],True,white)
        screen.blit(filledellipsetxtPic,(620,600))

    if tool == "filledrectangle":
        draw.rect(screen,gray,predisplayRect)
        filledrectangletxtPic = arialblacksmallFont.render(words[8],True,white)
        screen.blit(filledrectangletxtPic,(600,600))
                
    if tool == "eraser":
        draw.rect(screen,gray,predisplayRect)
        draw.circle(screen,colour,(688,686),size)
        erasertxtPic = arialblacksmallFont.render(words[2],True,white)
        screen.blit(erasertxtPic,(655,600))

    if tool == "brush": 
        draw.rect(screen,gray,predisplayRect)
        draw.circle(screen,colour,(688,686),size)
        brushtxtPic = arialblacksmallFont.render(words[3],True,white)
        screen.blit(brushtxtPic,(655,600))

    if tool == "eyedropper": 
        draw.rect(screen,gray,predisplayRect)
        draw.circle(screen,colour,(688,686),size)
        eyedroppertxtPic = arialblacksmallFont.render(words[16],True,white)
        screen.blit(eyedroppertxtPic,(630,600))

    if tool == "spraycan": 
        draw.rect(screen,gray,predisplayRect)
        draw.circle(screen,colour,(688,686),size)
        spraycantxtPic = arialblacksmallFont.render(words[5],True,white)
        screen.blit(spraycantxtPic,(630,600))

    if tool == "highlighter": 
        draw.rect(screen,gray,predisplayRect)
        draw.circle(screen,colour,(688,686),size)
        highlightertxtPic = arialblacksmallFont.render(words[4],True,white)
        screen.blit(highlightertxtPic,(630,600))

    if tool == "pencil": 
        draw.rect(screen,gray,predisplayRect)
        draw.line(screen,colour,(580,686),(795,686),size)
        penciltxtPic = arialblacksmallFont.render(words[1],True,white)
        screen.blit(penciltxtPic,(655,600))

    if tool == "line": 
        draw.rect(screen,gray,predisplayRect)
        draw.line(screen,colour,(580,686),(795,686),size)
        linetxtPic = arialblacksmallFont.render(words[6],True,white)
        screen.blit(linetxtPic,(665,600))

    if tool == "unfilledrectangle": 
        draw.rect(screen,gray,predisplayRect)
        draw.line(screen,colour,(580,686),(795,686),size)
        unfilledrectangletxtPic = arialblacksmallFont.render(words[7],True,white)
        screen.blit(unfilledrectangletxtPic,(590,600))

    if tool == "unfilledellipse": 
        draw.rect(screen,gray,predisplayRect)
        draw.line(screen,colour,(580,686),(795,686),size)
        unfilledellipsetxtPic = arialblacksmallFont.render(words[9],True,white)
        screen.blit(unfilledellipsetxtPic,(605,600))

    
        
   
    #stamp hover/select and blitting
    if scoutstampRect.collidepoint(mx,my):
        draw.rect(screen,blue,scoutstampRect,2)
        if mb[0]==1:
            tool = "scoutstamp"
    if soldierstampRect.collidepoint(mx,my):
        draw.rect(screen,red,soldierstampRect,2)
        if mb[0]==1:
            tool = "soldierstamp"
    if pyrostampRect.collidepoint(mx,my):
        draw.rect(screen,blue,pyrostampRect,2)
        if mb[0]==1:
            tool = "pyrostamp"
    if demomanstampRect.collidepoint(mx,my):
        draw.rect(screen,red,demomanstampRect,2)
        if mb[0]==1:
            tool = "demomanstamp"
    if heavystampRect.collidepoint(mx,my):
        draw.rect(screen,blue,heavystampRect,2)
        if mb[0]==1:
            tool = "heavystamp"
    if engineerstampRect.collidepoint(mx,my):
        draw.rect(screen,red,engineerstampRect,2)
        if mb[0]==1:
            tool = "engineerstamp"
    if medicstampRect.collidepoint(mx,my):
        draw.rect(screen,blue,medicstampRect,2)
        if mb[0]==1:
            tool = "medicstamp"
    if sniperstampRect.collidepoint(mx,my):
        draw.rect(screen,red,sniperstampRect,2)
        if mb[0]==1:
            tool = "sniperstamp"
    if spystampRect.collidepoint(mx,my):
        draw.rect(screen,blue,spystampRect,2)
        if mb[0]==1:
            tool = "spystamp"
    
    
    #most of toolcodes #(some are up top where they were executed immediately)
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        if tool == "pencil":
            draw.line(screen,colour,(omx,omy),(mx,my),size-1)

        if tool == "brush":
            draw.circle(screen,colour,(mx,my),size+9)
            if size<1:
                size=1
                
        if tool == "eraser":
            draw.circle(screen,white,(mx,my),size+9)
            
        if tool == "unfilledrectangle":
            screen.blit(back,(0,0))
            draw.rect(screen,colour,(start[0],start[1],mx-start[0],my-start[1]),size)
            
        if tool == "line":
            screen.blit(back,(0,0))
            draw.line(screen,colour,start,(mx,my),size)

        if tool == "highlighter":
            if mx!=omx or my!=omy:
                if mb[0]==1:
                    screen.blit(brushHead, (mx-10,my-10))  # this is where it uses the alpha
                    if mb[2]==1:
                        screen.blit(eraserHead, (mx-20,my-20))

        if tool == "filledrectangle":
            screen.blit(back,(0,0))
            draw.rect(screen,colour,(start[0],start[1],mx-start[0],my-start[1]),0)

        if tool == "unfilledellipse":
            screen.blit(back,(0,0))
            drawnunfilledellipseRect=Rect(start[0],start[1],mx-start[0],my-start[1])

            drawnunfilledellipseRect.normalize() #makes sure that radius isnt negative
            try:
                draw.ellipse(screen,colour,drawnunfilledellipseRect,size)
                
            except:
                draw.ellipse(screen,colour,drawnunfilledellipseRect,0) #when the radius is so small and it looks like a filledellipse
            
        if tool == "filledellipse":
            screen.blit(back,(0,0))
            drawnfilledellipseRect=Rect(start[0],start[1],mx-start[0],my-start[1])

            drawnfilledellipseRect.normalize()
            try:
                draw.ellipse(screen,colour,drawnfilledellipseRect,0)
                
            except:
                draw.ellipse(screen,colour,drawnfilledellipseRect,0)

        spraycanx=randint(-size,size)
        spraycany=randint(-size,size) #the limit the spraypaint draws the tiny circles
        if tool == "spraycan":
            if hypot(spraycanx,spraycany)<size: #has to be within the size of the spraycircle
                draw.circle(screen,colour,(mx+spraycanx,my+spraycany),1,1)

        if tool == "eyedropper":
            colour=screen.get_at((mx,my))


        if tool == "scoutstamp":
            screen.blit(back,(0,0))
            screen.blit(scoutstamp,(mx-350,my-250))

        if tool == "soldierstamp":
            screen.blit(back,(0,0))
            screen.blit(soldierstamp,(mx-330,my-250))

        if tool == "pyrostamp":
            screen.blit(back,(0,0))
            screen.blit(pyrostamp,(mx-330,my-250))

        if tool == "demomanstamp":
            screen.blit(back,(0,0))
            screen.blit(demomanstamp,(mx-340,my-250))

        if tool == "heavystamp":
            screen.blit(back,(0,0))
            screen.blit(heavystamp,(mx-340,my-250))

        if tool == "engineerstamp":
            screen.blit(back,(0,0))
            screen.blit(engineerstamp,(mx-330,my-250))

        if tool == "medicstamp":
            screen.blit(back,(0,0))
            screen.blit(medicstamp,(mx-340,my-250))

        if tool == "sniperstamp":
            screen.blit(back,(0,0))
            screen.blit(sniperstamp,(mx-340,my-250))

        if tool == "spystamp":
            screen.blit(back,(0,0))
            screen.blit(spystamp,(mx-340,my-250))   

    
    screen.set_clip(None)

    omx,omy = mx,my

    
    display.flip()


quit()
