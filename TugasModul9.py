import os
from termcolor import colored

def pertamina_logo():
    print(colored("\n                                pertamina   \n", "white", attrs=["bold"]))

    print(colored("                           ██████████████████", "red"))
    print(colored("                             ██████████████████", "red"))
    print(colored("                               ██████████████████", "red"))
    print(colored("                                 ██████████████████", "red"))
    print(colored("                                   ██████████████████", "red"))
    print()

    print(colored("              ██████████████████", "blue") + "   " + colored("██████████████████", "green") + "   " + colored("███████  ██████  ██████   ██████   █████   ███     ███  ██  ███   ██   █████", "white"))
    print(colored("            ██████████████████", "blue") + "   " + colored("██████████████████", "green") + "     " + colored("██   ██  ██      ██   ██    ██    ██   ██  ████   ████  ██  ████  ██  ██   ██", "white"))
    print(colored("          ██████████████████", "blue") + "   " + colored("██████████████████", "green") + "       " + colored("███████  █████   ██████     ██    ███████  ██ ██ ██ ██  ██  ██ ██ ██  ███████", "white"))
    print(colored("        ██████████████████", "blue") + "   " + colored("██████████████████", "green") + "         " + colored("██       ██      ██ ██      ██    ██   ██  ██  ███  ██  ██  ██  ████  ██   ██", "white"))
    print(colored("      ██████████████████", "blue") + "   " + colored("██████████████████", "green") + "           " + colored("██       ██████  ██  ███    ██    ██   ██  ██       ██  ██  ██   ███  ██   ██", "white"))
    print(colored("    ██████████████████", "blue"))
    print(colored("  ██████████████████", "blue"))
    print(colored("██████████████████", "blue"))

def adidas_logo():
    print(colored("\n\t\t\t\t\t\t\t\t                      adidas   \n", "white", attrs=["bold"]))
    print(colored("\t\t\t\t\t\t\t\t   ███████             ████             ███████", "white"))
    print(colored("\t\t\t\t\t\t\t\t  ████████████       ████████       ████████████", "white"))
    print(colored("\t\t\t\t\t\t\t\t ███████████████    ██████████    ███████████████", "white"))
    print(colored("\t\t\t\t\t\t\t\t█████████████████  ████████████  █████████████████", "white"))
    print(colored("\t\t\t\t\t\t\t\t █████████████████ ████████████ █████████████████", "white"))
    print()
    print(colored("\t\t\t\t\t\t\t\t    ██████████████████████████████████████████", "white"))
    print()
    print(colored("\t\t\t\t\t\t\t\t       ████████████████████████████████████", "white"))
    print()
    print(colored("\t\t\t\t\t\t\t\t           █████████ ████████ █████████     ", "white"))
    print(colored("\t\t\t\t\t\t\t\t               █████    ██    █████     ", "white"))
    print()
    print(colored("\t\t\t\t\t\t\t\t     █████  ██████  ██ ██████   █████   ██████", "white"))
    print(colored("\t\t\t\t\t\t\t\t    ██   ██ ██   ██ ██ ██   ██ ██   ██ ████", "white"))
    print(colored("\t\t\t\t\t\t\t\t    ███████ ██   ██ ██ ██   ██ ███████    ████", "white"))
    print(colored("\t\t\t\t\t\t\t\t    ██   ██ ██████  ██ ██████  ██   ██ ██████", "white"))

def main():
    
    print(colored("=== PILIH LOGO ===", "cyan", attrs=["bold"]))
    print(colored("1. Logo Pertamina", "green"))
    print(colored("2. Logo Adidas", "yellow"))
    pilihan = input(colored("Masukkan pilihan Anda (1/2): ", "blue"))

    if pilihan == "1":
        pertamina_logo()
    elif pilihan == "2":
        adidas_logo()
    else:
        print(colored("Pilihan tidak valid.", "red"))

main()
