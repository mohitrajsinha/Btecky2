def start():
    print("You are standing in a dark forest.")
    print("There is a path to your left and a path to your right.")

    choice = input("Which path do you take? (left or right) ")

    if choice == "left":
        go_left()
    elif choice == "right":
        go_right()
    else:
        print("Invalid choice.")
        start()

def go_left():
    print("You walk down the left path.")
    print("You come to a clearing with a pond.")
    print("There is a house on the other side of the pond.")

    choice = input("Do you swim across the pond or go back? (swim or back) ")

    if choice == "swim":
        swim()
    elif choice == "back":
        start()
    else:
        print("Invalid choice.")
        go_left()

def go_right():
    print("You walk down the right path.")
    print("You come to a cave.")
    print("Do you enter the cave or go back?")

    choice = input("(enter or back) ")

    if choice == "enter":
        enter_cave()
    elif choice == "back":
        start()
    else:
        print("Invalid choice.")
        go_right()

def swim():
    print("You swim across the pond.")
    print("You reach the house and knock on the door.")
    print("The door opens and a friendly old woman greets you.")
    print("She invites you in for tea and cookies.")
    print("You have a lovely time and then go home.")

def enter_cave():
    print("You enter the cave.")
    print("It is dark and spooky.")
    print("You hear a noise behind you.")
    print("You turn around and see a giant spider!")
    print("You run out of the cave and never go back.")

start()
