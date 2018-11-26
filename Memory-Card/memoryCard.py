import pygame,sys,random,time
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption('记忆卡片')

#设置图片尺寸，以及读取图片
imageWidth = 120
imageHeight = 120
cardImage1 = pygame.image.load('source/xiaohulu2.jpg')
cardImage2 = pygame.image.load('source/mengmeng2.jpg')
cardImage3 = pygame.image.load('source/dengmeimei.jpg')
cardImage4 = pygame.image.load('source/shigege.jpg')
bgcardImage = pygame.image.load('source/bgcard.jpg')
bgImage = pygame.image.load('source/BG.jpg')
#设置音效
victroySound = pygame.mixer.Sound('source/victroy.wav')
failSound = pygame.mixer.Sound('source/fail.wav')
#设置图片的位置
image_rect1 = Rect(100,180,imageWidth,imageHeight)
image_rect2 = Rect(260,180,imageWidth,imageHeight)
image_rect3 = Rect(420,180,imageWidth,imageHeight)
image_rect4 = Rect(580,180,imageWidth,imageHeight)
image_rect5 = Rect(100,340,imageWidth,imageHeight)
image_rect6 = Rect(260,340,imageWidth,imageHeight)
image_rect7 = Rect(420,340,imageWidth,imageHeight)
image_rect8 = Rect(580,340,imageWidth,imageHeight)
#设置背景图片并加载
screen.blit(bgImage,(0,0))
imageList = [cardImage1,cardImage2,cardImage3,cardImage4]*2
random.shuffle(imageList)
rectList = [image_rect1,image_rect2,image_rect3,image_rect4,image_rect5,image_rect6,image_rect7,image_rect8]
clickImageList = []
clickRectList = []

#游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            #按空格键开始游戏，先展示图片内容
            if event.key == pygame.K_SPACE:
                for i in range(8):
                    screen.blit(imageList[i],rectList[i])
            #按下回车键后盖住卡片内容
            if event.key == pygame.K_RETURN:
                for i in range(8):
                    screen.blit(bgcardImage,rectList[i])
        #鼠标点击图片出现原来的正面图片
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            for i in range(8):
                if rectList[i].collidepoint(mouse_x,mouse_y):
                    screen.blit(imageList[i],rectList[i])
                    # if imageList[i] not in clickImageList:
                    clickImageList.append(imageList[i])
                    clickRectList.append(rectList[i])
                    print(clickImageList)
            pygame.time.wait(1000)
            if len(clickImageList) == 2 :
                print(clickImageList)
                if clickImageList[0] == clickImageList[1]:
                    victroySound.play()
                    # pygame.draw.circle(screen,red,(clickRectList[0].centerx,clickRectList[0].centery),20,0)
                    # pygame.draw.circle(screen,red, (clickRectList[1].centerx, clickRectList[1].centery), 20, 0)
                else:
                    failSound.play()
                    # pygame.draw.circle(screen,blue,(50,100),20,0)
                    pygame.time.wait(1000)
                    for i in range(2):
                        screen.blit(bgcardImage, clickRectList[i])
                clickImageList=[]
                clickRectList=[]

                print(clickImageList)





    pygame.display.update()





