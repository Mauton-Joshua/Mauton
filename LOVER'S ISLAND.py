# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 15:21:34 2023

@author: AYOOLUWA-MAUTON
"""

print('''         __,,,__
                ,-""-,-"       "-,-""-,
               /,-' , .-'-.7.-'-. , '-,\
               \(    /  _     _  \    )/
                '-,  { (0)   (0) }  ,-'
                 /    >  .---.  <    \
                |/ .-'   \___/   '-. \|
                {, /  ,_       _,  \ ,}
                \ {,    \     /    ,} /
                 ',\.    '---'    ./,'
             _.-""""""-._     _.-""""""-._
           .'            `._.`            '.
         _/_               _                \
      .'`   `\            | |                \
     /        |           | |                 ;
     |        /           |_|                 |
     \  ;'---'    _    ___  _  _  ___         ;
      '. ;       | |  /   \| || ||  _|     _ ;
        `-\      | |_ | | || |/ /|  _|   .' `,
           `\    |___|\___/ \__/ |___|  |     \
             \            _ _           \     |
         jgs  `\         | | |         /`   _/
    ,-""-.    .'`\       | | |       /`-,-'` .-""-,
   /      `\.'    `\     \___/     /`    './`      \
  ;  .--.   \       '\           /'       /   .--.  ;
  | (    \   |,       '\       /'        |   /    ) |
   \ ;    }             ;\   /;         `   {    ; /
    `;\   \         _.-'  \ /  `-._         /   /;`
      \ \__.'   _.-'       Y       `-._    '.__//
       '.___,.-'                       `-.,___.'
''')
print("Welcome to lovers island")
print("Please help Ash to find Teddy the love bear")
play =input("Will you help Ash? type 'Y' or 'N' \n").upper()
if play =="Y":
    print("Let's get going then.")
    
    seaport= input("You start at the seaport, which boat do you take to reach the lovers island? blue, red, orange and green \n").lower()
    
    if seaport == "blue":
        print("Whoa this boat is super fast, we'll reach the island in no time")
    elif seaport == "red":
        print("This boat is not that bad")
        boat = input("Well done! You have reached the lovers island. Now we need to find Teddy. Do you wait till night or go now when it is bright and clear? 'Y' or 'N'").upper()
        if boat =="Y":
            print("Alright let's get moving, Thank you for helping me thus far")
        else:
            print("That's too bad, we can't see at night guess I can't find Teddy anymore. \n GAME OVER!")
        
    else:
        print("Oops this boat is unable to move")
        path = input("You have reached a junction, turn 'left', 'right' or take the 'central' path").lower()
        if path =="right":
            print("Checkpoint reached. \n path 1 or 2?")
        elif path =="central":
             print("You have reached another checkpoint. \n Please select either path '1' or '2'")
        else:
             print("Game over!")
    pathway = input("Please select a pathway between path 1 and 2")
    if pathway =="1":
        print("I see Teddy over there! \n Thank you for helping me find Teddy!")
    else:
        print("Thank you for trying we couldn't find Teddy")

else:
    print("I could really use your help though.")


    
      

