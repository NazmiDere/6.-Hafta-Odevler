import random
print("*"*15,"GAME OF FINDING NUMBER","*"*15)
print("""-----> please select a number between zero to one hundred in your mind
system will try to find that number.
please give information about situation as write '-' and '+'
if your number is found by system please write '*'\n\n""")
a = 0                                                                               #set 2 variable to use in random randrange
b = 100
try:
    while True:
        estimation = random.randrange(a+1,b)                                        #estimate numbers betweeen a+1(a+1 because a included in random modul estimation) to b
        print("system's estimation is:{}\n".format(estimation))                     #print the estimation
        situation=input("situation:")                                               #take a situation from user to use in other estimation
        if situation == "*":                                                        #when system estimate correctly users will enter '*' and the loop will end
            print("your number has been found by system:{}".format(estimation))     
            break
        if situation == "-":                                                        #if user will enter '-' variable b will be estimation
            b = estimation
        elif situation == "+":                                                      #if user will enter '+' variable a will be estimation
            a = estimation
        else:
            print("you should enter '-', '+' or '*'\n")                             #if user enter something wrong it will appear this text and the loop will end
            break
except ValueError:
    print("your input is incorrect,your number should be estimated by system")
except:
    print("something happened wrong,please try again")
