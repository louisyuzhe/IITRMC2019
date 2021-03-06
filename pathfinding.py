#Move 3 steps aheah (40cm each)
import matplotlib.pyplot as plt
import math

class Pathfinding:
    def __init__(self, rx ,ry):
        self.isForward = True       #If the robot is going forward
        self.r = 50.0 # radius of robot
        self.rX = rx  # x-coordinate of robot
        self.rY = ry  # y-coordinate of robot

        # coordinates of 2 detected obstacles
        self.obstacle = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]

        dir = 1     #Direction faced by the robot
        dest = 1    #Direction of destination (-1 = bin, 1 = mining area)

        #Coordinate of first obstacle
        xA = yA = 0.0

        #Coordinate of first obstacle
        xB = yB = 0.0

        #Coordinate of the next 3 steps to be taken
        x1 = y1 = 0.0
        x2 = y2 = 0.0
        x3 = y3 = 0.0

    def pathFinder(self, numObstacle): # Returns a path of the next 3 points
        print("Start Pathfinding")

        if(numObstacle == 0):
            self.moveStraight()
            #x2 = y2 = x3 = y3 = self.obstacle[0][0]]= [0][1]= [1][0] = [1][1] = None
            self.draw(self.rX, self.rY,x1,y1, None,None,None,None,None, None, None, None)
        if(numObstacle == 1):
            self.pathA(1)
            self.draw(self.rX, self.rY,x1,y1,x2,y2,x3,y3,self.obstacle[0][0], self.obstacle[0][1], None, None)
        if(numObstacle == 2):
            self.pathB()
            self.draw(self.rX, self.rY,x1,y1,x2,y2,x3,y3,self.obstacle[0][0], self.obstacle[0][1], self.obstacle[1][0], self.obstacle[1][1])
        else:# eliminate unnecessary obstacle
           pass # need to implement

    def moveTo(self, x, y): # move robot to given (x,y) coordinates
        pass # need to implement using aruidno motor class

    def moveStraight(self): # moves robot forward/backward 10 cm
        global x1
        global y1

        #Set directon to moving forward or backward
        if (self.isForward == True):
            dest = 1
        else:
            dest = -1
        print(self.rX, self.rY)
        x1 = self.rX+dest*10
        y1 = self.rY
        self.moveTo(x1, y1)   #Move 10cm forward

    def pathA(self, num): # if numObstacle == 1
        global xA
        global yA
        global x1
        global y1
        global x2
        global y2
        global x3
        global y3

        #Set directon to moving forward or backward
        if(self.isForward == True):
            dest = 1
        else:
            dest = -1

        if(num == 1):
            xA = self.obstacle[0][0]
            yA = self.obstacle[0][1]
            if(yA > 0.0):
                dir = -1
            else:
                dir = 1
        if(num == 2):
            if((self.obstacle[0][1]+self.obstacle[1][1])/2 > 0):
                dir = -1
            else:
                dir = 1
            if(dir == 1):
                if(self.obstacle[0][1] > self.obstacle[1][1]):
                    xA = self.obstacle[0][0]
                    yA = self.obstacle[0][1]
                    xB = self.obstacle[1][0]
                    yB = self.obstacle[1][1]
                else:
                    xA = self.obstacle[1][0]
                    yA = self.obstacle[1][1]
                    xB = self.obstacle[0][0]
                    yB = self.obstacle[0][1]
            else:
                if(self.obstacle[0][1] > self.obstacle[1][1]):
                    xA = obstacle[1][0]
                    yA = obstacle[1][1]
                    xB = obstacle[0][0]
                    yB = obstacle[0][1]
                else:
                    xA = self.obstacle[0][0]
                    yA = self.obstacle[0][1]
                    xB = self.obstacle[1][0]
                    yB = self.obstacle[1][1]
        x3 = xA
        y3 = yA + dir*(self.r+40)
        x2 = xA - dest*(self.r+40)*2/3
        y2 = y3
        x1 = xA - dest * (self.r + 40)
        y1 = y3 - dir*(self.r+ 40)/3
        if(dest*x1 > dest*self.rX):
            self.moveTo(x1,y1)      #Move to first point
        if (dest * x2 > dest * self.rX):
            self.moveTo(x2, y2)     #Move to second point
        if (dest * x3 > dest * self.rX):
            self.moveTo(x3, y3)     #Move to third point

    def pathB(self): # if numObstacle == 2
        global xA
        global yA
        global xB
        global yB
        global x1
        global y1
        global x2
        global y2
        global x3
        global y3
        xA = self.obstacle[0][0]
        yA = self.obstacle[0][1]
        xB = self.obstacle[1][0]
        yB = self.obstacle[1][1]
        width = math.sqrt(math.pow(xB-xA,2)+math.pow(yB-yA,2)) - self.obstacle[0][2] - self.obstacle[1][2]
        x1 = (xA + xB) / 2
        y1 = (yA + yB) / 2
        if (self.isForward == True):
            dest = 1
        else:
            dest = -1
        if(width > 2*self.r):
            if(math.fabs(yA-yB) < 2*self.r):
                if(dest*(xA-xB) < 0.0):
                    xA = self.obstacle[1][0]
                    yA = self.obstacle[1][1]
                    xB = self.obstacle[0][0]
                    yB = self.obstacle[0][1]
                if((yA-yB) > 0.0):
                    dir = -1
                else:
                    dir = 1
                x2 = x1
                y2 = y1
                if(dest == dir):
                    x1 = x2 - dest*30
                    y1 = y2 - dest*30
                else:
                    x1 = x2 + dir*30
                    y1 = y2 + dest*30
                x3 = xA
                y3 = yA + dir*(self.r+40)
            else:
                x2 = x1
                y2 = y1
                x1 = x2 - dest*20
                y3 = y2
                x3 = x2 + dest*20

            if(dest*x1 > dest*self.rX):
                self.moveTo(x1,y1)      #Move to first point
            if (dest * x2 > dest * self.rX):
                self.moveTo(x2, y2)     #Move to second point
            if (dest * x3 > dest * self.rX):
                self.moveTo(x3, y3)     #Move to third point
        else:
            self.pathA(2) # treat the two obstacles as a single big one

    def draw(self, rX,rY,x1,y1,x2,y2,x3,y3,xA,yA,xB,yB): # plot to test cases
        plt.plot([rX, x1, x2, x3], [rY, y1,y2,y3])

        if((xA != None) & (yA != None)):
                        plt.plot([xA-10.6, xA-10.6, xA+10.6, xA+10.6, xA-10.6 ], [yA-10.6, yA+10.6, yA+10.6, yA-10.6, yA-10.6])
        if((xB != None) & (yB != None)):
            plt.plot([xB-10.6, xB-10.6, xB+10.6, xB+10.6, xB-10.6 ], [yB-10.6, yB+10.6, yB+10.6, yB-10.6, yB-10.6])

        plt.plot([rX-40, rX-40, rX+40, rX+40, rX-40 ], [rY-40, rY+40, rY+40, rY-40, rY-40])
        plt.plot([x1-40, x1-40, x1+40, x1+40, x1-40 ], [y1-40, y1+40, y1+40, y1-40, y1-40])
        if((x2 != None) & (y2 != None) & (x3 != None) & (y3 != None)):
            plt.plot([x2-40, x2-40, x2+40, x2+40, x2-40 ], [y2-40, y2+40, y2+40, y2-40, y2-40])
            plt.plot([x3-40, x3-40, x3+40, x3+40, x3-40 ], [y3-40, y3+40, y3+40, y3-40, y3-40])
        plt.show()
