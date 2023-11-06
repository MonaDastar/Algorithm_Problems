# import turtle

# def turleStamp():
    
#     sc = turtle.Screen()
#     sc.bgcolor("darkblue")
#     tess = turtle.Turtle()
#     tess.shape("turtle")
#     tess.color("yellow")
#     tess.up()

#     distance = 5

#     for _ in range(50):
#         tess.stamp()
#         tess.forward(distance)
#         tess.right(24)
#         distance+=3
#     sc.exitonclick()
        
from PIL import Image

def image_play():
    img = Image.open("pic2.jpeg")
    width,height = img.size
    
    
    for row in range(0, img.height):
        for col in range(0,img.width):
            p = img.getpixel((col, row))
            
            newred = 255 - p[0]
            newgreen = 255 - p[1]
            newblue = 255 - p[2]
            
            newpixel =(newred, newgreen, newblue)
            
            img.putpixel((col,row),newpixel)
            
        
    img.show()
    
image_play()

