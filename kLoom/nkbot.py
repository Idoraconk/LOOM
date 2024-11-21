def nk():
    import pyautogui as bot 

    bot.PAUSE = 0.5
    bot.hotkey('win', 'r')
    bot.write('idle3')
    bot.press('enter')
nk()