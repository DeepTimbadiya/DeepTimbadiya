import random

# Snake Water Gun or Rock Paper Scissors
def gameWin(comp, comp2):
    # If two values are equal, declare a tie!
    if comp == comp2:
        return None

    # Check for all possibilities when computer chose s
    elif comp == 's':
        if comp2=='w':
            return False
        elif comp2=='g':
            return True
    
    # Check for all possibilities when computer chose w
    elif comp == 'w':
        if comp2=='g':
            return False
        elif comp2=='s':
            return True
    
    # Check for all possibilities when computer chose g
    elif comp == 'g':
        if comp2=='s':
            return False
        elif comp2=='w':
            return True

print("Comp1 Turn: Snake(s) Water(w) or Gun(g)?")
randNo1 = random.randint(1, 3) 
if randNo1 == 1:
    comp = 's'
elif randNo1 == 2:
    comp = 'w'
elif randNo1 == 3:
    comp = 'g'

print("Comp2 Turn: Snake(s) Water(w) or Gun(g)?")
randNo2 = random.randint(1, 3) 
if randNo2 == 1:
    comp2 = 's'
elif randNo2 == 2:
    comp2 = 'w'
elif randNo2 == 3:
    comp2 = 'g'
a = gameWin(comp, comp2)

print(f"Computer chose {comp}")
print(f"Computer2 chose {comp2}")

if a == None:
    print("The game is a tie!")
elif a:
    print("comp2 Win!")
else:
    print("comp2 Lose!")