greeting = "Welcome to Spooky World Mad Libs"
print(greeting)
player = input("What is your name:")
print(f"Welcome, {player}. Would you like to play a game?")
answer = input("Y/N:")
while answer !="Y" and answer !="N":
  answer = input("Y/N")
if answer != "Y":
  print("Well, fine then...")
  exit()
if answer != "N":
  print("Then buckle up.")
  
noun1 = input("A noun:")
noun2 = input("Another noun:")
verbpast1 = input("Past tense verb:")

story= f"Once in an evil pumpkin patch, there was a {noun1} among us. I reached for the {noun2}. I {verbpast1} to the store."

print("--*--*--*--")

print(story)
