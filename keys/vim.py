def vim():
    import pyautogui as bot

    bot.PAUSE = 0.5
    bot.press('win')
    bot.write('vim')
    bot.press('down', presses=2)
    bot.press('enter')
vim()
