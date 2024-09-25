import pygame
import sys
import mouse
import keyboard
 
# Initialize Pygame
pygame.init()

speed = 0.0001 
pygame.joystick.init()

def check_for_joystick():
    """Checks if a joystick is connected and initializes it."""
    global joystick
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        return joystick
    else:
        return None

# Ensure at least one joystick is connected
joystick = check_for_joystick() 
if joystick is None:
    print("No joystick connected!")
    pygame.quit()
    sys.exit()

keys = [chr(i).lower() for i in range(ord('A'), ord('Z') + 1)]
skeys = []
skeys.append(' ')
skeys.append(',')
skeys.append('.')
skeys.append(':')
skeys.append('/')
skeys.append('\\')
skeys.append('\'')
skeys.append('+')
skeys.append('-')
skeys.append(';')
skeys.append('_')
skeys.append('!')
skeys.append('\"')
skeys.append('%')
skeys.append('(')
skeys.append(')')
skeys.append('{')
skeys.append('}')
skeys.append('#')
skeys.append('*')
skeys.append('=')
skeys.append('<')
skeys.append('>')

for i in range(0, 10):
    keys.append(str(i))
    skeys.append(str(i))
    
key_num = 0
key_lock = False
tast = keys
special_keys = False

while True:
    joystick = check_for_joystick()

    if joystick is not None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.JOYBUTTONDOWN:
                if joystick.get_button(6):
                    pygame.quit()
                    sys.exit()
                
                if joystick.get_button(8):
                    special_keys = not special_keys
                    if special_keys is True:
                        tast = skeys
                    else:
                        tast = keys
                    
                    try:
                        print(f"{key_num}: \'{tast[key_num]}\'")
                    except:
                        key_num = 0
                        print(f"{key_num}: \'{tast[key_num]}\'")
                    
                elif joystick.get_button(9):
                    key_lock = not key_lock
                    if key_lock is True:
                        print(f"{key_num}: \'{tast[key_num].upper()}\'")
                    else:
                        print(f"{key_num}: \'{tast[key_num].lower()}\'")
                    
                if joystick.get_button(4):
                    if key_num != 0:
                        key_num -= 1
                    else:
                        key_num = len(tast) - 1
                    
                    if key_lock is True:
                        print(f"{key_num}: \'{tast[key_num].upper()}\'")
                    else:
                        print(f"{key_num}: \'{tast[key_num].lower()}\'")
                    
                elif joystick.get_button(5):
                    if key_num != len(tast) - 1:
                        key_num += 1
                    else:
                        key_num = 0
                        
                    if key_lock is True:
                        print(f"{key_num}: \'{tast[key_num].upper()}\'")
                    else:
                        print(f"{key_num}: \'{tast[key_num].lower()}\'")
                
                if joystick.get_button(0):
                    mouse.click('left')
                
                if joystick.get_button(3):
                    keyboard.write('\n')
                
                if joystick.get_button(2):
                    if key_lock is True:
                        keyboard.press("shift")
                        keyboard.press(str(tast[key_num].upper()))
                        keyboard.release("shift")
                    else:
                        keyboard.press(str(tast[key_num].lower()))
                
                if joystick.get_button(1):
                    keyboard.press('backspace')
        # Hallo ,..012345678Acd
        axis_x = joystick.get_axis(0)
        axis_y = joystick.get_axis(1)
        
        dpad = joystick.get_hat(0)  # 0 ist der Index fÃ¼r das erste D-Pad
        if dpad[1] == 1:
            mouse.wheel(0.1)
        elif dpad[1] == -1:
            mouse.wheel(-0.1)
        
        lt_axis = joystick.get_axis(4) 
        rt_axis = joystick.get_axis(5) 
        
        lt_value = (lt_axis + 1) / 2
        rt_value = (rt_axis + 1) / 2
        
        if lt_value != 0:
            mouse.press()
        else:
            mouse.release()
            
        x, y = mouse.get_position()
        
        if not rt_value == 0:
            mouse.click('right')
        
        mouse.move(x + round(axis_x), y + round(axis_y), duration=speed)
    

    else:
        print("Joystick disconnected! Waiting for reconnection...")
        pygame.joystick.quit()
        while joystick is None:
            pygame.joystick.init()
            joystick = check_for_joystick()
            pygame.joystick.quit()
            pygame.time.wait(500)  # Wait a bit before checking again
            
        pygame.joystick.init()
        print("Joystick reconnected!")
