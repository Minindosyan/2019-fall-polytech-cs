def setup():
    size(500,500)
    smooth()
    background(235)
    strokeWeight(30)
    noLoop()
    
def draw():
    for i in range(1,8):
        stroke(20)
        line(i*50,200,150+(i-1)*50,300)
         