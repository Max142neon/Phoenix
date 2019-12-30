# Tic Tac Toe with AI

import pygame
import time


pygame.init()


red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
cyan = (25,255,255)
black = (0,0,0)
yellow = (255,255,0)
light_green = (0,200,0)
light_red = (200,0,0)
grey = (200,200,200)

display_width=1200
display_height=600

game_display=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption(("TIC TAC TOE"))
game_display.fill(cyan)


#font used in pygame
font2=pygame.font.SysFont(None,70)
font3=pygame.font.SysFont(None,50)
font5=pygame.font.SysFont(None,70)

#scoreboard variables
r=l=str(0)
y=0

#plays music
pygame.mixer.music.load("01-Animals-Original-Mix.mp3")
pygame.mixer.music.play(-1)

#import image 
image=pygame.image.load("D:\\ammazing wallpapers\\7a7e653f7969f64ea8ae381a2c29c537.jpg")

# board connected to the displayboard in pygame ,AI works on this board and shows result in pygame displayboard
board = [' ' for x in range(10)]


#simple functions which works on board

def insertLetter(letter,pos):
    board[pos] = letter

def spaceIsFree(pos):
    return (board[pos] == ' ')

def isWinner(bo,le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

def compMove():
    possibleMoves = [x for x,letter in enumerate(board) if letter == ' ' and x!=0]
    move=0

    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy=board[:]
            boardCopy[i] = let
            if isWinner(boardCopy,let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
                    
    


def playerMove(pos1,pos2,pos3,pos4):
    pygame.draw.line(game_display,white,pos1,pos2,10)
    pygame.draw.line(game_display,white,pos3,pos4,10)
    pygame.display.update()



def compDraw(move):
    if move == 1:
        pygame.draw.circle(game_display,white,(258,214),45,10)
        pygame.display.update()
    elif move == 2:
        pygame.draw.circle(game_display,white,(455,214),45,10)
        pygame.display.update()
    elif move == 3:
        pygame.draw.circle(game_display,white,(615,214),45,10)
        pygame.display.update()
    elif move == 4:
        pygame.draw.circle(game_display,white,(258,382),45,10)
        pygame.display.update()
    elif move == 5:
        pygame.draw.circle(game_display,white,(441,382),45,10)
        pygame.display.update()
    elif move == 6:
        pygame.draw.circle(game_display,white,(615,382),45,10)
        pygame.display.update()
    elif move == 7:
        pygame.draw.circle(game_display,white,(258,512),45,10)
        pygame.display.update()
    elif move == 8:
        pygame.draw.circle(game_display,white,(444,512),45,10)
        pygame.display.update()
    elif move == 9:
        pygame.draw.circle(game_display,white,(616,512),45,10)
        pygame.display.update()


def Cpu_processor(move):
    if move == 0:
        game_display.fill(cyan)
        time.sleep(1)
        message_to_board("TIE GAME!",red,426,242)
        pygame.display.update()
    else:
        insertLetter('O',move)
        compDraw(move)


def intro_button():
    global t
    t = 0
    m = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pressed()
    
    
    if 524+200 > m[0] > 524 and 200+100 > m[1] > 200:
        pygame.draw.rect(game_display,light_green,(524,200,200,100))
        if mouse[0]== 1:
            t = 1
    else:
        pygame.draw.rect(game_display,green,(524,200,200,100))
        
    if 524+200 > m[0] > 524 and 400+100 > m[1] > 400:
        pygame.draw.rect(game_display,light_red,(524,400,200,100))
        if mouse[0]==1:
            t = -1
    else:
        pygame.draw.rect(game_display,red,(524,400,200,100))
        
    message_to_Inscreen("Play!","QUIT!",black,553,238,553,438)
            
    pygame.display.update()
    
    
def gameOver_Loop(goir,gameOver,gameExit,r,l,y):
    while gameOver==True:
            
            if goir == 1:
                
                game_display.fill(white)
                time.sleep(1)
                message_to_board(" Press c to play again or q to quit!! ",red,260,268)
                pygame.display.update()
            else:
                
                game_display.fill(white)
                time.sleep(1)
                message_to_board(" Game over !Press c to play again or q to quit!! ",red,50,280)
                pygame.display.update()

                

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                    
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        quit()
                        
                        
                    if event.key==pygame.K_c:
                        if goir == 1 and y == 0:
                            r = str(int(r)+1)
                        elif goir == 0 and y==0:
                            l = str(int(l)+1)
                        if y==1:
                            y = 0   
                        #print(r)
                        game_display.fill(cyan)
                        #board = [' ' for x in range(10)]
                        game_loop(r,l,y)


    
        
def winner_line(bo,le):
    if (bo[7] == le and bo[8] == le and bo[9] == le):
        pygame.draw.line(game_display,yellow,(195,526),(258,526),10)
        pygame.display.update()
        time.sleep(1)
        pygame.draw.line(game_display,yellow,(258,526),(539,526),10)
        pygame.display.update()
        time.sleep(1)
        pygame.draw.line(game_display,yellow,(539,526),(679,526),10)
        pygame.display.update()
        
    elif (bo[4] == le and bo[5] == le and bo[6] == le):
        pygame.draw.line(game_display,yellow,(195,370),(340,370),10)
        pygame.display.update()
        time.sleep(1)
        pygame.draw.line(game_display,yellow,(340,370),(536,370),10)
        pygame.display.update()
        time.sleep(1)
        pygame.draw.line(game_display,yellow,(536,370),(679,370),10)
        pygame.display.update()
    
    elif (bo[1] == le and bo[2] == le and bo[3] == le):
        pygame.draw.line(game_display,yellow,(195,215),(262,215),10)
        pygame.display.update()
        time.sleep(1)
        pygame.draw.line(game_display,yellow,(262,215),(440,215),10)
        pygame.display.update()
        time.sleep(1)
        pygame.draw.line(game_display,yellow,(440,215),(671,215),10)
        pygame.display.update()
        
    elif (bo[1] == le and bo[4] == le and bo[7] == le):
        pygame.draw.line(game_display,yellow,(260,155),(260,301),10)
        pygame.display.update()
        time.sleep(1)
        pygame.draw.line(game_display,yellow,(260,301),(260,454),10)
        pygame.display.update()
        time.sleep(1)
        pygame.draw.line(game_display,yellow,(260,454),(260,568),10)
        pygame.display.update()
    elif (bo[2] == le and bo[5] == le and bo[8] == le):
        pygame.draw.line(game_display,yellow,(437,155),(437,298),10)
        pygame.display.update()
        time.sleep(1)
        pygame.draw.line(game_display,yellow,(437,298),(437,455),10)

        pygame.display.update()
        time.sleep(1)
        pygame.draw.line(game_display,yellow,(437,455),(437,568),10)
        pygame.display.update()
    elif (bo[3] == le and bo[6] == le and bo[9] == le):
        pygame.draw.line(game_display,yellow,(609,155),(609,299),10)
        pygame.display.update()
        time.sleep(1)
        pygame.draw.line(game_display,yellow,(609,299),(609,456),10)
        pygame.display.update()
        time.sleep(1)
        pygame.draw.line(game_display,yellow,(609,456),(609,568),10)
        pygame.display.update()
    elif (bo[1] == le and bo[5] == le and bo[9] == le):
        pygame.draw.line(game_display,yellow,(207,168),(338,289),10)
        pygame.display.update()
        time.sleep(1)
        pygame.draw.line(game_display,yellow,(338,289),(537,451),10)
        pygame.display.update()
        time.sleep(1)
        pygame.draw.line(game_display,yellow,(537,451),(680,570),10)
        pygame.display.update()
    elif (bo[3] == le and bo[5] == le and bo[7] == le):
        pygame.draw.line(game_display,yellow,(193,577),(338,463),10)
        pygame.display.update()
        time.sleep(1)
        pygame.draw.line(game_display,yellow,(338,463),(528,302),10)
        pygame.display.update()
        time.sleep(1)
        pygame.draw.line(game_display,yellow,(528,302),(685,156),10)
        pygame.display.update()
    

def score_board(r,l):
    

    pygame.draw.rect(game_display,green,(969,174,200,100))
    pygame.draw.rect(game_display,red,(974,363,200,100))
    pygame.display.update()
    message_to_scoreboard("WINS:-",r,994,224,1117,224,black)
    pygame.display.update()
    message_to_scoreboard("LOSES:-",l,993,415,1139,415,black)
    pygame.display.update()
    
    
    


def message_to_scoreboard(msg1,msg2,pos1,pos2,pos3,pos4,color):
    screen_text=font3.render(msg1,True,color)
    screen_text1=font3.render(msg2,True,color)
    game_display.blit(screen_text,[pos1,pos2])
    game_display.blit(screen_text1,[pos3,pos4])

def message_to_Inscreen(msg1,msg2,color,pos1,pos2,pos3,pos4):
    screen_text = font5.render(msg1,True,color)
    screen_text1 = font5.render(msg2,True,color)
    game_display.blit(screen_text,[pos1,pos2])
    game_display.blit(screen_text1,[pos3,pos4])    


def message_to_board(msg,color,pos1,pos2):
    screen_text=font2.render(msg,True,color)
    game_display.blit(screen_text,[pos1,pos2])
    

def game_loop(r,l,y):
    global board
    
    q = w = 0
    

    

    goir=0
    clock=pygame.time.Clock()
    gameExit=False
    gameOver=False
    message_to_board("WELCOME TO TIC TAC TOE",white,334,132)
    pygame.display.update()
    
    

    




    while not gameExit:
        
        
        pygame.time.delay(100)
        #print(board)
        


        #m=pygame.mouse.get_pos()
        #print(m)


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
        if q==0:
            intro_button()
        if t == 1:
            if q == 0:
                q += 1
                w=1
                
                Board(r,l)
        elif t == -1:
            gameExit = True

                
        key = pygame.key.get_pressed()
        if w == 1:
            if not(isBoardFull(board)):
                if not(isWinner(board,'O')):
                    if key[pygame.K_1]:
                        if spaceIsFree(1):
                            #print(1)
                            insertLetter('X',1)
                            playerMove((207,163),(316,269),(207,269),(316,163))
                            if not(isWinner(board,'X')):
                                move = compMove()
                                Cpu_processor(move)
                            else:
                                winner_line(board,'X')
                                game_display.fill(cyan)
                                time.sleep(2)
                                board = [' ' for x in range(10)]
                                message_to_board("You won this time! Good Job",green,226,242)
                                pygame.display.update()
                                gameOver_Loop(1,True,False,r,l,y)
                                
                        else:
                            message_to_board("Sorry,this place is occupied!",green,30,34)
                            pygame.display.update()
                            time.sleep(1)
                            pygame.draw.rect(game_display,cyan,(30,34,700,100))
                            pygame.display.update()

                    
                    elif key[pygame.K_2]:
                        if spaceIsFree(2):
                            #print(2)
                            insertLetter('X',2)
                            playerMove((380,165),(504,273),(380,273),(504,165))
                            if not(isWinner(board,'X')):
                                move = compMove()
                                Cpu_processor(move)
                            else:
                                winner_line(board,'X')
                                game_display.fill(cyan)
                                time.sleep(2)
                                board = [' ' for x in range(10)]
                                message_to_board("You won this time! Good Job",green,226,242)
                                pygame.display.update()
                                gameOver_Loop(1,True,False,r,l,y)
                        else:
                            message_to_board("Sorry,this place is occupied!",green,30,34)
                            pygame.display.update()
                            time.sleep(1)
                            pygame.draw.rect(game_display,cyan,(30,34,700,100))
                            pygame.display.update()


                    elif key[pygame.K_3]:
                        if spaceIsFree(3):
                            #print(3)
                            insertLetter('X',3)
                            playerMove((559,166),(661,266),(568,266),(661,166))
                            if not(isWinner(board,'X')):
                                move = compMove()
                                Cpu_processor(move)
                            else:
                                winner_line(board,'X')
                                game_display.fill(cyan)
                                time.sleep(2)
                                board = [' ' for x in range(10)]
                                message_to_board("You won this time! Good Job",green,226,242)
                                pygame.display.update()
                                gameOver_Loop(1,True,False,r,l,y)
                        else:
                            message_to_board("Sorry,this place is occupied!",green,30,34)
                            pygame.display.update()
                            time.sleep(1)
                            pygame.draw.rect(game_display,cyan,(30,34,700,100))
                            pygame.display.update()


                    elif key[pygame.K_4]:
                        if spaceIsFree(4):
                            #print(4)
                            insertLetter('X',4)
                            playerMove((195,324),(317,416),(195,416),(317,324))
                            if not(isWinner(board,'X')):
                                move = compMove()
                                Cpu_processor(move)
                            else:
                                winner_line(board,'X')
                                game_display.fill(cyan)
                                time.sleep(2)
                                board = [' ' for x in range(10)]
                                message_to_board("You won this time! Good Job",green,226,242)
                                pygame.display.update()
                                gameOver_Loop(1,True,False,r,l,y)
                        else:
                            message_to_board("Sorry,this place is occupied!",green,30,34)
                            pygame.display.update()
                            time.sleep(1)
                            pygame.draw.rect(game_display,cyan,(30,34,700,100))
                            pygame.display.update()


                    elif key[pygame.K_5]:
                        if spaceIsFree(5):
                            #print(5)
                            insertLetter('X',5)
                            playerMove((376,332),(501,422),(376,423),(501,332))
                            if not(isWinner(board,'X')):
                                move = compMove()
                                Cpu_processor(move)
                            else:
                                winner_line(board,'X')
                                game_display.fill(cyan)
                                time.sleep(2)
                                board = [' ' for x in range(10)]
                                message_to_board("You won this time! Good Job",green,226,242)
                                pygame.display.update()
                                gameOver_Loop(1,True,False,r,l,y)
                        else:
                            message_to_board("Sorry,this place is occupied!",green,30,34)
                            pygame.display.update()
                            time.sleep(1)
                            pygame.draw.rect(game_display,cyan,(30,34,700,100))
                            pygame.display.update()


                    elif key[pygame.K_6]:
                        if spaceIsFree(6):
                            #print(6)
                            insertLetter('X',6)
                            playerMove((554,324),(663,422),(562,422),(656,324))
                            if not(isWinner(board,'X')):
                                move = compMove()
                                Cpu_processor(move)
                            else:
                                winner_line(board,'X')
                                game_display.fill(cyan)
                                time.sleep(2)
                                board = [' ' for x in range(10)]
                                message_to_board("You won this time! Good Job",green,226,242)
                                pygame.display.update()
                                gameOver_Loop(1,True,False,r,l,y)
                        else:
                            message_to_board("Sorry,this place is occupied!",green,30,34)
                            pygame.display.update()
                            time.sleep(1)
                            pygame.draw.rect(game_display,cyan,(30,34,700,100))
                            pygame.display.update()


                    elif key[pygame.K_7]:
                        if spaceIsFree(7):
                            #print(7)
                            insertLetter('X',7)
                            playerMove((197,479),(318,567),(197,567),(318,479))
                            if not(isWinner(board,'X')):
                                move = compMove()
                                Cpu_processor(move)
                            else:
                                winner_line(board,'X')
                                game_display.fill(cyan)
                                time.sleep(2)
                                board = [' ' for x in range(10)]
                                message_to_board("You won this time! Good Job",green,226,242)
                                pygame.display.update()
                                gameOver_Loop(1,True,False,r,l,y)
                        else:
                            message_to_board("Sorry,this place is occupied!",green,30,34)
                            pygame.display.update()
                            time.sleep(1)
                            pygame.draw.rect(game_display,cyan,(30,34,700,100))
                            pygame.display.update()


                    elif key[pygame.K_8]:
                        if spaceIsFree(8):
                            #print(8)
                            insertLetter('X',8)
                            playerMove((376,476),(501,567),(376,567),(501,476))
                            if not(isWinner(board,'X')):
                                move = compMove()
                                Cpu_processor(move)
                            else:
                                winner_line(board,'X')
                                game_display.fill(cyan)
                                time.sleep(2)
                                board = [' ' for x in range(10)]
                                message_to_board("You won this time! Good Job",green,226,242)
                                pygame.display.update()
                                gameOver_Loop(1,True,False,r,l,y)
                        else:
                            message_to_board("Sorry,this place is occupied!",green,30,34)
                            pygame.display.update()
                            time.sleep(1)
                            pygame.draw.rect(game_display,cyan,(30,34,700,100))
                            pygame.display.update()


                    elif key[pygame.K_9]:
                        if spaceIsFree(9):
                            #print(9)
                            insertLetter('X',9)
                            playerMove((554,479),(663,567),(562,567),(663,476))
                            if not(isWinner(board,'X')):
                                move = compMove()
                                Cpu_processor(move)
                            else:
                                winner_line(board,'X')
                                game_display.fill(cyan)
                                time.sleep(2)
                                board = [' ' for x in range(10)]
                                message_to_board("You won this time! Good Job",green,226,242)
                                pygame.display.update()
                                gameOver_Loop(1,True,False,r,l,y)
                        else:
                            message_to_board("Sorry,this place is occupied!",green,30,34)
                            pygame.display.update()
                            time.sleep(1)
                            pygame.draw.rect(game_display,cyan,(30,34,700,100))
                            pygame.display.update()
                else:
                    winner_line(board,'O')
                    game_display.fill(cyan)
                    time.sleep(2)
                    board = [' ' for x in range(10)]
                    message_to_board("Sorry Cpu won this time!",red,322,240)
                    
                    pygame.display.update()
                    gameOver_Loop(0,True,False,r,l,y)
            else:
                
                game_display.fill(cyan)
                time.sleep(2)
                board = [' ' for x in range(10)]
                gameOver_Loop(1,True,False,r,l,1)
          
        
    pygame.quit()
    quit()


def Board(r,l):
    game_display.fill(cyan)

    score_board(r,l)

    #vertical lines of board
    pygame.draw.line(game_display,black,(346,152),(346,575),20)
    pygame.draw.line(game_display,black,(538,153),(538,575),20)

    #Horizontal lines of board
    pygame.draw.line(game_display,black,(190,300),(680,300),20)
    pygame.draw.line(game_display,black,(190,454),(680,454),20)

    pygame.display.update()

    


    


    

game_loop(r,l,0)











            
