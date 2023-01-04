import pygame
import numpy as np
from time import time
from time import localtime
# 게임 윈도우 크기
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255,51,180)
BGD= (118,12,12)
FILL= (255,192,103)

def Rmat(degree):
    radian = np.deg2rad(degree)
    c = np.cos(radian)
    s = np.sin(radian)
    R = np.array( [[ c, -s, 0], [s, c, 0], [0, 0, 1] ] )
    return R

def Tmat(a,b):
    H = np.eye(3)
    H[0,2] = a
    H[1,2] = b
    return H


# Pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("Drawing")

# 윈도우 생성
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# 게임 종료 전까지 반복
done = False
# 폰트 선택(폰트, 크기, 두껍게, 이탤릭)
font = pygame.font.SysFont('FixedSys', 40, True, False)

# poly: 4 x 3 matrix
hourhand=np.array( [[0, 0, 1], [150, 0, 1], [150, 20, 1], [0, 20, 1]])
hourhand= hourhand.T

minhand=np.array( [[0, 0, 1], [250, 0, 1], [250, 20, 1], [0, 20, 1]])
minhand=minhand.T

sechand=np.array( [[0, 0, 1], [200, 0, 1], [200, 12, 1], [0, 12, 1]])
sechand=sechand.T

cor = np.array([10, 10, 1])
cor2 = np.array([6, 6, 1])

print(time())
print(localtime(time()))


# 게임 반복 구간
while not done:
    # 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # 윈도우 화면 채우기
    screen.fill(FILL)

    font = pygame.font.SysFont('FixedSys', 50, True, False)
    text12=font.render("XVI",True, BLACK)
    screen.blit(text12, [325, 100])

    text3=font.render("III",True, BLACK)
    screen.blit(text3, [600, 345])

    text6=font.render("VI",True, BLACK)
    screen.blit(text6, [340, 600])

    text9=font.render("IX",True, BLACK)
    screen.blit(text9, [95, 345])
    

    cal=localtime(time())
    hour=cal[3]
    min=cal[4]
    sec=cal[5]

    sdegree = sec * 6 -90
    mdegree = min * 6 + sec/10 -90 #60초에 분침 6도
    hdegree = hour%12 * 30 + min/2 + sec/120 -90# 60분에 시침 30도 


    #HOUR
    H = Tmat(350, 350) @ Tmat(10, 10) @ Rmat(hdegree) @ Tmat(-10, -10)
    pph = H @ hourhand
    # print(pp.shape, pp, pp.T )
    qh = pph[0:2, :].T # N x 2 matrix
    pygame.draw.polygon(screen, RED, qh, 4)

    #MINUTE
    M = Tmat(350, 350) @ Tmat(10, 10) @ Rmat(mdegree) @ Tmat(-10, -10)
    ppm = M @ minhand
    # print(pp.shape, pp, pp.T )
    qm = ppm[0:2, :].T # N x 2 matrix
    pygame.draw.polygon(screen, PINK, qm, 4)

    #SECOND
    S = Tmat(354, 354) @ Tmat(6, 6) @ Rmat(sdegree) @ Tmat(-6, -6)
    pps = S @ sechand
    corps = S @ cor2 #점
    # print(pp.shape, pp, pp.T )
    qs = pps[0:2, :].T # N x 2 matrix
    pygame.draw.polygon(screen, BGD, qs, 4)
    pygame.draw.circle(screen, BGD, corps[:2], 3)


    
    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)

    # 게임 종료
pygame.quit()