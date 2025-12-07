import hashlib
import itertools
import string
import time
import os

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                  🔥 PASSWORD CRACKER TOOL (OFFLINE) 🔥                      ║
# ║                         Coded with 💀 by SADHIN                              ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

def loading_animation():
    print("\033[91m" + "═" * 80 + "\033[0m")
    print("\033[91m╔{'═' * 78}╗\033[0m")
    print("\033[91m║\033[0m" + " " * 25 + "\033[1;91m⚡ OFFLINE PASSWORD CRACKER ⚡\033[0m" + " " * 25 + "\033[91m║\033[0m")
    print("\033[91m║\033[0m" + " " * 23 + "\033[1;93mEducational Tool v1.0 - Use Responsibly\033[0m" + " " * 23 + "\033[91m║\033[0m")
    print("\033[91m╚{'═' * 78}╝\033[0m")
    print("\033[91m" + "═" * 80 + "\033[0m")
    
    print("\n\033[1;95m[*] Initializing Cracker Modules...\033[0m")
    time.sleep(1.5)
    print("\033[1;92m[✔] Ready to Crack! 🔥\033[0m\n")

def md5_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

def brute_force_crack(target_hash, charset=string.ascii_lowercase + string.digits, max_length=6):
    print("\033[1;94m[*] Starting Brute-Force Attack (Max Length: {})\033[0m".format(max_length))
    start_time = time.time()
    attempts = 0
    
    for length in range(1, max_length + 1):
        for combo in itertools.product(charset, repeat=length):
            password = ''.join(combo)
            attempts += 1
            if md5_hash(password) == target_hash:
                end_time = time.time()
                print("\n\033[1;92m[✔] Password Found: {}\033[0m".format(password))
                print("\033[1;93mTime Taken: {:.2f} seconds | Attempts: {}\033[0m".format(end_time - start_time, attempts))
                return password
            if attempts % 10000 == 0:
                print("\r\033[1;91m[>] Trying: {} (Attempts: {})\033[0m".format(password, attempts), end="")
    print("\n\033[1;91m[!] Password Not Found in Brute-Force Mode.\033[0m")
    return None

def dictionary_crack(target_hash, wordlist_file):
    if not os.path.exists(wordlist_file):
        print("\033[1;91m[!] Wordlist File Not Found: {}\033[0m".format(wordlist_file))
        return None
    
    print("\033[1;94m[*] Starting Dictionary Attack with: {}\033[0m".format(wordlist_file))
    start_time = time.time()
    attempts = 0
    
    with open(wordlist_file, 'r') as file:
        for line in file:
            password = line.strip()
            attempts += 1
            if md5_hash(password) == target_hash:
                end_time = time.time()
                print("\n\033[1;92m[✔] Password Found: {}\033[0m".format(password))
                print("\033[1;93mTime Taken: {:.2f} seconds | Attempts: {}\033[0m".format(end_time - start_time, attempts))
                return password
            if attempts % 1000 == 0:
                print("\r\033[1;91m[>] Trying: {} (Attempts: {})\033[0m".format(password, attempts), end="")
    print("\n\033[1;91m[!] Password Not Found in Dictionary.\033[0m")
    return None

def main():
    os.system('clear')
    loading_animation()
    
    print("\033[1;96m[1] Brute-Force Attack (Simple Chars)\033[0m")
    print("\033[1;96m[2] Dictionary Attack (Need Wordlist File)\033[0m")
    print("\033[1;96m[0] Exit\033[0m")
    
    choice = input("\033[1;93m[>] Select Option: \033[0m")
    
    target_hash = input("\033[1;93m[>] Enter MD5 Hash to Crack: \033[0m").lower()
    
    if choice == '1':
        max_length = int(input("\033[1;93m[>] Max Password Length (Default 6): \033[0m") or 6)
        brute_force_crack(target_hash, max_length=max_length)
    elif choice == '2':
        wordlist_file = input("\033[1;93m[>] Enter Wordlist File Path (e.g., rockyou.txt): \033[0m")
        dictionary_crack(target_hash, wordlist_file)
    elif choice == '0':
        print("\033[1;91m[>] Exiting Tool. Stay Safe! 🔥\033[0m")
    else:
        print("\033[1;91m[!] Invalid Option.\033[0m")

if __name__ == "__main__":
    main()
