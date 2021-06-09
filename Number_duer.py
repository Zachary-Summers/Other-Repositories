#Number douer
import pygame, math, sys, random
pygame.init()

#variable stuff
iNum12proMax=1#random.randint(-9999,9999)*random.choice([0.1,0.01,0.001,1])
name="Number douer"
w=800
h=600
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption(name)
buttons={"+":"+" , "-":"-", "*":"*", "/":"/" , "(":"(", ")":")",  ".":".",
        "0":"0",  "1":"1", "math.factorial(":"!"}
result=""
answer=0
fontSize=32
babyFont=pygame.font.SysFont("comicsansms",20)
font=pygame.font.SysFont("comicsansms",fontSize)

buttons_x=w//6
buttons_y=h-99-int(fontSize*1.5)
for i in buttons:
    buttons[i]=[font.render(str(buttons[i]), True, (0,255,255))]
    buttons[i].append(buttons[i][0].get_rect(center=(buttons_x,buttons_y)))
    screen.blit(buttons[i][0],buttons[i][1])
    buttons_x+=w//6
    
    if buttons_x>=w-10:
        buttons_x=w//6
        buttons_y+=int(fontSize*1.5)


clear=pygame.draw.circle(screen,(255,0,255),(w//2,46),10)
backspace=pygame.draw.circle(screen,(255,0,25),(w//2,15),10)

while True:
    answerText=font.render(str(answer),True,(255,255,0))
    answerText_rect=answerText.get_rect(center=(w//2,h//2))
    
    resultText=babyFont.render(result,True,(255,255,0))
    resultText_rect=resultText.get_rect(center=(w//2,87))
    
    iNum12proMax_text=font.render(str(iNum12proMax),True,(255,0,0))
    iNum12proMax_rect=iNum12proMax_text.get_rect(center=(200,h//2-50))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if clear.collidepoint(event.pos):
                result=''
                answer=0
            elif backspace.collidepoint(event.pos):
                result=result[:-1]
                try:
                    answer=eval(result)
                except:
                    pass
                
            for i in buttons:
                if buttons[i][1].collidepoint(event.pos):
                    result+=i
                    resultText=babyFont.render(result,True,(255,255,0))
                    resultText_rect=resultText.get_rect(center=(w//2,random.randint(80,90)))
                    try:
                        answer=eval(result)
                        if answer==iNum12proMax:
                            print("you may be a wainner")
                            result="Cheese"
                            iNum12proMax=random.randint(-999999,999999)*random.choice([0.1,0.01,0.001,1])
                            result=''
                            answer=0           
                    except:
                        pass
                    
                    print(result,answer)
        
        screen.fill((0,0,0))
        
        for i in buttons:
            screen.blit(buttons[i][0],buttons[i][1])
        screen.blit(answerText,answerText_rect)
        screen.blit(resultText,resultText_rect)
        clear=pygame.draw.circle(screen,(255,0,255),(w//2,46),10)
        backspace=pygame.draw.circle(screen,(255,255,25),(w//2,220),10)
        screen.blit(iNum12proMax_text,iNum12proMax_rect)
        
        pygame.display.update()
        