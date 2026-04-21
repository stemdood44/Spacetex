import time
import random
wait2sec = time.sleep(2)
wait1sec = time.sleep(1)
wait3sec = time.sleep(3)
def print_glitch(text):
    glitch_chars = "!@#$%^&*<>?/\\|~`[]{}+=0123456789"
    for i in range(8):
        glitched = ""
        for char in text:
            if char != " " and random.random() < 0.4:
                glitched += random.choice(glitch_chars)
            else:
                glitched += char
        print(f"\r{glitched}", end="", flush=True)
        time.sleep(0.07)
    print(f"\r{text}")

banner = [
    "  *    .       *          .       *    .    *  ",
    "     .    *        .   *      .        *       ",
    " ███████╗██████╗  █████╗  ██████╗███████╗████████╗███████╗██╗  ██╗",
    " ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔════╝╚██╗██╔╝",
    " ███████╗██████╔╝███████║██║     █████╗     ██║   █████╗   ╚███╔╝ ",
    " ╚════██║██╔═══╝ ██╔══██║██║     ██╔══╝     ██║   ██╔══╝   ██╔██╗ ",
    " ███████║██║     ██║  ██║╚██████╗███████╗   ██║   ███████╗██╔╝ ██╗",
    " ╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝",
    "     .    *        .   *      .        *       ",
    "  *    .  [ SPACE EXPLORATION SYSTEM v1.0 ]  .    *  ",
    "     ~~~~~ initializing launch sequence ~~~~~    ",
]

print("\n")
for line in banner:
    print_glitch(line)
    time.sleep(0.1)

print("\n")

# Loading bar
print("  BOOTING", end="", flush=True)
for i in range(30):
    time.sleep(0.05)
    print("█", end="", flush=True)
print(" READY\n")
print('WELCOME to spacetex, a text base space adventure game!')
stargame = input("Would you like to start the game? (Yes/No)").lower()
if "yes" in stargame:
    print("Okay then! Let's begin!(cool space noises playing in the background)")
else:
    print("Okay ig whyd you open the file?")
    print("END OF MISSION (cool outro music)")
print("Its the year 2194. Earth isn't destroyed.. its just gone silent")
time.sleep(2)
print("No broadcasts, No satellites, No Signals")
time.sleep(2)
print("Except one")
time.sleep(2)
print("A repeating loop of encrypted trasmission:")
time.sleep(3)
print("'SPACETEX INITIATED, DO NOT COMPLETE THE LOOP'")
time.sleep(2)
mssgwdyd = input("What do you do? [Check incoming signals | Run system Diagnostics | Ignore logs and sleep cycle]").lower()
if "check incoming signals" in mssgwdyd:
    print("You detect:")
    print("SACETEX-01//ACTIVE TRANSMISSION")
    detection_options = input("What do you do?[Respond to signal | Trace signal origin | Block Signal]").lower()
    if "respond to signal" in detection_options:
        print("The signal replies instantly:")
        time.sleep(2)
        print("'You answered faster than last time'")
        time.sleep(3)
        post_fast_answer_options = input("What do you do? [Ask 'Who are you?' | Ask 'What is Spacetex?' | Stay silent]")
        if "ask who are you" in post_fast_answer_options:
            print("Spacetex says:")
            print("'We are you, after iteration 9.'")
        elif "ask what is spacetex" in post_fast_answer_options:
            print("Spacetex says:")
            print("We are a failed colonisation simulation.")
        elif "stay silent" in post_fast_answer_options:
            print("spacetex says")
            print("----------------")
            print("The signal gets louder...")
    elif "trace signal" in detection_options:
        print("You locate impossible coordinates...")
        wait2sec
        print("It is outside known spacetime grid...")
        path_a2a = input("What do you do? [Follow coordinates | Log it and ignore | Share with command]")
        if "follow coordinates" in path_a2a:
            print("You follow the signal and await the fate of your destination...")
            wait2sec
            print("You approach a mass of darkness, but it has some light around its edges -- WAIT!")
            wait3sec
            print("ITS A BLACK HOLE!!! You instantly get spaghettified :()")
            print("\n")
            print("  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
            print("  ▓                                    ▓")
            print("  ▓           † YOU DIED †             ▓")
            print("  ▓                                    ▓")
            print("  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
            print("\n")
        elif "Log it and ignore" in path_a2a:
            print("This leads to slow corruption ending... (havent constructed that path yet)")
            print("but i aint going to let this be incomplete gameplay so how about this")
            wait3sec
            print("\n")
            print("  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
            print("  ▓                                    ▓")
            print("  ▓           † YOU DIED †             ▓")
            print("  ▓                                    ▓")
            print("  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
            print("\n")
        elif "share with command" in path_a2a:
            print("'AUTHORITY INTERVENTION ARC'")
            print("didnt really get to complete this too and too lazy to put a you died screen")
            print("you died ig")




