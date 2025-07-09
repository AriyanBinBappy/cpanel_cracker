import random
import string

def print_banner():
    banner = r"""
  ___       _          ____             _       ____      _               
 / _ \  ___| |_ ___   |  _ \  __ _ _ __| | __  / ___|   _| |__   ___ _ __ 
| | | |/ __| __/ _ \  | | | |/ _` | '__| |/ / | |  | | | | '_ \ / _ \ '__|
| |_| | (__| || (_) | | |_| | (_| | |  |   <  | |__| |_| | |_) |  __/ |   
 \___/ \___|\__\___/  |____/ \__,_|_|  |_|\_\  \____\__, |_.__/ \___|_|   
                                                    |___/                 
 ____                            _ 
/ ___|  __ _ _   _  __ _ _ __ __| |
\___ \ / _` | | | |/ _` | '__/ _` |
 ___) | (_| | |_| | (_| | | | (_| |
|____/ \__, |\__,_|\__,_|_|  \__,_|
          |_|                      

    🛠️ Cpanel Password Genarator 
    👤 Made by: Ariyan Bin Bappy
    ☠️  Group: Octo Dark Cyber Squad 
    ⚠️  For authorized testing only 
  

"""
    print(banner)

def generate_usernames(base_names, count=100):
    usernames = set()
    while len(usernames) < count:
        base = random.choice(base_names)
        suffix = str(random.randint(0, 9999))
        username = f"{base}{suffix}"
        usernames.add(username.lower())
    return list(usernames)

def generate_passwords(count=100, length_range=(6,12), use_upper=True, use_digits=True, use_special=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += "!@#$%^&*()-_+=<>?"

    passwords = set()
    while len(passwords) < count:
        length = random.randint(*length_range)
        pwd = ''.join(random.choice(chars) for _ in range(length))
        passwords.add(pwd)
    return list(passwords)

def generate_combos(usernames, passwords, max_combos=1000):
    combos = set()
    attempts = 0
    while len(combos) < max_combos and attempts < max_combos * 10:
        user = random.choice(usernames)
        pwd = random.choice(passwords)
        combo = f"{user}:{pwd}"
        combos.add(combo)
        attempts += 1
    return list(combos)

def main():
    print_banner()

    base_names = ["admin", "user", "cpanel", "webmaster", "root", "test", "host", "server"]

    user_count = int(input("How many usernames to generate? (default 100): ") or "100")
    pwd_count = int(input("How many passwords to generate? (default 100): ") or "100")
    combo_count = int(input("How many combos to generate? (default 1000): ") or "1000")

    usernames = generate_usernames(base_names, user_count)
    passwords = generate_passwords(pwd_count)

    combos = generate_combos(usernames, passwords, combo_count)

    with open("combos.txt", "w") as f:
        for c in combos:
            f.write(c + "\n")

    print(f"\nGenerated {len(combos)} combos and saved to combos.txt")

if __name__ == "__main__":
    main()
