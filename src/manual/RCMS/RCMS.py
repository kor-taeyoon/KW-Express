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


# Display Initialize
screen = pygame.display.set_mode((300,300)) # WIDTH, HEIGHT
pygame.display.set_caption("KW-Express")
clock = pygame.time.Clock()
run = True

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
                print('w')
            if event.key == pygame.K_s:
                print('s')
            if event.key == pygame.K_a:
                print('a')
            if event.key == pygame.K_d:
                print('d')
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_w) or (event.key == pygame.K_s) or (event.key == pygame.K_a) or (event.key == pygame.K_d):
                print('stop')

    

    # Tick (FPS)
    clock.tick(60)
