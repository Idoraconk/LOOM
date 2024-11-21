def lboffice_wr():
    import pyautogui as bot

    bot.PAUSE = 0.5
    bot.press('win')
    bot.write('libreoffice writer')
    bot.press('enter')
lboffice_wr()
