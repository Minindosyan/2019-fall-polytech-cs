def setup():
    size(500,500)
    smooth()
    strokeWeight(1)
    background(255)
i=0
k=1

def upDate():
    global i,k
    i = i + k
    if i==255:
        k=-1
    if i==0:
        k=1
        
def draw():
    global i,k
    stroke(i,20)
    myRandom = random(-100,100)
    myY1 = mouseY-myRandom
    myY2 = mouseY+myRandom
    line(0,myY1,500,myY2)
    upDate()
