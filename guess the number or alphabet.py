print("Welcome to the guessing game!")
x = "guess the number"
y = "guess the alphabet"
game = input(f"what you want to play {x} or {y}: ")
if game == x:
  import random
  mode = input("Choose a mode: hard, easy, or normal: ").lower()
  easy = "easy"
  hard = "hard"
  normal = "normal"
  if mode == easy:
      computer = random.randint(1, 10)
      max_attempts = 5
      attempts = 0
      while attempts < max_attempts:
          data = int(input("Enter a number between 1 and 10: "))
          attempts += 1
          if data > computer:
              print("Too high, try again.")
          elif data < computer:
              print("Too low, try again.")
          else:
              print("You win!")
              break
      else:
          print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {computer}.")
  elif mode == hard:
      computer = random.randint(-500, 500)
      max_attempts = 8
      attempts = 0
      while attempts < max_attempts:
          data = int(input("Enter a number between -500 and 500: "))
          attempts += 1
          if data > computer:
              print("Too high, try again.")
          elif data < computer:
              print("Too low, try again.")
          else:
              print("You win!")
              break
      else:
          print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {computer}.")
  elif mode == normal:
      computer = random.randint(1, 100)
      max_attempts = 6
      attempts = 0
      while attempts < max_attempts:
          data = int(input("Enter a number between 1 and 100: "))
          attempts += 1
          if data > computer:
              print("Too high, try again.")
          elif data < computer:
              print("Too low, try again.")
          else:
              print("You win!")
              break
      else:
          print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {computer}.")
  else:
      print("Invalid mode selected.")
elif game == y:
  import random
  import string
  mode = input("Choose a mode: hard, easy, or normal: ").lower()
  easy = "easy"
  hard = "hard"
  normal = "normal"
  if mode == easy:
      computer = random.choice(string.ascii_lowercase[:10])  # 'a' to 'j'
      max_attempts = 5
      attempts = 0
      while attempts < max_attempts:
          data = input("Enter a letter (a-j): ").lower()
          attempts += 1
          if data > computer:
              print("Too high, try again.")
          elif data < computer:
              print("Too low, try again.")
          else:
              print("You win!")
              break
      else:
          print(f"Sorry, you've used all {max_attempts} attempts. The correct letter was {computer}.")
  elif mode == hard:
      computer = random.choice(string.ascii_lowercase[:20])  # 'a' to 't'
      max_attempts = 5
      attempts = 0
      while attempts < max_attempts:
          data = input("Enter a letter (a-t): ").lower()
          attempts += 1
          if data > computer:
              print("Too high, try again.")
          elif data < computer:
              print("Too low, try again.")
          else:
              print("You win!")
              break
      else:
          print(f"Sorry, you've used all {max_attempts} attempts. The correct letter was {computer}.")
  elif mode == normal:
      computer = random.choice(string.ascii_lowercase[:15])  # 'a' to 'o'
      max_attempts = 5
      attempts = 0
      while attempts < max_attempts:
          data = input("Enter a letter (a-o): ").lower()
          attempts += 1
          if data > computer:
              print("Too high, try again.")
          elif data < computer:
              print("Too low, try again.")
          else:
              print("You win!")
              break
      else:
          print(f"Sorry, you've used all {max_attempts} attempts. The correct letter was {computer}.")
  else:
      print("Invalid mode selected.")
else:
  print ("check your spelling")
