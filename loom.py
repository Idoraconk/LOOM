import os
import time
import sys
import webbrowser as web

def goto():
    os.system('cls')
    def template_loom():
        print("+ =~==~==~==~==~==~==~==~==~==~==~<=>~==~==~==~==~==~==~==~==~==~==~= +")
        print("|                                                                     |")
        print("|                                                  .                  |")  
        print("|                                              ;JLRPcJ2r              |") 
        print("|                                            Zgs;,Xw.:rUBB.           |")
        print("|                                           BGa:  cL  :5aLBc          |") 
        print("|                                          Bv .XL :r ;Pr  .B:         |") 
        print("|                                         sB    :rcZQH     7B         |")
        print("|                          .              JDsDPwJMQBBg;7rr:7B         |")
        print("|                     .:;RBBB             :J  ::s7:Jc.     ;B         |")
        print("|          ,,  :;7LUHZEgZggBBBBBBBBBB6H67r;B;. L; .r rOROa1Br.B       |")
        print("|         sBBa55KP2SUL77L7HQMBOiJ2KpGRBBBBBBBQBBBQMGHgBBBBBBrHB;      |")
        print("|         rBBO1L7L;;,7wXUc2MggQ7..    Pc     S1;LHROQG77OBBBBMBr      |")
        print("|         :BBQBBBBBBBQBQPJUpDggQBQBQgKEBUcc7sLp6g6RPr,r:, rQG         |")
        print("|         :BBRJgi;spDQZSRBgMBRDMQBBBBBQBBBBRROZZSJM61 ZD1JGBQ         |")
        print("|         :QBRsL6aScrri:;PXRB1rr5RBgBBMQQBBQBBBBBMgRpsBBL1gBB         |")
        print("|         ,BBBBBQQEZKaJ5OPQPwU22sc7JsJ72SBXcJJsLaBBBGQQs  :BB         |")
        print("|         ,BBaJaEBBBBBBBBQBgBDP5s77;r;rr:  .:;rr2QBBJwp257PQB         |")
        print("|         ,BBPSgpL.,QBX5:.:BQQRBBBBBBBQBSc:.     BBB  :i71GBQ         |")
        print("|         :QBBBBBEJsBE      B::;sJSrrJKRBBBBBBBBBBBB       Kp         |")
        print("|         .Bg. :sOQBBBBBBBprQEcJ;           ,ivw6BBB                  |")
        print("|                     ,rSRBQBBBQBBOwv:.          BBB                  |")
        print("|                             ,75QBBBBQBBBZwr:.  BBB                  |")
        print("|                                     :c6BBQBQBBBBBQ                  |")
        print("|                                            .:71BBB                  |")
        print("|                                                1gB                  |")
        print("|                                                                     |")             
        print("|       ooooo          .oooooo.     .oooooo.   ooo        ooooo       |")
        print("|       `888'         d8P'  `Y8b   d8P'  `Y8b  `88.       .888'       |")
        print("|        888         888      888 888      888  888b     d'888        |")
        print("|        888         888      888 888      888  8 Y88. .P  888        |")
        print("|        888         888      888 888      888  8  `888'   888        |")
        print("|        888       o `88b    d88' `88b    d88'  8    Y     888        |")
        print("|       o888ooooood8  `Y8bood8P'   `Y8bood8P'  o8o        o888o       |")
        print("|                                                                     |")
        print("+ =~==~==~==~==~==~==~==~==~==~==~<=>~==~==~==~==~==~==~==~==~==~==~= +")
    template_loom()
    print("Enter the key to access the automatic process you want to perform")
    key = str(input("> "))
    chars = "/—\|"
    #RAWS
    list_rawK = ["GAGO :3", "GVIM", "VIM", "LIBREOFFICE", "LIBREOFFICE WRITER", "MICROSOFT EDGE", "YOUTUBE"]
    list_rawKC = ["QUIT", "WINDOWS EXPLORER", "WINDOWS CONFIGURATIONS", "EXECUTE (win + r)", "LOOM KEYS LIST", "URL ACESS", "GO TO THE LOOM MENU"]
    #KEYS
    list_keys = ["gago", "gvim", "vim", "lboffice", "lboffice%wr", "micro", "youtube"]
    list_command_keys = [":q", ":we", ":config", ":exe", ":keys%list", ":url", ":$m"] 
    import keys
    #KEYS BEGIN
    #Microsoft Edge Key
    if key == 'micro':
        while key == 'micro':
            print("\n")
            for char in chars:
                sys.stdout.write('\r'+'Initializing Microsoft Edge...'+char)
                time.sleep(0.5)
                sys.stdout.flush()
                import keys.micro
            os.system('cls')
            template_loom()
            print("Initialization of Microsoft Edge - Process Completed!")
            break
    #Gago :3 Key
    elif key == 'gago':
        while key == 'gago':
            print("\n")
            for char in chars:
                sys.stdout.write('\r'+'Initializing Gago :3...'+char)
                time.sleep(0.5)
                sys.stdout.flush()
                import keys.gago
            os.system('cls')
            template_loom()
            print("Initialization of Gago :3 - Process Completed! You are Gagogged!")
            break
    #LibreOffice Key
    elif key == 'lboffice':
        while key == 'lboffice':
            print("\n")
            for char in chars:
                sys.stdout.write('\r'+'Initializing LibreOffice...'+char)
                time.sleep(0.5)
                sys.stdout.flush()
                import keys.lboffice
            os.system('cls')
            template_loom()
            print("Initialization of LibreOffice - Process Completed!")
            break
    #LibreOffice Writter Key
    elif key == 'lboffice%wr':
        while key == 'lboffice%wr':
            print("\n")
            for char in chars:
                sys.stdout.write('\r'+'Initializing LibreOffice Writter...'+char)
                time.sleep(0.5)
                sys.stdout.flush()
                import keys.lbofficewr
            os.system('cls')
            template_loom()
            print("Initialization of LibreOffice Writter - Process Completed!")
            break
    #Vim Key
    elif key == 'vim':
        while key == 'vim':
            print("\n")
            for char in chars:
                sys.stdout.write('\r'+'Initializing Vim...'+char)
                time.sleep(0.5)
                sys.stdout.flush()
                import keys.vim
            os.system('cls')
            template_loom()
            print("Initialization of Vim - Process Completed!")
            break
    #gVim Key
    elif key == 'gvim':
        while key == 'gvim':
            print("\n")
            for char in chars:
                sys.stdout.write('\r'+'Initializing gVim...'+char)
                time.sleep(0.5)
                sys.stdout.flush()
                import keys.gvim
            os.system('cls')
            template_loom()
            print("Initialization of gVim - Process Completed!")
            break
    #YouTube Key
    elif key == 'youtube':
        while key == 'youtube':
            for char in chars:
                sys.stdout.write('\r'+'Initializing YouTube...'+char)
                time.sleep(0.2)
                sys.stdout.flush()
                import keys.youtube
            os.system('cls')
            template_loom()
            print("Initialization of YouTube - Process Completed!")
            break
    #KEYSBASICEND
    #COMMAND KEYS ONLY
    #Command Key :q
    elif key == ':q':
        os.system('cls')
        sys.exit()
    #Command Key :we
    elif key == ':we':
        os.system('cls')
        template_loom()
        import hotkeys.hwe
        print(":hotkey")
        print(":hotkey - Windows Explorer")
        print(":hotkey - [acessed] - (win + e)")
        time.sleep(0.7)
    #Command Key :config
    elif key == ':config':
        os.system('cls')
        template_loom()
        import hotkeys.hconfig
        print(":hotkey")
        print(":hotkey - Windows Configurations")
        print(":hotkey - [acessed] - (win + i)")
        time.sleep(0.7)
    #Command Key :exe
    elif key == ':exe':
        os.system('cls')
        template_loom()
        import hotkeys.hexe
        print(":hotkey")
        print(":hotkey - Execute")
        print(":hotkey - [acessed] - (win + r)")
        time.sleep(0.7)
    #Command Key :keys%list
    elif key == ':keys%list':
        while key == ':keys%list':
            os.system('cls')
            print("+ ==~==~==~==~==~==~===~==~=~==~====~==~==~==~==~==~==~==~==~==~==~== +")
            print("|                                                                     |")
            print("|       ooooo          .oooooo.     .oooooo.   ooo        ooooo       |")
            print("|       `888'         d8P'  `Y8b   d8P'  `Y8b  `88.       .888'       |")
            print("|        888         888      888 888      888  888b     d'888        |")
            print("|        888         888      888 888      888  8 Y88. .P  888        |")
            print("|        888         888      888 888      888  8  `888'   888        |")
            print("|        888       o `88b    d88' `88b    d88'  8    Y     888        |")
            print("|       o888ooooood8  `Y8bood8P'   `Y8bood8P'  o8o        o888o       |")
            print("|                                                                     |")
            print("+ ==~==~==~==~==~==~===~==~=~==<KEYS>==~==~==~==~==~==~==~==~==~==~== +")
            print("LIST OF KEYS")
            print("[name of the key] -> [key]")
            text = ''
            textkc = ''
            for rawl, keyl in zip(list_rawK, list_keys):
                text += "\n {} -> {} ".format(rawl, keyl)
            print(text)
            print("\n+ ==~==~==~==~==~==~===~==~=~==~====~==~==~==~==~==~==~==~==~==~==~== +")
            print("LIST OF COMMAND KEYS")
            print("[command of the key] -> [key%command]")
            for rawkc, keyc in zip(list_rawKC, list_command_keys):
                textkc += "\n {} -> {}".format(rawkc, keyc)
            print(textkc)
            print("\n")
            input("\nPress ENTER to continue...")
            os.system('cls')
            goto()
            break
    elif key == ':url':
        os.system('cls')
        print("+ ==~==~==~==~==~==~===~==~=~==~====~==~==~==~==~==~==~==~==~==~==~== +")
        print("|                                                                     |")
        print("|       ooooo          .oooooo.     .oooooo.   ooo        ooooo       |")
        print("|       `888'         d8P'  `Y8b   d8P'  `Y8b  `88.       .888'       |")
        print("|        888         888      888 888      888  888b     d'888        |")
        print("|        888         888      888 888      888  8 Y88. .P  888        |")
        print("|        888         888      888 888      888  8  `888'   888        |")
        print("|        888       o `88b    d88' `88b    d88'  8    Y     888        |")
        print("|       o888ooooood8  `Y8bood8P'   `Y8bood8P'  o8o        o888o       |")
        print("|                                                                     |")
        print("+ ==~==~==~==~==~==~===~==~=~==<URL>==~==~==~==~==~==~==~==~==~==~==  +")
        print("Enter the URL")
        print('Header: "http://www.mylinkname.com"')
        url_w = str(input("> "))
        if url_w == ':$m':
            while url_w == ':$m':
                os.system('cls')
                goto()
        else:
            web.open(url_w)
            for char in chars:
                sys.stdout.write('\r'+'\nOpen the url...'+char)
                time.sleep(0.3)
                sys.stdout.flush()
            time.sleep(0.3)
            os.system('cls')
    elif key == ':kloom':
        while key == ':kloom':
            os.system('cls')
            for char in chars:
                sys.stdout.write('\r'+'\nOpen kLOOM...'+char)
                time.sleep(0.3)
                sys.stdout.flush()
                import kloomlau
            time.sleep(0.3)
            os.system('cls')
            break
    else:
        while key != list_keys or list_command_keys:
            os.system('cls')
            print("+ ==~==~==~==~==~==~===~==~=~==~====~==~==~==~==~==~==~==~==~==~==~== +")
            print("|                                                                     |")
            print("|       ooooo          .oooooo.     .oooooo.   ooo        ooooo       |")
            print("|       `888'         d8P'  `Y8b   d8P'  `Y8b  `88.       .888'       |")
            print("|        888         888      888 888      888  888b     d'888        |")
            print("|        888         888      888 888      888  8 Y88. .P  888        |")
            print("|        888         888      888 888      888  8  `888'   888        |")
            print("|        888       o `88b    d88' `88b    d88'  8    Y     888        |")
            print("|       o888ooooood8  `Y8bood8P'   `Y8bood8P'  o8o        o888o       |")
            print("|                                                                     |")
            print("+ ==~==~==~==~==~==~==~==~==~==~<ERROR>~==~==~==~==~==~==~=~==~==~==  +")
            print("|              The enter key was invalid, try a available             |")
            print("|              key agin or register a new key                         |")
            print("+ ==~==~==~==~==~==~===~==~=~==~====~==~==~==~==~==~==~==~==~==~==~== +")
            print("\n")
            input("\nPress ENTER to continue...")
            os.system('cls')
            goto()
            break
    #KEYS ENDING
    #LOADING SCREEN
    def loading_configurations():
        os.system('cls')
        for char in chars:
            sys.stdout.write('\r'+'Rebooting LOOM system...'+char)
            time.sleep(0.5)
            sys.stdout.flush()
        os.system('cls')
        print("Reboot LOOM system - Process Completed!")
        for char in chars:
            sys.stdout.write('\r'+'Rebooting Keys configuration...'+char)
            time.sleep(0.5)
            sys.stdout.flush() 
        os.system('cls')
        print("Reboot LOOM system - Process Completed!")
        print("Reboot Keys configuration - Process Completed!")
        for char in chars:
            sys.stdout.write('\r'+'Processing Reset_loom...'+char)
            time.sleep(0.2)
            sys.stdout.flush() 
        os.system('cls')
        print("Reboot LOOM system - Process Completed!")
        print("Reboot Keys configuration - Process Completed!")
        print("Processing Reset_loom - Process Completed!")
        time.sleep(0.1)
        import reset_loom
    loading_configurations()
    if loading_configurations == True:
        key_to_bot = str(input(""))
        if key_to_bot == ':q':
            while key_to_bot == ':q':
                os.system('cls')
                sys.exit()
                break
goto()

                                      