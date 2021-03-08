import random

def game(comp,you):
    if(comp==you):
     print("No one wins")
    if comp=='s':
        if you=='w':
          return False
        elif you=='g':
             return True
    elif comp=='w':
        if you=='s':
         return True
        elif you=='g':
             return False
    if comp=='g':
        if you=='w':
         return True
        elif you=='s':
             return False
                               

print("Comp Turn: Snake(s) Water (w) or Gun(g)?")
randNo=random.randint(1,3)
if (randNo==1):
 comp='s'
elif (randNo==2):
    comp='w'
elif (randNo==3):
        comp='g'
you=input("Your Turn: Snake(s) Water (w) or Gun(g)?")
a=game(comp,you)

print(f"Computer chose {comp}")
print(f"You chose {you}")
 

if a==None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else :
    print("You Lose!")