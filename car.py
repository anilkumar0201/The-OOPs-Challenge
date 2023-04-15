class car:
    def __init__(self,make,model,year,speed,x,y):
        self.make=make
        self.model=model
        self.year=year
        self.speed=speed
        self.x=x
        self.y=y
    def accelerate(self,speed_increment):
        self.speed=self.speed+speed_increment
    def brake(self,speed_decrement):
        self.speed=self.speed-speed_decrement
    def move(self):
        self.x=self.x+self.speed
        self.y=self.x+self.speed
    def detect_collision(self,c):
        if ((self.x==c.x) & (self.y==c.y)):
            return True
        else:
            return False
    def time_to_collision(self,c):
        if (self.speed-c.speed)>0:
            return ((self.x**2+self.y**2)**0.5-(c.x**2+c.y**2)**0.5)/(self.speed-c.speed)
        else:
            return -1
make1=input("enter make of the car:")
model1=input("enter model of the car:")
year1=int(input("enter the year of manufacture:"))
speed1=int(input("Enter the speed of car1:"))
x1=int(input("enter x coordinate of car1:"))
y1=int(input("enter y coordinate of car1:"))
c1=car(make1,model1,year1,speed1,x1,y1)
make2=input("enter make of the car2:")
model2=input("enter model of the car2:")
year2=int(input("enter the year of manufacture:"))
speed2=int(input("Enter the speed of car2:"))
x2=int(input("enter x coordinate of car2:"))
y2=int(input("enter y coordinate of car2:"))
c2=car(make2,model2,year2,speed2,x2,y2)

op=(input("Which car speed need to be incremented or Decremented:"))
if op.lower()==model1.lower():
    op1=(input("speed increment or decrement (I/D)?:"))
    if op1.lower()=="i":
            sp1=int(input("enter the speed need to be incremented:"))
            c1.accelerate(sp1)
    else:
            sp1=int(input("Enter the speed need to be decremented:"))
            c1.brake(sp1)
else:
    op1=("speed increment or decrement (I/D)?:")
    if op1.lower()=="i":
            sp1=int(input("enter the speed need to be incremented:"))
            c2.accelerate(sp1)
    else:
            sp1=int(input("Enter the speed need to be decremented:"))
            c2.brake(sp1) 
c1.move()
c2.move()
s=c1.detect_collision(c2)
if s=="True":
    print("collided")
else:
    print("No collision")
time=c1.time_to_collision(c2)
if time==-1:
    print("Never Collide")
else:
    print("time to collide in hours:",time)