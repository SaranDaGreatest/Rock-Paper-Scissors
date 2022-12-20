import random

def game():#Creates a function so that it can be repeated continuesly if wanted
  sign = input("Please input either rock or paper or scissors: ") # asks the user to chose their sign

  bot = ["rock", "paper", "scissors"] #The 3 choice the computer has to choose from in string form
  bot = random.choice(bot) #Randomly choose one of the 3 choices from above 

  if sign == bot: #If the sign the user chose is the same as the sign of the computer, it's a tie
    print("You chose" , sign , "and I chose" , bot)
    print("It's a tie")
  elif sign == "rock": #The user chooses rock
    if bot == "paper":#If the computer chooses paper, the user loses
      print("You chose" , sign , "and I chose" , bot)
      print("You lost")
    if bot == "scissors":#If the computer chooses scissors, the user wins
      print("You chose" , sign , "and I chose" , bot)
      print("You win")
  elif sign == "paper": #The user chooses paper
    if bot == "rock":#If the computer chooses rock, the user wins
      print("You chose " , sign , "and I chose" , bot)
      print("You win")
    if bot == "scissors":#If the computer chooses scissors, the user loses
      print("You chose" , sign , "and I chose" , bot)
      print("You lost")
  elif sign == "scissors": #The user chooses scissors
    if bot == "rock":#If the computer chooses rock, the user lost
      print("You chose" , sign , "and I chose" , bot)
      print("You lost")
    if bot == "paper":#If the computer chooses paper, the user wins
      print("You chose" , sign , "and I chose" , bot)
      print("You win")
  else:
    print("Please input your sign correctly") #The user did not input rock or paper or scissors correctly

while True: #A forever while loop
  game() #Runs the function from above
  end = input("Play again (Y/N)?: ") #Asks if the user wants to play again
  if end == "N":
    print("Good bye...")
    break
  elif end =="Y":
    print("Ok...")