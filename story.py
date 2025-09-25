def intro():
    print("You wake up in a dark forest. You can go left, center, or right.")
    choice = input("Which direction do you choose? (left/center/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "center":
        center_path()
    elif choice == "right":
        right_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")
    print("You pick up the sword, feeling its magical power surge through you.")
    print("The sword glows brighter as you take each step forward.")  # <-- new line
    print("You encounter a fierce dragon!")
    print("You bravely fight the dragon and emerge victorious!")
    print("After defeating the dragon, you find a chest full of gold!")

def center_path():
    print("You walk down the center path and find a peaceful clearing.")
    print("Birds are singing, and the sun warms your face. You feel at peace.")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")

if __name__ == "__main__":
    intro()
