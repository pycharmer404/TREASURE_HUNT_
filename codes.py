from random import randint

while True:
 def initialize():
    print()
    print("You will be asked to enter number of moves in which you would like to find the treasure")
    print()
    print("Please enter valid moves between 4 and 14")
    print()
    print("You will need to find treasure between those moves")
    print()
    print("All the best")
    global dessert, tr, tc, found, moves, notfound
    dessert = [[(".") for col in range(30)]for row in range (10)]
    tr = randint(0,9)
    tc = randint(0,29)
    moves = 0
    notfound = True
    
 def printgrid():
    print("Treasure is burried under one of these:")
    for row in range (10):
        print()
        for col in range(30):
            print(dessert[row][col], end=" ")
    
 def move():
    global dessert, tr, tc, moves, notfound
    print()

    while True:
        moves = int(input("In how many moves?(4 to 14) "))
        if moves > 3 and moves < 15 :
          break
        else:
          print("invalid")

 def dighole():
    global dessert, tr, tc, moves, notfound
    turn = 1
    while notfound == True and turn <= moves:
          dr = int(input("Enter row to dig= "))-1
          dc = int(input("Enter col to dig= "))-1
          if 0 <= dr <= 9 and 0 <= dc <= 29:
           if dr==tr and dc==tc:
              won(dr,dc)          
           else:
              dessert[dr][dc] = "O"
              printgrid()
              print()
              hints(dr,dc)
          else:
              print("invalid")
          turn += 1
              
    if notfound == True:
        print("Out of moves")
        print("The correct row and col is: ", tr+1, tc+1)


 def won(dr,dc):
     global dessert, tr, tc, moves, notfound
     dessert[dr][dc] = "$"
     printgrid()
     print()
     print("You found the treasure :: Congractulations")
     notfound = False
     dighole()
    
 def hints(dr,dc):
    global dessert, tr, tc, found

    if dr == tr:
        print("correct row")
    elif dr > tr:
        print("dig up")
    elif dr < tr:
        print("dig down")

    if dc == tc:
        print("correct column")
    elif dc < tc:
        print("dig right")
    elif dc > tc:
        print("dig left")



     
 ask = input("Play this game:(y/n) ")
 if ask == "y" :
       initialize()
       printgrid()
       move()
       dighole()
 else:
       print("BYE BYE")
       break

 



