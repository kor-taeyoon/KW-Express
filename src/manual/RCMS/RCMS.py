'''
import sys
import time
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic

last = 0

form_class = uic.loadUiType("./src/manual/RCMS/RCMS.ui")[0]

class RCMS(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def keyPressEvent(self, e):
        global last
        if e.key() == Qt.Key_W:
            if (time.time() - last) > 0.1:
                print('forward')
            last = time.time()
        if e.key() == Qt.Key_S:
            if (time.time() - last) > 0.1:
                print('backward')
            last = time.time()
        if e.key() == Qt.Key_A:
            if (time.time() - last) > 0.1:
                print('lefttrun')
            last = time.time()
        if e.key() == Qt.Key_D:
            if (time.time() - last) > 0.1:
                print('righttrun')
            last = time.time()

    def keyReleaseEvent(self, e):
        print('stop')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_RCMS = RCMS()
    app_RCMS.show()


    app.exec_()
'''
import pygame
pygame.init()

# Define
WIN_WIDTH = 925
WIN_HEIGHT = 510
FPS = 50
STEP_MAX_SPEED = 10000
STEP_ACCEL = 20000
STEP_ACCEL_FRAME = STEP_ACCEL/FPS


# Display Initialize
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) # WIDTH, HEIGHT
pygame.display.set_caption("KW-Express")
clock = pygame.time.Clock()
run = True


def DrawSquare(center_x, center_y, size, fill):
    if fill == 0:
        pygame.draw.rect(screen, (0,0,0), (center_x-(size/2), center_y-(size/2),size, size), 0)
    else:
        pygame.draw.rect(screen, (0,0,0), (center_x-(size/2), center_y-(size/2),size, size), fill)    

# Object Initialize
screen.fill((150,150,150))
stop = DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2, 80, 0)
forward = DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2-100, 80, 1)
backward = DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2+100, 80, 1)
lefttrun = DrawSquare(WIN_WIDTH/2-100, WIN_HEIGHT/2, 80, 1)
righttrun = DrawSquare(WIN_WIDTH/2+100, WIN_HEIGHT/2, 80, 1)
flag_left = 0
flag_right = 0
velo_left = 0
velo_right = 0

# Main Loop Start
while run:
    # Keyboard Event Process
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_w:
                screen.fill((150,150,150))
                stop = DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2, 80, 1)
                forward = DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2-100, 80, 0)
                backward = DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2+100, 80, 1)
                lefttrun = DrawSquare(WIN_WIDTH/2-100, WIN_HEIGHT/2, 80, 1)
                righttrun = DrawSquare(WIN_WIDTH/2+100, WIN_HEIGHT/2, 80, 1)
                flag_left = 1
                flag_right = 1
                print('w')
            if event.key == pygame.K_s:
                screen.fill((150,150,150))
                stop = DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2, 80, 1)
                forward = DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2-100, 80, 1)
                backward = DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2+100, 80, 0)
                lefttrun = DrawSquare(WIN_WIDTH/2-100, WIN_HEIGHT/2, 80, 1)
                righttrun = DrawSquare(WIN_WIDTH/2+100, WIN_HEIGHT/2, 80, 1)
                flag_left = -1
                flag_right = -1
                print('s')
            if event.key == pygame.K_a:
                screen.fill((150,150,150))
                stop = DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2, 80, 1)
                forward = DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2-100, 80, 1)
                backward = DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2+100, 80, 1)
                lefttrun = DrawSquare(WIN_WIDTH/2-100, WIN_HEIGHT/2, 80, 0)
                righttrun = DrawSquare(WIN_WIDTH/2+100, WIN_HEIGHT/2, 80, 1)
                flag_left = -1
                flag_right = 1
                print('a')
            if event.key == pygame.K_d:
                screen.fill((150,150,150))
                stop = DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2, 80, 1)
                forward = DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2-100, 80, 1)
                backward = DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2+100, 80, 1)
                lefttrun = DrawSquare(WIN_WIDTH/2-100, WIN_HEIGHT/2, 80, 1)
                righttrun = DrawSquare(WIN_WIDTH/2+100, WIN_HEIGHT/2, 80, 0)
                flag_left = 1
                flag_right = -1
                print('d')
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_w) or (event.key == pygame.K_s) or (event.key == pygame.K_a) or (event.key == pygame.K_d):
                screen.fill((150,150,150))
                stop = DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2, 80, 0)
                forward = DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2-100, 80, 1)
                backward = DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2+100, 80, 1)
                lefttrun = DrawSquare(WIN_WIDTH/2-100, WIN_HEIGHT/2, 80, 1)
                righttrun = DrawSquare(WIN_WIDTH/2+100, WIN_HEIGHT/2, 80, 1)
                flag_left = 0
                flag_right = 0
                print('stop')

    # Wheel Step Per Sec Calculator
    if flag_left == 1:    # Accel On
        if velo_left <= STEP_MAX_SPEED-STEP_ACCEL_FRAME:
            velo_left+=STEP_ACCEL_FRAME
    elif flag_left == -1:
        if velo_left >= -(STEP_MAX_SPEED-STEP_ACCEL_FRAME):
            velo_left-=STEP_ACCEL_FRAME
    else:   # Accel Off
        if velo_left > 0:
            if velo_left >= 0+STEP_ACCEL_FRAME:
                velo_left-=STEP_ACCEL_FRAME
        elif velo_left < 0:
            if velo_left <= 0-STEP_ACCEL_FRAME:
                velo_left+=STEP_ACCEL_FRAME
    if flag_right == 1:    # Accel On
        if velo_right <= STEP_MAX_SPEED-STEP_ACCEL_FRAME:
            velo_right+=STEP_ACCEL_FRAME
    elif flag_right == -1:
        if velo_right >= -(STEP_MAX_SPEED-STEP_ACCEL_FRAME):
            velo_right-=STEP_ACCEL_FRAME
    else:   # Accel Off
        if velo_right > 0:
            if velo_right >= 0+STEP_ACCEL_FRAME:
                velo_right-=STEP_ACCEL_FRAME
        elif velo_right < 0:
            if velo_right <= 0-STEP_ACCEL_FRAME:
                velo_right+=STEP_ACCEL_FRAME
    
    
    print(flag_left, flag_right, velo_left, velo_right)
        
    # Refresh & Tick (FPS)
    pygame.display.update()
    clock.tick(FPS)
