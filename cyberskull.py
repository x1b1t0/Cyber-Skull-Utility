import os
import time
import subprocess
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# ASCII Skull
skull = f"""{Fore.RED}
               uuuuuuu
           uu$$$$$$$$$$$uu
        uu$$$$$$$$$$$$$$$$$uu
       u$$$$$$$$$$$$$$$$$$$$$u
      u$$$$$$$$$$$$$$$$$$$$$$$u
     u$$$$$$$$$$$$$$$$$$$$$$$$$u
     u$$$$$$$$$$$$$$$$$$$$$$$$$u
     u$$$$$$"   "$$$"   "$$$$$$u
     "$$$$"      u$u       $$$$"
      $$$u       u$u       u$$$
      $$$u      u$$$u      u$$$
       "$$$$uu$$$   $$$uu$$$$"
        "$$$$$$$"   "$$$$$$$"
          u$$$$$$$u$$$$$$$u
           u$"$"$"$"$"$"$u
uu        $$u$ $ $ $ $ $u$$       uu
u$$$uu     "$$$u$u$u$u$$$"     uu$$$u
$$$$$$$$$$$uu ""$$$$$$$$$$uuuu$$$$$$$$$$
u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$u
u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$u
        uuuu$$$$$$$$$$$$$$$$$$$$uuuu
u$$$uuu$$$$$$$$$uu   $$$$   uuuu$$$$$$$$$uuu$$$
$$$$$$$$$$$                 $$$$$$$$$$
      $$$$   $$$$$$$$$$$$$$   $$$$
       "$$$$   $$$$$$$$$$$   $$$$"
         "$$$$uu   """   uu$$$$"
           "$$$$$$uuu$$$$$$"
              "$$$$$$$$$"
               "$$$$$"
                 uuu
"""

def install_package(package):
    """Installs the specified package using the system's package manager"""
    print(f"{Fore.YELLOW}Installing {package}...{Fore.RESET}")
    if os.name == 'nt':  # Windows
        subprocess.run(["choco", "install", package, "-y"], check=True)
    else:  # Linux/Mac
        subprocess.run(["sudo", "apt-get", "install", package, "-y"], check=True)

def scan_network():
    """Performs a network scan using Nmap"""
    if not shutil.which("nmap"):
        install_package("nmap")
    target = input("Enter target IP or range: ")
    os.system(f"nmap -sV {target}")

def enumerate_shares():
    """Enumerates SMB shares"""
    if not shutil.which("smbclient"):
        install_package("smbclient")
    target = input("Enter target IP: ")
    os.system(f"smbclient -L \\\\{target} -N")

def check_firewall():
    """Checks firewall rules"""
    if os.name == 'nt':
        os.system("netsh advfirewall show allprofiles state")
    else:
        if not shutil.which("ufw"):
            install_package("ufw")
        os.system("sudo ufw status verbose")

def sniff_traffic():
    """Captures network traffic using tcpdump"""
    if not shutil.which("tcpdump"):
        install_package("tcpdump")
    print("Capturing network traffic...")
    os.system("sudo tcpdump -i any -c 50")

def exploit_ssh():
    """Attempts a brute-force attack on SSH (for authorized testing only)"""
    if not shutil.which("hydra"):
        install_package("hydra")
    target = input("Enter SSH target (IP or domain): ")
    user = input("Enter username: ")
    wordlist = input("Enter path to password wordlist: ")
    os.system(f"hydra -l {user} -P {wordlist} {target} ssh")

def exit_program():
    """Exits the program"""
    print("Exiting...")
    time.sleep(1)
    exit()

def menu():
    """Displays the menu"""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    print(skull)
    print(f"{Fore.YELLOW}       ╔═══════════════════╗")
    print(f"{Fore.YELLOW}       ║  {Fore.GREEN}CyberSkull Utility {Fore.YELLOW}║")
    print(f"{Fore.YELLOW}       ╚═══════════════════╝")
    print(f"{Fore.CYAN}  [1] Network Scan (Nmap)")
    print(f"{Fore.CYAN}  [2] Enumerate SMB Shares")
    print(f"{Fore.CYAN}  [3] Check Firewall Rules")
    print(f"{Fore.CYAN}  [4] Sniff Network Traffic")
    print(f"{Fore.CYAN}  [5] SSH Brute Force (Hydra)")
    print(f"{Fore.CYAN}  [0] Exit")
    print("\n")

def main():
    """Main function controlling the menu loop"""
    while True:
        menu()
        choice = input(f"{Fore.MAGENTA}Select an option: {Fore.RESET}")

        if choice == "1":
            scan_network()
        elif choice == "2":
            enumerate_shares()
        elif choice == "3":
            check_firewall()
        elif choice == "4":
            sniff_traffic()
        elif choice == "5":
            exploit_ssh()
        elif choice == "0":
            exit_program()
        else:
            print(f"{Fore.RED}Invalid option. Try again.")

        input(f"\n{Fore.YELLOW}Press Enter to continue...")  # Pause

if __name__ == "__main__":
    main()
