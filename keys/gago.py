import pyautogui as bot

def type_unicode(text):
    import pyautogui
    import pyperclip
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")
bot.PAUSE = 0.5
path1 = r"cd C:\Users\cynar\OneDrive"
bot.hotkey('win','r')
bot.write('cmd')
bot.press('enter')
bot.write(path1)
bot.press('enter')
bot.write('cd ')
type_unicode("Á")
bot.write("rea de trabalho")
bot.press('enter')
bot.write('cd LOOM')
bot.press('enter')
bot.write('start gago.jpg')
bot.press('enter')
bot.press('f11')