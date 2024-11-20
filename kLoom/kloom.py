import os
import sys
import time
import pyautogui as bot

def goto():
    os.system('cls')
    def tempalte_kl():
        print("+ ==~==~==~==~==~==~====~==~==~==~==~==~== +")
        print("|                                          |")
        print("|             ..            ...            |")
        print("|       < .z@8'`        .zf'` `'tu         |")
        print("|        !@88E         x88      '8N.       |")
        print("|        '888E   u     888k     d88&       |")
        print("|         888E u@8NL   8888N.  @888F       |")
        print("|         888E`'88*'   `88888 9888%        |")
        print("|         888E .dN.      %888 '88F         |")
        print("|         888E~8888       8'   '*h=~       |")
        print("|         888E '888&    z8Weu              |")
        print("|         888E  9888.  ''88888i.   Z       |")
        print("|       ''888*' 4888' '   '8888888*        |")
        print("|          ''    ''         ^'**''         |")
        print("|                                          |")
        print("+ ==~==~==~==~==~==~====~==~==~==~==~==~== +")
        print("|                  kLOOM                   |")
        print("+ ==~==~==~==~==~==~====~==~==~==~==~==~== +")
    tempalte_kl()
    print("|       [&nk] - New Key  [&q] - Quit       |")
    print("|       [&ik] - Integrate Key              |")
    print("+ ==~==~==~==~==~==~====~==~==~==~==~==~== +")
    print("Enter the  conditional")
    chars = "/—\|"
    conditional = str(input("> "))
    if conditional == '&nk':
        while conditional == '&nk':
            import nkbot
            break
    elif conditional == '&ik':
        while conditional == '&ik':
            os.system('cls')
            tempalte_kl()
            print("Select the editor to integrate key")
            print("[Available editors: gVim, Vim]")
            print("[To acess gVim -> &egvim]")
            print("[To acess Vim -> &vim]")
            edt_ik = str(input("> "))
            if edt_ik == '&egvim':
                while edt_ik == '&egvim':
                    os.system('cls')
                    tempalte_kl()
                    print("INTEGRATE KEYS - GVIM")
                    for char in chars:
                        sys.stdout.write('\r'+'Loading gVim...'+char)
                        time.sleep(0.5)
                        sys.stdout.flush()
                        import integrateklGVIM
                    os.system('cls')
                    break
            elif edt_ik == '&vim':
                while edt_ik == '&vim':
                    os.system('cls')
                    tempalte_kl()
                    print("INTEGRATE KEYS - VIM")
                    for char in chars:
                        sys.stdout.write('\r'+'Loading Vim...'+char)
                        time.sleep(0.5)
                        sys.stdout.flush()
                        import integratedklVIM
                    os.system('cls')
                    break
            break
    elif conditional == '&q':
        while conditional == '&q':
            os.system('cls')
            sys.exit()
            break
    else:
        while conditional != '&nk' or '&q' or '&ik':
            os.system('cls')
            tempalte_kl()
            print("<                  ERROR                  >")
            print("+ ==~==~==~==~==~==~====~==~==~==~==~==~== +")
            print("| The enter conditional is invalid or      |")
            print("| different of '&nk' and '&q'              |")
            print("+ ==~==~==~==~==~==~====~==~==~==~==~==~== +")
            print("\n")
            input("\nPress ENTER to continue...")
            break
    os.system('cls')
    for char in chars:
        sys.stdout.write('\r'+'Rebooting kLOOM...'+char)
        time.sleep(0.5)
        sys.stdout.flush()
    os.system('cls')
    goto()
goto()
