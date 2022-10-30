from sys import stdin, argv

def caesar(c, rot):
    if ord(c) >= 97 and ord(c) <= 122:
        return chr((ord(c)-97+rot)%26+97)
    elif ord(c) >= 65 and ord(c) <= 90:
        return chr((ord(c)-65+rot)%26+65)
    return c

def main(rot):
    inp = stdin.read().strip()
    print("".join(caesar(c, rot) for c in inp))

def print_help():
    print("Caesar decoder")
    print("caesar {rot}")
    print("echo ABC | caesar 13")
    
if __name__ == "__main__":
    if "-h" in argv[1:] or "--help" in argv[1:]:
        print_help()
    elif len(argv) < 2:
        print("Need to specify rot\n eg. caesar 13")
    else:
        rot = int(argv[1])
        main(rot)

