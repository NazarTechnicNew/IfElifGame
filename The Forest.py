


import colorama


TEXT_COLOR = colorama.Fore.CYAN
INPUT_COLOR = colorama.Fore.BLUE
CHOICE_COLOR = colorama.Fore.YELLOW
WIN_COLOR = colorama.Fore.GREEN
LOSE_COLOR = colorama.Fore.RED
SPEAK_COLOR = colorama.Fore.WHITE
FOURTH_WALL_COLOR = colorama.Fore.BLACK
ACHIVEMENT_COLOR = colorama.Fore.BLACK
SECRET_COLOR = colorama.Fore.MAGENTA


thirsty = 0
hunger = 0
lives = 3



print(f"{TEXT_COLOR}You entered the forest and now you can't exit it. You have 3 lives. There is two paths. Where will you go?")
print(f"{CHOICE_COLOR}1. Go left")
print(f"{CHOICE_COLOR}2. Go straight")
print(f"{CHOICE_COLOR}3. Go right")
user_des = input(f"{INPUT_COLOR}Select the number of your choice: ")
if user_des == "1":
    thirsty += 2
    hunger += 1
    print(f"{TEXT_COLOR}You went left and found the lake. You drank little water. You saw something that looks like a house. What will you do?")
    thirsty -= 1
    print(f"{CHOICE_COLOR}1. Go to the thing")
    print(f"{CHOICE_COLOR}2. Run away")
    user_des2 = input(f"{INPUT_COLOR}Select the number of your choice: ")
    if user_des2 == "1":
        print(f"{TEXT_COLOR}It's a house where you found food!")
        hunger -= 1
        print(f"{TEXT_COLOR} Then, you found a map to the cafe. You went there. {WIN_COLOR}You exit the forest!")
    elif user_des2 == "2":
        print(f"{TEXT_COLOR} You ran away and there is {LOSE_COLOR} nothing to do now. You are trapped here forever!")
elif user_des == "2":
    print(f"{TEXT_COLOR}You went and heard a growl. What would you do?")
    print(f"{CHOICE_COLOR}1. Go there")
    print(f"{CHOICE_COLOR}2. Wait")
    user_des3 = input(f"{INPUT_COLOR}Select the number of your choice: ")
    if user_des3 == "1":
        print(f"{TEXT_COLOR}You went there and saw Skinwalker. It saw you too and chases you. Choose quickly!")
        print(f"{CHOICE_COLOR}1. Run as fast as you can!!!")
        print(f"{CHOICE_COLOR}2. Wait")
        print(f"{CHOICE_COLOR}3. FIGHT!!!")
        user_des4 = input(f"{INPUT_COLOR}Select the number of your choice: ")
        if user_des4 == "1":
            print(f"{TEXT_COLOR}You ran as fast as you can but this creature was faster and bit your arm.\nYou hane 2 lives left. Now, you saw your friend.")
            print(f"{SPEAK_COLOR}You: What are you doing here? Aren't you at the prison?")
            print(f"{SPEAK_COLOR}Your friend: I escaped! I was running 3 days and 3 nights! I'm so hungry! Have you something to eat?")
            print(f"{SPEAK_COLOR}You: Yes, I have.")
            print(f"{TEXT_COLOR}You had 2 apples and you gave them to your friend. He ate them. But he was still hungry so he ate you. {LOSE_COLOR}You lose!")
            lives -= 2
        elif user_des4 == "2":
            print(f"{TEXT_COLOR}Skinwalker bit you again and he wanted to eat you, but seal apeared and ate skinwalker. But he was hungry, so he ate you too. What will you do?")
            lives -= 1
            print(f"{CHOICE_COLOR}1. Pass through the esophagus into the stomach")
            print(f"{CHOICE_COLOR}2. Try to exit")
            user_des5 = input(f"{INPUT_COLOR}Select the number of your choice: ")
            if user_des5 == "1":
                print(f"{TEXT_COLOR}You are in seal's stomach. {LOSE_COLOR}And you died because you've been digested!")
                lives -= 1
            elif user_des5 == "2":
                print(f"{LOSE_COLOR}You tried to exit but the seal was too strong and you died because lack of oxygen!")
                lives -= 1
        elif user_des4 == "3":
            print(f"{TEXT_COLOR}You fighted with this creation and you killed it! You cut its stomach and there was a map to WorldIT company office. What will you do?")
            print(f"{CHOICE_COLOR}1. Go there")
            print(f"{CHOICE_COLOR}2. Stay here")
            user_des6 = input(f"{INPUT_COLOR}Select the number of your choice: ")
            if user_des6 == "1":
                print(f"{TEXT_COLOR}You went to WorldIT company. There was tutor Anton. {FOURTH_WALL_COLOR}He told you that you aren't human, you are just digital text that appears as the script was written down... {LOSE_COLOR}Game Over.")
                print(f"{ACHIVEMENT_COLOR}Unlocked achivement ``Matrix``!")
            elif user_des6 == "2":
                print(f"{TEXT_COLOR}You stayed at the forest. But suddenly the blue helicopter flew to you and you jumped in. There was Gena the crocodile and he saved you. {WIN_COLOR}You win!")
                print(f"{ACHIVEMENT_COLOR}Unlocked achivement ``Gena the crocodile``!")
    elif user_des3 == "2":
        print(f"{LOSE_COLOR}You waited some time. The monster Skinwalker run into you and ate you. Game over!")
elif user_des == "3":
    print(f"{TEXT_COLOR}You went right and found something that looks like a basement. You entered it and saw a door. What will you do?")
    print(f"{CHOICE_COLOR}1. Try to open")
    print(f"{CHOICE_COLOR}2. Try to brake it")
    user_des7 = input(f"{INPUT_COLOR}Select the number of your choice: ")
    if user_des7 == "1":
        print(f"{TEXT_COLOR}It's locked.")
        print(f"{CHOICE_COLOR}1. Look for the key")
        print(f"{CHOICE_COLOR}2. Go away")
        user_des8 = input(f"{INPUT_COLOR}Select the number of your choice: ")
        if user_des8 == "1":
            print(f"{TEXT_COLOR}You found a key and opened the door! There was subway. You went home. {WIN_COLOR}You win!")
        elif user_des8 == "2":
            print(f"{LOSE_COLOR}You went away. Game over.")
        elif user_des8 == "???":
            print(f"{SECRET_COLOR}-.-- --- ..- / .- .-. . / -. --- - / ... .--. --- ... . -.. / - --- / -... . / .... . .-. . ")
    elif user_des7 == "2":
        print(f"{LOSE_COLOR}Instead of the door, you broke your head!")