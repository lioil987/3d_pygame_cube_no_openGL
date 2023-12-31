import math
import time
from math import cos, sin
from typing import Callable

import pygame
from abc import abstractmethod, ABC
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 2500, 1500
screen = pygame.display.set_mode((width, height))

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)


class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class ShapeObject:
    circles = []
    edges = []
    list_type = []

    @staticmethod
    def list_all_shapes():
        ShapeObject.list_type.append(ShapeObject.circles)
        ShapeObject.list_type.append(ShapeObject.edges)


class Shape(ABC):
    centerX = width / 2
    centerY = height / 2

    positions = []

    def __init__(self, positions):
        self.positions = positions

    def addPositions(self, position):
        self.positions.append(position)

    @abstractmethod
    def draw(self):
        pass

    def rotateZ(self, a):
        for position in self.positions:
            tempx = position.x
            tempy = position.y
            position.x = tempx * cos(a) - tempy * sin(a)
            position.y = tempx * sin(a) + tempy * cos(a)

    def rotateX(self, a):
        for position in self.positions:
            tempy = position.y
            tempz = position.z
            position.y = tempy * cos(a) - tempz * sin(a)
            position.z = tempz * cos(a) + tempy * sin(a)

    def rotateY(self, a):
        for position in self.positions:
            tempx = position.x
            tempz = position.z
            position.x = tempx * cos(a) + tempz * sin(a)
            position.z = tempz * cos(a) - tempx * sin(a)
    def transformX(self, m):
        Shape.centerX =Shape.centerX + m
        for position in self.positions:
            position.x = position.x + m
    def transformY(self, m):
        Shape.centerY = Shape.centerY+m
        for position in self.positions:
            position.y = position.y+m
    def transformZ(self, m):
        for position in self.positions:
            position.z = position.z +m


class Edge(Shape):
    def __init__(self, x1, y1, z1, x2, y2, z2):
        super().__init__(self.positions)
        self.positions = [Position(x1, y1, z1), Position(x2, y2, z2)]
        ShapeObject.edges.append(self)

    def draw(self):
        pygame.draw.line(screen, (123,112,212), (self.positions[0].x+Shape.centerX, self.positions[0].y+Shape.centerY),
                         (self.positions[1].x+Shape.centerX, self.positions[1].y+Shape.centerY), 20)


class Circle(Shape):

    def __init__(self, x, y, z=0, r=20):
        self.positions = []
        super().__init__(self.positions)
        self.position = Position(x, y, z)
        self.addPositions(self.position)
        self.r = r
        ShapeObject.circles.append(self)

    def draw(self):
        pygame.draw.circle(screen, (123,112,212), (self.position.x + Circle.centerX, self.position.y + Circle.centerY), self.r)


class ShapeManagement():
    @staticmethod
    def draw_all():
        for item in ShapeObject.list_type:
            for item in item:
                item.draw()

    @staticmethod
    def rotate_x_all(a):
        for itemI in ShapeObject.list_type:
            for itemII in itemI:
                itemII.rotateX(a)

    @staticmethod
    def rotate_y_all(a):
        for itemI in ShapeObject.list_type:
            for itemII in itemI:
                itemII.rotateY(a)

    @staticmethod
    def rotate_z_all(a):
        for itemI in ShapeObject.list_type:
            for itemII in itemI:
                itemII.rotateZ(a)
    @staticmethod
    def transform_x_all(m):
        for itemI in ShapeObject.list_type:
            for itemII in itemI:
                itemII.transformX(m)
    @staticmethod
    def transform_y_all(m):
        for itemI in ShapeObject.list_type:
            for itemII in itemI:
                itemII.transformY(m)
    @staticmethod
    def transform_z_all(m):
        for itemI in ShapeObject.list_type:
            for itemII in itemI:
                 itemII.transformZ(m)


t = 141
tn = -t

Circle(0, 200,tn)
Circle(-200, 0,tn)
Circle(200, 0,tn)
Circle(0, -200,tn)

Circle(0, 200,t)
Circle(-200, 0,t)
Circle(200, 0,t)
Circle(0, -200,t)



class FindDistance:
    class CircleDistance:
        def __init__(self,distance,circleI,circleII):
            self.distance = distance
            self.circleI = circleI
            self.circleII = circleII
    @staticmethod
    def calculate_distance(x1, y1, z1, x2, y2, z2):
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
        return math.floor(distance)
    @staticmethod
    def find():
        close_circles = []

        for itemI in ShapeObject.circles:
            distance = 0
            temp_list = []
            x1 = itemI.positions[0].x
            y1 = itemI.positions[0].y
            z1 = itemI.positions[0].z
            for itemII in ShapeObject.circles:
                x2 = itemII.positions[0].x
                y2 = itemII.positions[0].y
                z2 = itemII.positions[0].z
                distance = FindDistance.calculate_distance(x1,y1,z1,x2,y2,z2)
                temp_list.append(FindDistance.CircleDistance(distance, itemI,itemII))
            close_circles.append(temp_list)
        return close_circles
    @staticmethod
    def minimum():
        all_circles_distance = FindDistance.find()
        result = []
        for itemI in all_circles_distance:
            filtered_objects = [obj for obj in itemI if obj.distance != 0]
            closest_circles_distance = min(filtered_objects, key=lambda obj: obj.distance).distance
            filtered_closest_circles = [obj for obj in filtered_objects if obj.distance == closest_circles_distance]
            result.append(filtered_closest_circles)
        return result







ShapeObject.list_all_shapes()

uu = FindDistance.minimum()

for itemI in uu :
    for itemII in itemI:
        x1 = itemII.circleI.position.x
        y1 = itemII.circleI.position.y
        z1 = itemII.circleI.position.z
        x2 = itemII.circleII.position.x
        y2 = itemII.circleII.position.y
        z2 = itemII.circleII.position.z

        Edge(x1, y1, z1, x2, y2, z2)


def loop():



    ShapeManagement.draw_all()
    WindowManagement.check_and_run()


class WindowManagement:
    flag_w = False
    flag_s = False
    flag_d = False
    flag_a = False
    flag_e = False
    flag_q = False

    flag_up = False
    flag_down = False
    flag_left = False
    flag_right = False
    @staticmethod
    def keydown(event):
        if event.key == pygame.K_w:  WindowManagement.flag_w = True
        if event.key == pygame.K_s:  WindowManagement.flag_s = True
        if event.key == pygame.K_d:  WindowManagement.flag_d = True
        if event.key == pygame.K_a:  WindowManagement.flag_a = True
        if event.key == pygame.K_e:  WindowManagement.flag_e = True
        if event.key == pygame.K_q:  WindowManagement.flag_q = True
        if event.key == pygame.K_UP:  WindowManagement.flag_up = True
        if event.key == pygame.K_DOWN:  WindowManagement.flag_down = True
        if event.key == pygame.K_LEFT:  WindowManagement.flag_left = True
        if event.key == pygame.K_RIGHT:  WindowManagement.flag_right = True

    @staticmethod
    def keyup(event):
        if event.key == pygame.K_w:  WindowManagement.flag_w = False
        if event.key == pygame.K_s:  WindowManagement.flag_s = False
        if event.key == pygame.K_d:  WindowManagement.flag_d = False
        if event.key == pygame.K_a:  WindowManagement.flag_a = False
        if event.key == pygame.K_e:  WindowManagement.flag_e = False
        if event.key == pygame.K_q:  WindowManagement.flag_q = False
        if event.key == pygame.K_UP:  WindowManagement.flag_up = False
        if event.key == pygame.K_DOWN:  WindowManagement.flag_down = False
        if event.key == pygame.K_LEFT:  WindowManagement.flag_left = False
        if event.key == pygame.K_RIGHT:  WindowManagement.flag_right = False

    class work:
        @staticmethod
        def w():
            ShapeManagement.rotate_x_all(.03)

        @staticmethod
        def s():
            ShapeManagement.rotate_x_all(-.03)

        @staticmethod
        def d():
            ShapeManagement.rotate_y_all(.03)

        @staticmethod
        def a():
            ShapeManagement.rotate_y_all(-.03)

        @staticmethod
        def e():
            ShapeManagement.rotate_z_all(.03)

        @staticmethod
        def q():
            ShapeManagement.rotate_z_all(-.03)
        @staticmethod
        def left():
            ShapeManagement.transform_x_all(-.1)
        @staticmethod
        def right():
            ShapeManagement.transform_x_all(.1)
        @staticmethod
        def up():
            ShapeManagement.transform_y_all(-.1)
        @staticmethod
        def down():
            ShapeManagement.transform_y_all(.1)
    @staticmethod
    def check_and_run():
        if WindowManagement.flag_w:WindowManagement.work.w()
        if WindowManagement.flag_s:WindowManagement.work.s()
        if WindowManagement.flag_d:WindowManagement.work.d()
        if WindowManagement.flag_a:WindowManagement.work.a()
        if WindowManagement.flag_e:WindowManagement.work.e()
        if WindowManagement.flag_q:WindowManagement.work.q()
        if WindowManagement.flag_up:WindowManagement.work.up()
        if WindowManagement.flag_down:WindowManagement.work.down()
        if WindowManagement.flag_left:WindowManagement.work.left()
        if WindowManagement.flag_right:WindowManagement.work.right()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN: WindowManagement.keydown(event)
        elif event.type == pygame.KEYUP: WindowManagement.keyup(event)




    screen.fill(black)

    loop()

    # Update the display
    pygame.display.flip()
