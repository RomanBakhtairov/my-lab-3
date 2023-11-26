from tkinter import *
import random 
GAME_WIDTH =500
GAME_HIGHT =500
OVAL_RADIUS = 25
SPEED = 25
BACKGROUND_COLOR = "#FFFFFF"
FIRSTBALL_COLOR="#000000"
MAX_BALLS_COUNT = 5

class Ball:
    static_all_balls_keeper = []
    static_index_keeper = 0
    abs_of_max_local_speed = [0,0]
    count_of_entering_in_collision = 0
    def __init__(self,
                 start_coordinate,
                 speed_vector =  [0,0],
                 acceleration_vector= [0,2],
                 color = FIRSTBALL_COLOR,
                 radius = OVAL_RADIUS,
                 loss_ratio = 0.9):
        self.loss_ratio = loss_ratio
        self.static_all_balls_keeper.append(self)
        self.color = color
        self.radius = radius
        self.speed = speed_vector
        self.coordinates = start_coordinate
        self.acceleration = acceleration_vector
        self.tag = 'ball'+ str(Ball.static_index_keeper)
        Ball.static_index_keeper+= 1
        self.me =self.draw_oval(start_coordinate, self.radius,color,self.tag)

    def draw_oval(self,coords, radius,color,tag):
        x,y = coords
        return canvas.create_oval(x,y,x+radius,y + radius, fill = color, tag = tag)
    
    def redraw(self,new_coordinates):
        canvas.delete(self.tag)
        self.me = self.draw_oval(new_coordinates,self.radius,self.color,self.tag)

    def apply_acceleration(self):
        self.speed= [self.speed[0]+ self.acceleration[0], self.speed[1]+self.acceleration[1]]

    def local_reset_max_speed(self):
        nums = self.abs_of_max_local_speed
        self.abs_of_max_local_speed = [0,0]
        return nums 
    
    def calculate_speed_after_collision(self,loss_ratio  =0.9):
        self.count_of_entering_in_collision+=1
        returning_speed= [i*(loss_ratio) for i in self.local_reset_max_speed()]
        return returning_speed

    def apply_speed(self):
        self.coordinates= [self.speed[0]+ self.coordinates[0], self.speed[1]+self.coordinates[1]]
        #
        self.abs_of_max_local_speed[0] = max(abs(self.speed[0]), self.abs_of_max_local_speed[0])
        self.abs_of_max_local_speed[1] = max(abs(self.speed[1]), self.abs_of_max_local_speed[1])
def update(balls):
    for b in balls:
        b.apply_acceleration()
        b.apply_speed()
        on_collision_do(b)
        b.redraw(b.coordinates)
 #   print(Ball.static_index_keeper)
    window.after(SPEED,update,Ball.static_all_balls_keeper)



def on_collision_do(ball):
    GRAVITY_CHANGE_PROBABILITY = 1#из 100
    NEW_BALL_APPEARANCE_PROBABILITY = 1#из 100
#    SPEED_CHANGE_RANGE
    r = lambda: random.randint(0,255)#реализация генерации случайного цвета честным образом украдено со stackoverflow
    def create_new_ball(cords, speed, acceleration,color = '#%02X%02X%02X' % (r(),r(),r()), loss_ratio =random.randint(4,9)/10 ):
        if Ball.static_index_keeper < MAX_BALLS_COUNT:
            newball= Ball(cords, speed,acceleration,color= color,loss_ratio= loss_ratio)
    x,y = ball.coordinates
    x_speed,y_speed = ball.speed
    xacceleration, yacceleration = ball.acceleration
    will_newball_create = random.randint(0,10)
    minus_plus_alt = random.randint(0,10)
    if   x <0:
        new_speed = ball.calculate_speed_after_collision(ball.loss_ratio)
        ball.speed = [new_speed[0], y_speed]
        ball.coordinates = [x+OVAL_RADIUS,y]
#        will_newball_create<8  or create_new_ball([x+OVAL_RADIUS,y], [0,1],[0,(-1)**minus_plus_alt])  
    elif x>GAME_WIDTH:
        new_speed = ball.calculate_speed_after_collision(ball.loss_ratio)
        ball.speed = [ -new_speed[0], y_speed]
        ball.coordinates = [x-OVAL_RADIUS,y]
#        will_newball_create<8  or create_new_ball([x-OVAL_RADIUS,y], [0,-1],[0,(-1)**minus_plus_alt])  
    if y <0:
        new_speed = ball.calculate_speed_after_collision(ball.loss_ratio)
        ball.speed = [x_speed,new_speed[1]]
        ball.coordinates = [x,y+OVAL_RADIUS]
#        will_newball_create<8 or create_new_ball([x+10,y+OVAL_RADIUS+1], [1,0],[0,(-1)**minus_plus_alt])
    elif y>GAME_HIGHT:
        print(ball.abs_of_max_local_speed)
        new_speed = ball.calculate_speed_after_collision(ball.loss_ratio)
        ball.speed = [x_speed,-new_speed[1]]
        ball.coordinates = [x,y-OVAL_RADIUS*2]
        will_newball_create<8 or  create_new_ball([x+10,y-OVAL_RADIUS-30], [-minus_plus_alt*3,0],[0,(-1)**minus_plus_alt])


window = Tk()
window.resizable(False, False)
window.title('Physics simulation')
canvas = Canvas(window, bg = BACKGROUND_COLOR, height= GAME_HIGHT, width= GAME_WIDTH)
canvas.pack()
ball = Ball([GAME_WIDTH//2,GAME_HIGHT//2],speed_vector=[1,1])
def left(event):
    ball.speed[0]-=0.3
def right(event):
    ball.speed[0]+=0.3

window.bind('<Left>',left)
window.bind('<Right>', right)
update([ball])
window.mainloop()
