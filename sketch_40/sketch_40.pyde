def setup():
    size(500,500)
    smooth()
    background(50)
    strokeWeight(2)
    stroke(250)

cx = 250
cy = 250
cR = 200
counter = 0
mcolor = 0
def draw():
    global cx,cy,cR,counter,mcolor
    counter=counter+2*PI/255
    x1 = sin(counter)*cR+cx
    y1 = cos(counter)*cR+cy
    mcolor=mcolor+1
    stroke(mcolor)
    line(cx,cy,x1,y1)
    
    while counter > 2*PI:
        counter=0
        mccolor=0
        background(50)
    
def keyPressed():
    if key =="s":
        saveFrame("Photo")
