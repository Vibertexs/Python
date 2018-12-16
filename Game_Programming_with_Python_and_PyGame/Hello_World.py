import pygame, sys
pygame.init()   

windowSize = (800,600)

screen = pygame.display.set_mode(windowSize)

# myriadProFont = pygame.font.SysFont("Myraid Pro", 48) used for rendering text only
# helloWorld =  myriadProFont.render("Hello World", 1, (255,0, 255), (255,255,255))


# helloWorld =  pygame.image.load("C:\pngs abc\Small-mario.png")
helloWorld =  pygame.image.load("static\Small-mario.png")

helloWorldSize = helloWorld.get_size() #returns is as a tuple

pygame.mouse.set_visible(0)

x , y = 0,0
directionX, directionY = 1,1
clock = pygame.time.Clock()

while 1:
        try: 
                clock.tick(60)        #Controls the fps 


                for event in pygame.event.get():
                        if event.type == pygame.QUIT: sys.exit()
                                
                screen.fill((0,0,0))   

                mousePosition = pygame.mouse.get_pos()

                x, y = mousePosition
                print(mousePosition)
                if x + helloWorldSize[0] > 800:
                        x = 800 - helloWorldSize[0]

                if y + helloWorldSize[1] > 600:
                        y = 600 - helloWorldSize[1]

                screen.blit(helloWorld, (x ,y))

                pygame.display.update()
        except SystemExit:
                break
#blit will just add not caring about whats on the screen  
