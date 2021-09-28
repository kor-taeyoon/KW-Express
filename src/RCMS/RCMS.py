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

print('Launch waiting... 3s')
time.sleep(1)
print('Launch waiting... 2s')
time.sleep(1)
print('Launch waiting... 1s')
time.sleep(1)
print('Launched !')



# PyGame GUI Start
# ========================================
# Define
WIN_WIDTH = 925
WIN_HEIGHT = 510
FPS = 40
STEP_MAX_SPEED = 10000
STEP_ACCEL = 20000
STEP_ACCEL_FRAME = STEP_ACCEL/FPS

# Global Variables & Objects
data_barcode = ""
time_last_barcode = time.time()
flag_stop = 1
flag_forward = 0
flag_backward = 0
flag_leftturn = 0
flag_rightturn = 0
flag_left = 0
flag_right = 0
flag_window = 0
flag_gori_1 = 1
flag_gori_2 = 1
flag_gori_3 = 1
velo_left = 0
velo_right = 0
myFont = pygame.font.SysFont("arial", 30, True, False)
txt_velo_left = myFont.render(str(velo_left), True, (0,0,0))

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

def DrawCircle(center_x, center_y, size, fill):
    if fill == 0:
        pygame.draw.circle(screen, (0,0,0), (center_x-(size/2), center_y-(size/2)), size, 0)
    else:
        pygame.draw.circle(screen, (0,0,0), (center_x-(size/2), center_y-(size/2)), size, fill)
    






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
    txt_barcode = myFont.render(data_barcode, True, (0,0,0))
    
    
    
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
            if event.key == pygame.K_w:     # 전진
                flag_stop = 0
                flag_forward = 1
                flag_left = 1
                flag_right = 1
                ser_nucleo.write("w".encode())
            if event.key == pygame.K_x:     # 후진
                flag_stop = 0
                flag_backward = 1
                flag_left = -1
                flag_right = -1
                ser_nucleo.write("x".encode())
            if event.key == pygame.K_a:     # 좌회전
                flag_stop = 0
                flag_leftturn = 1
                flag_left = -1
                flag_right = 1
                ser_nucleo.write("a".encode())
            if event.key == pygame.K_d:     # 우회전
                flag_stop = 0
                flag_rightturn = 1
                flag_left = 1
                flag_right = -1
                ser_nucleo.write("d".encode())

            if event.key == pygame.K_r:     # 창문 열기
                ser_ramps.write("r".encode())
                flag_window = 1
            if event.key == pygame.K_f:     # 창문 닫기
                ser_ramps.write("f".encode())
                flag_window = 0
            if event.key == pygame.K_t:     # 1번 고리 복귀
                ser_ramps.write("t".encode())
                flag_gori_1 = 1
            if event.key == pygame.K_g:     # 1번 고리 낙하
                ser_ramps.write("g".encode())
                flag_gori_1 = 0
            if event.key == pygame.K_y:     # 2번 고리 복귀
                ser_ramps.write("y".encode())
                flag_gori_2 = 1
            if event.key == pygame.K_h:     # 2번 고리 낙하
                ser_ramps.write("h".encode())
                flag_gori_2 = 0
            if event.key == pygame.K_u:     # 3번 고리 복귀
                ser_ramps.write("u".encode())
                flag_gori_3 = 1
            if event.key == pygame.K_j:     # 3번 고리 낙하
                ser_ramps.write("h".encode())
                flag_gori_3 = 0

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
    txt_velo_left = myFont.render(str(int(velo_left))+" step/s", True, (0,0,0))
    txt_velo_right = myFont.render(str(int(velo_right))+" step/s", True, (0,0,0))
    
    # GUI Drawing
    # ========================================
    # Controlling Box Drawing
    screen.fill((150,150,150))
    DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2, 60, 3)        # S
    DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2-100, 80, 5)    # W
    DrawSquare(WIN_WIDTH/2, WIN_HEIGHT/2+100, 80, 5)    # X
    DrawSquare(WIN_WIDTH/2-100, WIN_HEIGHT/2, 80, 5)    # A
    DrawSquare(WIN_WIDTH/2+100, WIN_HEIGHT/2, 80, 5)    # D
    DrawCircle(WIN_WIDTH-250, WIN_HEIGHT-100, 20, 4)    # F # 창문 올리기
    DrawCircle(WIN_WIDTH-250, WIN_HEIGHT-50, 20, 4)     # R # 창문 내리기
    DrawCircle(WIN_WIDTH-150, WIN_HEIGHT-100, 20, 4)    # G # 1번 고리 복귀
    DrawCircle(WIN_WIDTH-150, WIN_HEIGHT-50, 20, 4)     # T # 1번 고리 낙하
    DrawCircle(WIN_WIDTH-100, WIN_HEIGHT-100, 20, 4)    # H # 2번 고리 복귀
    DrawCircle(WIN_WIDTH-100, WIN_HEIGHT-50, 20, 4)     # Y # 2번 고리 낙하
    DrawCircle(WIN_WIDTH-50, WIN_HEIGHT-100, 20, 4)     # J # 3번 고리 복귀
    DrawCircle(WIN_WIDTH-50, WIN_HEIGHT-50, 20, 4)      # U # 3번 고리 낙하

    # Drawn Square Modifying
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

    if flag_window:
        DrawCircle(WIN_WIDTH-250, WIN_HEIGHT-100, 20, 0)
    else:
        DrawCircle(WIN_WIDTH-250, WIN_HEIGHT-50, 20, 0)
    if flag_gori_1:
        DrawCircle(WIN_WIDTH-150, WIN_HEIGHT-100, 20, 0)
    else:
        DrawCircle(WIN_WIDTH-150, WIN_HEIGHT-50, 20, 0)
    if flag_gori_2:
        DrawCircle(WIN_WIDTH-100, WIN_HEIGHT-100, 20, 0)
    else:
        DrawCircle(WIN_WIDTH-100, WIN_HEIGHT-50, 20, 0)
    if flag_gori_3:
        DrawCircle(WIN_WIDTH-50, WIN_HEIGHT-100, 20, 0)
    else:
        DrawCircle(WIN_WIDTH-50, WIN_HEIGHT-50, 20, 0)

    # Text Data Update
    screen.blit(txt_velo_left, [WIN_WIDTH/2 - 250, WIN_HEIGHT/2 - 200])
    screen.blit(txt_velo_right, [WIN_WIDTH/2 + 200, WIN_HEIGHT/2 - 200])
    screen.blit(txt_barcode, [30, WIN_HEIGHT-50])
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

    # Refresh & Tick (FPS)
    pygame.display.update()
    clock.tick(FPS)
