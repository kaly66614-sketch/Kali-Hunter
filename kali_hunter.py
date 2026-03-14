import requests
import os
import sys

# تنظيف الشاشة
os.system('clear')

def logo():
    print("\033[1;31m")
    print("      _  __    _    _       ___ ")
    print("     | |/ /   / \  | |     |_ _|")
    print("     | ' /   / _ \ | |      | | ")
    print("     | . \  / ___ \| |___   | | ")
    print("     |_|\_\/_/   \_\_____| |___|")
    print("\n   [--- KALI VULNERABILITY HUNTER ---]")
    print("   [---   STAY ETHICAL, MOHAMED   ---]")
    print("-" * 45)
    print("\033[0m")

logo()

target = input("[+] Enter Website (e.g. google.com): ")

# التأكد من وجود http في الرابط
if not target.startswith("http"):
    target = "http://" + target

vuln_paths = [
    ".env", ".git/config", "admin/", "config.php", 
    "phpinfo.php", "backup.sql", "db.php", ".htaccess",
    "robots.txt", "server-status", "dashboard/"
]

print(f"\n[*] Target: {target}")
print("[*] Starting deep scan... (Press CTRL+C to stop)\n")

found_count = 0

try:
    for path in vuln_paths:
        full_url = f"{target}/{path}"
        # السطر ده هيخليك تشوف الأداة وهي بتجرب كل رابط
        sys.stdout.write(f"\r\033[1;34m[*] Testing: {path}\033[0m")
        sys.stdout.flush()
        
        try:
            response = requests.get(full_url, timeout=10)
            if response.status_code == 200:
                print(f"\n\033[1;32m[✔] FOUND: {full_url} (Code 200)\033[0m")
                found_count += 1
            elif response.status_code == 403:
                print(f"\n\033[1;33m[!] FORBIDDEN: {full_url} (Code 403)\033[0m")
        except requests.exceptions.RequestException:
            pass

except KeyboardInterrupt:
    print("\n\n[!] Scan stopped by user.")

print("\n" + "-" * 45)
print(f"   Scan Finished. Total Vulnerabilities: {found_count}")
print("-" * 45)

