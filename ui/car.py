class Car:

    def __init__(self, id, pos, vel = 0.5):
        self.id = id
        self.pos = pos
        self.vel = vel #velocity pixels
        
        

    def move(self,x, y):
        self.pos[0]+=x
        self.pos[1]+=y

    def move_to(self, dest):
        (x1, y1) = self.pos
        (x2, y2) = dest
        m = (y2-y1)/(x2-x1)

        #y2=y1+m(x2-x1) --> y1 = y2 - m(x2-x1)  || x1 = x2 - (y2-y1) / m
        
        x1 = x1 - self.vel if x1 > dest[0] else x1 + self.vel
        y1 = y1 - self.vel if y1 > dest[0] else y1 + self.vel

        y1 = y2 - m*(x2-x1)
        x1 = x2 - (y2-y1) / m

        self.pos = (x1, y1)
        #self.pos[0] = self.pos[0] - self.vel if self.pos[0] > dest[0] else self.pos[0] + self.vel
        #elf.pos[1] = self.pos[1] - self.vel if self.pos[1] > dest[1] else self.pos[1] + self.vel
        