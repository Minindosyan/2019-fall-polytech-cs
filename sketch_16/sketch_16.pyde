def setup ():
    size(2000, 500)
    smooth()
    background(255)
    strokeWeight(30)
def draw ():
    for i in range(1,4):
        stroke(20)
        line(i*50, 200, 150 + (i-1)*50, 300)
    
         
