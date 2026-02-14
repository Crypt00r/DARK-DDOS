import os
import sys
import time
import random
import subprocess
from platform import system


def clearScr():
    if system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    banner = """
    
██████╗  █████╗ ██████╗ ██╗  ██╗    ██████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║  ██║███████║██████╔╝█████╔╝     ██║  ██║██║  ██║██║   ██║███████╗
██║  ██║██╔══██║██╔══██╗██╔═██╗     ██║  ██║██║  ██║██║   ██║╚════██║
██████╔╝██║  ██║██║  ██║██║  ██╗    ██████╔╝██████╔╝╚██████╔╝███████║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝

Note! : I'm Not Responsible for any illegal usage.
Coded by : Crypt0r
Instagram: theyoungycc

[+] 1. Tool Option
"""

    for line in banner.split("\n"):
        sys.stdout.write(f"\x1b[1;{random.choice(colors)}m{line}{clear}\n")
        time.sleep(0.03)


class Menu:

    def run_option(self):
        script_path = os.path.join("files", "ddos", "ddos.py")

        if not os.path.exists(script_path):
            print("\n[!] Script not found:", script_path)
            return

        try:
            subprocess.run([sys.executable, script_path])
        except Exception as e:
            print("\n[!] Error executing script:", e)

    def exit_program(self):
        print("\nClosing...\nPlease wait...")
        time.sleep(1.5)
        sys.exit()


def main():
    clearScr()
    logo()

    choice = input("CRYPT0R:~# ").strip()

    menu = Menu()

    if choice == "1":
        menu.run_option()
    elif choice.lower() in ["exit", "quit", "q"]:
        menu.exit_program()
    else:
        print("\n[!] Invalid Input!")


if __name__ == "__main__":
    main()
