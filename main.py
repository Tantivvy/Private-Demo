import time
import keyboard

print("SUNDAY DINNER \n")
time.sleep(1)
print("press SPACE  to continue")
time.sleep(1)


def opening_sequence():
    print("INT. KITCHEN, JOEL'S HOUSE - DAY")
    time.sleep(0.8)
    print()

while True:
    if keyboard.is_pressed('space'):
        opening_sequence()
        break
else:
    print("You need to press SPACE to continue!")
    time.sleep(0.5)