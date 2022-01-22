import pyautogui as pg
import time

if pyautogui.hotkey('ctrl', 'shift', 's'): #for starting the spammer
	while True:
    	pg.write("..")
    	pg.press("enter")
    	if pyautogui.hotkey('ctrl', 'shift', 'e'): #for ending the spammer
    		break
#if the hotkeys won't work. Please contact me!
