try:
    from decorations.progressBar import progress_bar
    import time
    import decorations.banners as banners
    from rich.console import Console
    console = Console()
    title = banners.banner("-[ LUNKY ]-")
    console.print(title, style="green")





    def hackez_console():
        global done
        global version
        done = "true"
        time.sleep(1)
        console.print("\n(svp) tapez 'credits' ou 'info' pour plus d'informations..", style="green")
        while True:
            cmd = input(f'\n{time.strftime("%H:%M:%S")} | ({system}) ->')
            if cmd.lower() == 'help':
                console.print("--------[ COMMANDS ]---------\ncredits\ninfo\nport-scanner\nvuln-scan\n\nexit", style="green")

            elif cmd.lower() == 'credits' or cmd.lower() == 'info':
                console.print(f'this version: {this_version}, new version: {version}\n{informations}', style="blue")

            elif cmd.lower().startswith("port-scanner"):
                try:
                    command = cmd.lower().replace("port-scanner ", '')
                except Exception:
                    print("ERROR")
                if command == '' or command == 'port-scanner':
                    console.print("ERROR: tapez port-scanner -h pour obtenir de l'aide", style="red")
                elif command == '-h':
                    print("--------[ OPTIONS ]--------\n-i [ip]\n-out [file.extension]")
                elif command.startswith('-i'):
                    try:
                        try:
                            options = command.split('-out ')
                        except Exception:
                            options = []
                            options.append(command)
                        ip = options[0].replace('-i ', '')
                        ip = ip.replace(' ', '')
                        out_file = options[1]
                        print(f'IP: {ip} out file: {out_file}')
                        pscan = PS.PScan()
                        pscan.initialize(ip, out_file)
                    except Exception as e:
                        print(e)
                        console.print('ERROR', style='red')
                    print(ip)


                else:
                    console.print("ERROR: option non valide. tapez port-scanner -h pour obtenir de l'aide", style="red")
            elif cmd.lower() == 'clear' or cmd.lower() == 'cls':
                if system == 'Linux':
                    os.system('clear')
                elif system == 'Windows':
                    os.system('cls')
            elif cmd.lower() == 'exit':
                bye = banners.banner("bye   : )")
                sys.exit(console.print(bye, style="purple"))
                exit()
            else:
                console.print("ERROR: invalid command", style="red")



    done = "false"
    def loading():
        while done == 'false':
            sys.stdout.write('\rchargement |')
            time.sleep(0.1)
            sys.stdout.write('\rchargement /')
            time.sleep(0.1)
            sys.stdout.write('\rchargement -')
            time.sleep(0.1)
            sys.stdout.write('\rchargement \\')
            time.sleep(0.1)
        sys.stdout.write('\rdone :)  ')


    def tool():
        global done
        t1 = threading.Thread(target=loading)
        t1.start()
        hackez_console()
        #pscan = PS.PScan()
        #pscan.initialize()


    print("                                LOADING...")
    progress_bar(0, 100, "blue")
    #1- imports
    import platform, threading, os, sys, datetime
    from requests import get
    import p_scan as PS
    progress_bar(40, 100, "blue")
    #variabili
    system = platform.system()
    this_version = '1.1.2'
    current_time = datetime.datetime.now()
    progress_bar(60, 100, "blue")
    try:
        version = get("https://pastebin.com/raw/67cuEevb").text
        versions = version.split('.')
        try:
            version = "[blue]v" + versions[0] + ".[green]" + versions[1] + "." + versions[2] + "[white]"
        except Exception:
            pass
        progress_bar(70, 100, "blue")
    except Exception:
        time.sleep(0.5)
        progress_bar(0, 100, "red")
        console.print(f"\n[!] ERROR: échec de l'obtention de la version actuelle (pas de connexion internet)", style="red")
        exit()
    try:
        informations = get("https://pastebin.com/raw/AaRffQqX").text
        progress_bar(80, 100, "blue")
    except Exception:
        time.sleep(0.5)
        progress_bar(0, 100, "red")
        console.print(f"\n[!] ERROR: pas réussi à obtenir les informations (pas de connexion internet)", style="red")
        exit()
    if this_version == version:
        old = False
    else:
        old = True
    progress_bar(90, 100, "blue")
    progress_bar(100, 100, "green")
    time.sleep(0.7)
    if system == 'Windows':
        os.system("cls")
    elif system == "Linux":
        os.system("clear")
    icon = banners.big_icon("TOOL", "LUNKY", version)
    console.print(icon)
    if old == True:
        console.print(f"\ncette version de l'outil est ancienne, mettez-la à jour en téléchargeant la nouvelle version sur GitHub\n          cette version: {this_version}   nouvelle version: {version}", style="red")
    tool()
except KeyboardInterrupt:
    print()
    bye = banners.banner("bye   : )")
    sys.exit(console.print(bye, style="purple"))
    exit()
