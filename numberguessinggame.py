import random

start = int(input("enter staring point"))
end = int(input("enter ending point"))

uniquenum = random.randint(start,end)
print("Let's Start the Game.")
while True:
    num = int(input(f"Guess the number between {start} and {end}: "))

    if num>=uniquenum:
        print("Too High!")
    elif num<=uniquenum:
        print("Too Low!")
    else :
        print("You WIN!")
        break