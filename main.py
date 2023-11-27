from tkinter import Tk, Canvas,Button
from random import randint
GAME_WIDTH =600
GAME_HIGHT =600
OVAL_RADIUS = 25
SPEED = 25
BACKGROUND_COLOR = "#FFFFFF"
FIRSTBALL_COLOR="#000000"
MAX_BALLS_COUNT = 10

class PhysicBall:
    #класс шарика
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
        self.static_all_balls_keeper.append(self)
        self.color = color
        self.radius = radius
        self.speed = speed_vector
        self.loss_ratio = loss_ratio
        self.coordinates = start_coordinate
        self.acceleration = acceleration_vector
        self.tag = 'ball'+ str(PhysicBall.static_index_keeper)
        #создаем унакальный для каждого шарика tag
        PhysicBall.static_index_keeper+= 1
        #
        self.me =self.draw_oval(start_coordinate, self.radius,color,self.tag)
        #отрисовываем шарик
        #
    def draw_oval(self,coords, radius,color,tag):
        x,y = coords
        return canvas.create_oval(x,y,x+radius,y + radius, fill = color, tag = tag)
    
    def redraw(self,new_coordinates):
        #рисует тотже шарик, но с учётом новых кординат
        canvas.delete(self.tag)
        self.me = self.draw_oval(new_coordinates,self.radius,self.color,self.tag)

    def apply_acceleration(self):
        #применить ускорение
        self.speed= [self.speed[0]+ self.acceleration[0], self.speed[1]+self.acceleration[1]]

    def local_reset_max_speed(self):
        #Обнулить записанную максимальную скорость
        nums = self.abs_of_max_local_speed
        self.abs_of_max_local_speed = [0,0]
        return nums 
    
    def calculate_speed_after_collision(self,loss_ratio  =0.9):
        #рассчёт скорости после удара(с учётом потерь)
        self.count_of_entering_in_collision+=1
        returning_speed= [i*(loss_ratio) for i in self.local_reset_max_speed()]
        return returning_speed

    def apply_speed(self):
        #применить скорость к кординатам + записать максимальную скорость между столкновениями
        self.coordinates= [self.speed[0]+ self.coordinates[0], self.speed[1]+self.coordinates[1]]
        #
        self.abs_of_max_local_speed[0] = max(abs(self.speed[0]), self.abs_of_max_local_speed[0])
        self.abs_of_max_local_speed[1] = max(abs(self.speed[1]), self.abs_of_max_local_speed[1])


def update(balls,blocker = True):
    #главный цикл игры
    for b in balls:
        b.apply_acceleration()
        b.apply_speed()
        on_collision_do(b)
        b.redraw(b.coordinates)
    window.after(SPEED,update,PhysicBall.static_all_balls_keeper)

def on_collision_do(ball):
    #создание ограничителя по бортикам.
    r = lambda: randint(0,255)
    #реализация генерации случайного цвета, честным образом украдено со stackoverflow
    def create_new_ball(cords, speed, acceleration,color = '#%02X%02X%02X' % (r(),r(),r()), loss_ratio =randint(4,9)/10 ):
        if PhysicBall.static_index_keeper < MAX_BALLS_COUNT:
            newball= PhysicBall(cords, speed,acceleration,color= color,loss_ratio= loss_ratio)
    x,y = ball.coordinates
    x_speed,y_speed = ball.speed
    will_newball_create = randint(0,10)
    if   x <0:
        new_speed = ball.calculate_speed_after_collision(ball.loss_ratio)
        ball.speed = [new_speed[0], y_speed]
        ball.coordinates = [x+OVAL_RADIUS,y]  
    elif x>GAME_WIDTH:
        new_speed = ball.calculate_speed_after_collision(ball.loss_ratio)
        ball.speed = [ -new_speed[0], y_speed]
        ball.coordinates = [x-OVAL_RADIUS,y]
    if y <0:
        new_speed = ball.calculate_speed_after_collision(ball.loss_ratio)
        ball.speed = [x_speed,new_speed[1]]
        ball.coordinates = [x,y+OVAL_RADIUS]
    elif y>GAME_HIGHT:
        new_speed = ball.calculate_speed_after_collision(ball.loss_ratio)
        ball.speed = [x_speed,-new_speed[1]]
        ball.coordinates = [x,y-OVAL_RADIUS*2]
        #
        radnom_y_speed, random_x_speed = randint(10,40),randint(10,40)
        will_newball_create<8 or  create_new_ball([x+10,y-OVAL_RADIUS-30], [-radnom_y_speed,random_x_speed],[0,1])


window = Tk()
window.resizable(False, False)
window.title('Physics simulation')
canvas = Canvas(window, bg = BACKGROUND_COLOR, height= GAME_HIGHT, width= GAME_WIDTH)
canvas.grid(column= 1,row=1)
ball = PhysicBall([GAME_WIDTH//2,GAME_HIGHT//2],speed_vector=[1,1])
B = Button(window, text ="Play", command = lambda:update([ball]))
B.grid(column=1,row = 0)

#Объявление всего самого важного



def left(event):
    ball.speed[0]-=0.4
def right(event):
    ball.speed[0]+=0.4
def down(event):
    ball.speed[1]+=20
window.bind('<Left>',left)
window.bind('<Right>', right)
window.bind('<Down>', down)
#добавление элементов управления


window.mainloop()
# конец)
