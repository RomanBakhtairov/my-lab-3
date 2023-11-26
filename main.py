import random
r = lambda: random.randint(0,255)
print('#%02X%02X%02X' % (r(),r(),r()))



# from tkinter import *
# import random 
# GAME_WIDTH =500
# GAME_HIGHT =500
# OVAL_RADIUS = 25
# SPEED = 10
# BACKGROUND_COLOR = "#FFFFFF"
# FIRSTBALL_COLOR ="#000000"

# class Ball:
#     def __init__(self,speed = [0,1] ) -> None:
#         x = GAME_WIDTH/2
#         y = GAME_HIGHT//2
#         self.coordinates = [x,y]
#         self.speed = [0,1]
#         self.acceleration = [0,1]
#         self.me = canvas.create_oval(x,y, x+OVAL_RADIUS, y +OVAL_RADIUS,fill= FIRSTBALL_COLOR, tag = 'ball')


# def game_update(ball):
#     ball.speed =  [ball.acceleration[0] + ball.speed[0], ball.acceleration[1] + ball.speed[1]]
#     ball.coordinates = [ball.coordinates[0] + ball.speed[0], ball.coordinates[1] + ball.speed[1]]
#     print(ball.coordinates)
#     x , y = ball.coordinates[0], ball.coordinates[1]
   
#     canvas.delete('ball')
#     newball = canvas.create_oval( x,y,x+OVAL_RADIUS, y + OVAL_RADIUS, fill= FIRSTBALL_COLOR,tag = 'ball')
#     window.after(SPEED, game_update,ball)
# def check_collisions(ball):
#     pass
    
# def game_over():
#     pass




# window = Tk()
# window.title('Physics simulation')
# window.resizable(False, False)
# canvas = Canvas(window, bg = BACKGROUND_COLOR, height= GAME_HIGHT, width= GAME_WIDTH)
# canvas.pack()
# ball = Ball()


# game_update(ball)

# window.mainloop()
