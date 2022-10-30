from sys import stdin, argv

def caesar(c, rot):
    if ord(c) >= 97 and ord(c) <= 122:
        return chr((ord(c)-97+rot)%26+97)
    elif ord(c) >= 65 and ord(c) <= 90:
        return chr((ord(c)-65+rot)%26+65)
    return c
    
def main():
    inp = stdin.read().strip()
    print("".join(caesar(c, 13) for c in inp))

def print_help():
    print("Rot13 or caesar cipher with 13 rot")
    print("echo ACB | rot13")

if __name__ == "__main__":
    if "-h" in argv[1:] or "--help" in argv[1:]:
        print_help()
    else:
        main()
