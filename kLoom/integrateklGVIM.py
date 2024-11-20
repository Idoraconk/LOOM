def gvimi():
    import pyautogui as bot

    path = r"C:\Users\cynar\OneDrive"
    def type_unicode(text):
        import pyautogui
        import pyperclip
        pyperclip.copy(text)
        pyautogui.hotkey("ctrl", "v")
    bot.PAUSE = 1
    bot.hotkey('win', 'r')
    bot.write('cmd')
    bot.press('enter')
    bot.write("cd ")
    bot.write(path)
    bot.press('enter')
    bot.write('cd ')
    type_unicode("Á")
    bot.write(r"rea de trabalho\LOOM")
    bot.press('enter')
    bot.write("gvim loom.py")
    bot.press('enter')
gvimi()