import pyautogui as bot
import sys
import os

os.system('cls')
bot.PAUSE = 1.5
def type_unicode(text):
    import pyautogui
    import pyperclip
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")
path1 = r"cd C:\Users\cynar\OneDrive"
bot.hotkey('win', 'r')
bot.write('cmd')
bot.press('enter')
#COLOR KLOOM
bot.write('color 2')
bot.press('enter')
bot.write(path1)
bot.press('enter')
bot.write('cd ')
type_unicode("Á")
bot.write("rea de trabalho")
bot.press('enter')
bot.write('cd LOOM\kLoom')
bot.press('enter')
bot.write('python kloom.py')
bot.press('enter')