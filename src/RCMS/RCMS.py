# Module import
import time
import serial
import pygame
pygame.init()


# Serial Connection
# ========================================

try:
    ser_nucleo = serial.Serial("/dev/Nucleo-F103RB", 9600, timeout=1)
    print('Nucleo-F103RB UART Connection Established!')
except:
    print('Nucleo-F103RB UART Connection Error Occured.')
    exit()

try:
    ser_ramps = serial.Serial("/dev/RAMPS", 9600, timeout=1)
    print('RAMPS UART Connection Established!')
except:
    print('RAMPS UART Connection Error Occured.')
    exit()

try:
    ser_barcode = serial.Serial("/dev/barcode_reader", 115200, timeout=0.001)
    print('BarCode Reader UART Connection Established!')
except:
    print('BarCode Reader UART Connection Error Occured.')
    exit()


data_barcode = ""
time_last_barcode = time.time()


time.sleep(1)


# PyGame GUI Start
# ========================================
# Define
WIN_WIDTH = 925
WIN_HEIGHT = 510
FPS = 40
STEP_MAX_SPEED = 10000
STEP_ACCEL = 20000
STEP_ACCEL_FRAME = STEP_ACCEL/FPS

# Display Initialize
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) # WIDTH, HEIGHT
pygame.display.set_caption("KW-Express")
clock = pygame.time.Clock()
run = True

# Object Drawing Function
def DrawSquare(center_x, center_y, size, fill):
    if fill == 0:
        pygame.draw.rect(screen, (0,0,0), (center_x-(size/2), center_y-(size/2),size, size), 0)
    else:
        pygame.draw.rect(screen, (0,0,0), (center_x-(size/2), center_y-(size/2),size, size), fill)    

# Object Initialize
flag_stop = 1
flag_forward = 0
flag_backward = 0
flag_leftturn = 0
flag_rightturn = 0
flag_left = 0
flag_right = 0
velo_left = 0
velo_right = 0
myFont = pygame.font.SysFont("arial", 30, True, False)
txt_velo_left = myFont.render(str(velo_left), True, (0,0,0))




# Main Loop Start
# ========================================
while run:
    # Barcode Data process
    if ser_barcode.readable():
        res = ser_barcode.read()
        if res != b'':
            res += ser_barcode.readline()
            data_barcode = "BarCode Data : " + res.decode()[:len(res)-1]
            ser_nucleo.write(data_barcode.encode())
            time_last_barcode = time.time()
    if time.time() - time_last_barcode > 2:
        data_barcode = ""
    
    # Controlling Box Drawing
    screen.fill((150,150,150))
    stop = DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2, 60, 3)
    forward = DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2-100, 80, 3)
    backward = DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2+100, 80, 3)
    lefttrun = DrawSquare(WIN_WIDTH/2-100, WIN_HEIGHT/2, 80, 3)
    righttrun = DrawSquare(WIN_WIDTH/2+100, WIN_HEIGHT/2, 80, 3)
    
    # Keyboard Event Process
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            ser_nucleo.close()
            ser_ramps.close()
            ser_barcode.close()
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_w:
                flag_stop = 0
                flag_forward = 1
                flag_left = 1
                flag_right = 1
                ser_nucleo.write("w".encode())
            if event.key == pygame.K_x:
                flag_stop = 0
                flag_backward = 1
                flag_left = -1
                flag_right = -1
                ser_nucleo.write("x".encode())
            if event.key == pygame.K_a:
                flag_stop = 0
                flag_leftturn = 1
                flag_left = -1
                flag_right = 1
                ser_nucleo.write("a".encode())
            if event.key == pygame.K_d:
                flag_stop = 0
                flag_rightturn = 1
                flag_left = 1
                flag_right = -1
                ser_nucleo.write("d".encode())
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_w) or (event.key == pygame.K_x) or (event.key == pygame.K_a) or (event.key == pygame.K_d):
                flag_stop = 1
                flag_forward = 0
                flag_backward = 0
                flag_leftturn = 0
                flag_rightturn = 0
                flag_left = 0
                flag_right = 0
                ser_nucleo.write("s".encode())

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
    
    # Velocity Data Update
    txt_velo_left = myFont.render(str(int(velo_left))+" step/s", True, (0,0,0))
    screen.blit(txt_velo_left, [WIN_WIDTH/2 - 250, WIN_HEIGHT/2 - 200])
    txt_velo_right = myFont.render(str(int(velo_right))+" step/s", True, (0,0,0))
    screen.blit(txt_velo_right, [WIN_WIDTH/2 + 200, WIN_HEIGHT/2 - 200])
    txt_barcode = myFont.render(data_barcode, True, (0,0,0))
    screen.blit(txt_barcode, [30, WIN_HEIGHT-50])

    # Normal Text Data Update
    txt_tmp = myFont.render("W", True, (0,0,0))
    screen.blit(txt_tmp, [WIN_WIDTH/2-14, WIN_HEIGHT/2 - 110])
    txt_tmp = myFont.render("X", True, (0,0,0))
    screen.blit(txt_tmp, [WIN_WIDTH/2-10, WIN_HEIGHT/2 + 90])
    txt_tmp = myFont.render("A", True, (0,0,0))
    screen.blit(txt_tmp, [WIN_WIDTH/2 - 110, WIN_HEIGHT/2-10])
    txt_tmp = myFont.render("D", True, (0,0,0))
    screen.blit(txt_tmp, [WIN_WIDTH/2 + 90, WIN_HEIGHT/2-10])
    txt_tmp = myFont.render("S", True, (0,0,0))
    screen.blit(txt_tmp, [WIN_WIDTH/2-10, WIN_HEIGHT/2-10])

    # Controlling Square Drawing
    if flag_stop:
        DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2, 60, 0)
    if flag_forward:
        DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2-100, 80, 0)
    if flag_backward:
        DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2+100, 80, 0)
    if flag_leftturn:
        DrawSquare(WIN_WIDTH/2-100, WIN_HEIGHT/2, 80, 0)
    if flag_rightturn:
        DrawSquare(WIN_WIDTH/2+100, WIN_HEIGHT/2, 80, 0)

    # Refresh & Tick (FPS)
    pygame.display.update()
    clock.tick(FPS)

