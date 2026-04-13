import os, time, random
os.system("clear")
print("\033[1;32m")
print("      [ SPECIALIST AUDIT TOOL ]")
print("            BY ROKOKAITOS\n")
def audio():
    os.system("termux-tts-speak Access-Granted")
def lluvia():
    print("\033[1;32m")
    for _ in range(50):
        print("".join(random.choice("0123456789ABCDEF") for _ in range(60)))
        time.sleep(0.02)
    print("\033[0m")
passw = input("Contraseña: ")
if passw == "1234":
    audio()
    lluvia()
    print("[+] ACCESO CONCEDIDO")
else:
    print("Error")


git clone https://github.com/Rokokaitos867/Specialist-Audit-Tool

python specialist_crack.py" > README.md

