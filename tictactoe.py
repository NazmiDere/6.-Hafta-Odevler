import random
print("*"*15,"X O X GAME","*"*15)
print("play against computer(if you enter 'q' you will quit from game)\ncomputer will be O") 
board = [["___","___","___"],                                                   #set the board which users play on it
         ["___","___","___"],
         ["___","___","___"]]
for i in board:                                                                 #print the board with for loop
    print("\n\t".expandtabs(30),*i)
winning_situation = [[[0, 0], [1, 0], [2, 0]],                                  #set the situation which one side will win
                     [[0, 1], [1, 1], [2, 1]],
                     [[0, 2], [1, 2], [2, 2]],
                     [[0, 0], [0, 1], [0, 2]],
                     [[1, 0], [1, 1], [1, 2]],
                     [[2, 0], [2, 1], [2, 2]],
                     [[0, 0], [1, 1], [2, 2]],
                     [[0, 2], [1, 1], [2, 0]]]

move_table = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]            #set the situation which the computer will play random
x_situation = []                                                                #set a empty list to insert x's move
o_situation = []                                                                #set a empty list to insert o's move

question=input("""\n\n                                                          
-(1)you will start at first
-(2)computer will start at first
please select one choice and press its number:""")                              #ask which side will start to user
if question == "1":                                                             #if user write 1 user will start
    turn = 0
if question == "2":                                                             #if user write 2 computer will start
    turn = 1            
try:
    while True:
        if turn % 2 == 0:                                                       #use 'turn' variable to which side will start
            mark = "X".center(3)                                                #if the turn is x variable 'mark' will be "X".center(3)
        elif turn % 2 == 1:                                                     
            mark = "O".center(3)                                                #if the turn is o variable 'mark' will be 
        print("\n\nplayer:{}".format(mark))                                     #print which side will play
        

        if mark == "X".center(3):                                               #if the 'mark' variable is X user will play                      
            x = input("please play your line move(1,2,3):")                     #to 'x' variable,user will enter where want to move in line
            if x == "q":                                                        #if user enter q game will end
                break
            y = input("please play your column move(1,2,3):")                   #to 'y' variable,user will enter where want to move in column
            if y == "q":                                                        #if user enter q game will end
                break
            x = int(x)-1                                                        #reduce the variables one point for system using                                                                                              
            y = int(y)-1

        
        if mark == "O".center(3):                                               
            while True:
                [x,y] = random.choice(move_table)                               #computer will play random                               
                for i in winning_situation:                                     #use loop in winning situation to computer play not random,because sometimes computer will play sensible 
                    if len( x_situation ) + len( o_situation ) == 9:            #if every move is played,system will quit
                        quit()
                    elif i[0] in o_situation and i[1] in o_situation:           #check that two O is in the same line               
##                        print("1",i[0] in o_situation and i[1] in o_situation)  
                        [x,y] = i[2]                                            #if they are in the same line computer will play the other(third) blank                               
                        break                                                   
                    elif i[1] in o_situation and i[2] in o_situation:
##                        print("2",i[1] in o_situation and i[2] in o_situation)    #you can see that which if block is running 
                        [x,y] = i[0]
                        break
                    elif i[0] in o_situation and i[2] in o_situation:
##                        print("3",i[0] in o_situation and i[2] in o_situation)
                        [x,y] = i[1]
                        break
                    elif ([x,y] in x_situation) or ( [x,y] in o_situation):     #if [x,y] is filled by one side     
                        [x,y] = random.choice(move_table)                       #move another random choice
                        break
                    for i in winning_situation:                                 #and again use the for loop in winning situation to computer play sensible according to X                                
                        if i[0] in x_situation and i[1] in x_situation:         #check that two O is in the same line
##                            print("4",i[0] in x_situation and i[1] in x_situation)
                            [x,y] = i[2]                                        #if they are in the same line computer will play the other(third) blank                           
                            break
                        elif i[1] in x_situation and i[2] in x_situation:
##                            print("5",i[1] in x_situation and i[2] in x_situation)    #you can see that which if block is running
                            [x,y] = i[0]
                            break
                        elif i[0] in x_situation and i[2] in x_situation:
##                            print("6",i[0] in x_situation and i[2] in x_situation)
                            [x,y] = i[1]
                            break
                        elif ([x,y] in x_situation) or ( [x,y] in o_situation): #if [x,y] is filled by one side
                            [x,y] = random.choice(move_table)                   #move another random choice
                            break
           
                if  board[1][1] == "___":                                       
                    [x,y] = [1,1]
                    break

                if ( [x,y] in x_situation ) or ( [x,y] in o_situation ):        #if the computer want to play somewhere is filled,the loop will start again
                    continue
                else:                                                           #else the loop will end
                    break              
                    

        if board[x][y] == "___":                                                #if the game board is blank                                                
            board[x][y] = mark                                                  #the blank will be 'mark' variable which is one side of the game
            if mark == "X".center(3):                                           #if 'mark' variable is X 
                x_situation += [[x,y]]                                          #insert the move of X into the x_situation list
            elif mark == "O".center(3):                                         #if 'mark' variable is O 
                o_situation += [[x,y]]                                          #insert the move of X into the o_situation list
            turn += 1                                                           #and icrease the 'turn' variable one point in order to other side play
        else:                                                                   #if there is filled which user want to play
            print("\nyou can not play this move,please try again")              #print this text
        
        for i in board:                                                         #print game board in each turn
            print("\n\t".expandtabs(30),*i)

        for i in winning_situation:                                             #use for loop in winning situation to determine which side win
            x = [a for a in i if a in x_situation]                              #if i in x_situation we will insert them in x list 
            o = [a for a in i if a in o_situation]                              #if i in o_situation we will insert them in o list
            if len(x) == len(i):                                                #if length of x list is equal to length of i which is 3
                print("X kazandi")                                              #the side of X will win
                quit()                                                          #and quit from program
            if len(o) == len(i):                                                
                print("O kazandi")                                              
                quit()                                                          
except ValueError:
    print("you enter something different,please try again")
except:
    print("please try again")
