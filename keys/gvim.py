def gvim():
    import pyautogui as bot

    bot.PAUSE = 0.5
    bot.press('win')
    bot.write('gvim')
    bot.press('down',presses=2)
    bot.press('enter')
gvim()
